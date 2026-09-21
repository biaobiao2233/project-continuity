#!/usr/bin/env python3
"""Read-only structural checks for explicit project execution snapshots.

This is NOT an authorization service, lock, remote-state reader, or acceptance
engine. It executes no commands and writes no files. Exit 0 means supplied
fields are mechanically consistent, not that a project is accepted or live.
"""
from __future__ import annotations

import argparse
from datetime import datetime
import json
from pathlib import Path
import re
import sys
from typing import Any

MAX_BYTES = 256 * 1024
IMMUTABLE_REF = re.compile(r"(?:git:)?(?:[0-9a-f]{40}|[0-9a-f]{64})$|sha256:[0-9a-f]{64}$")
LIMITS = ("Supplied snapshot only. No GitHub/live queries, identity verification, "
          "authorization, locking, command execution, merge, deployment, or project acceptance.")


class InputError(ValueError):
    """Invalid or ambiguous input, with no input payload echoed."""


def unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise InputError("Duplicate JSON key; regenerate an unambiguous snapshot.")
        result[key] = value
    return result


def load_json(path: Path) -> dict[str, Any]:
    try:
        with path.open("rb") as stream:
            raw = stream.read(MAX_BYTES + 1)
        if len(raw) > MAX_BYTES:
            raise InputError("Input exceeds the 256 KiB snapshot limit.")
        value = json.loads(raw.decode("utf-8"), object_pairs_hook=unique_object)
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError) as exc:
        raise InputError("Cannot read a bounded UTF-8 JSON object.") from exc
    return obj(value, "snapshot")


def obj(value: Any, field: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise InputError(f"{field} must be an object.")
    return value


def items(value: Any, field: str) -> list[Any]:
    if not isinstance(value, list):
        raise InputError(f"{field} must be an array.")
    if len(value) > 256:
        raise InputError(f"{field} exceeds the 256-item bound.")
    return value


def text(value: Any, field: str) -> str:
    if not isinstance(value, str) or not value.strip() or len(value) > 2048:
        raise InputError(f"{field} must be a non-empty bounded string.")
    if any(ord(char) < 32 for char in value):
        raise InputError(f"{field} contains control characters.")
    return value


def ref(value: Any, field: str) -> str:
    value = text(value, field)
    if not IMMUTABLE_REF.fullmatch(value):
        raise InputError(f"{field} must be a full Git SHA or sha256 artifact reference.")
    return value


def stamp(value: Any, field: str) -> str:
    value = text(value, field)
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if parsed.tzinfo is None:
            raise ValueError("timezone missing")
    except ValueError as exc:
        raise InputError(f"{field} must be an ISO timestamp with timezone.") from exc
    return value


def flag(value: Any, field: str) -> bool:
    if not isinstance(value, bool):
        raise InputError(f"{field} must be a boolean.")
    return value


def finding(code: str, detail: str) -> dict[str, str]:
    return {"code": code, "detail": detail}


def evidence(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip()) and len(value) <= 2048


def resources(value: Any) -> list[dict[str, str]]:
    result = []
    for raw in items(value, "resources"):
        item = obj(raw, "resource")
        kind = text(item.get("kind"), "resource.kind")
        if kind not in {"code", "runtime", "production", "central", "contract"}:
            raise InputError("Unknown resource kind.")
        host = text(item.get("host"), "resource.host").lower()
        key = text(item.get("key"), "resource.key").replace("\\", "/")
        if any(piece in {".", ".."} for piece in key.split("/")):
            raise InputError("Resource keys must already be canonical; no dot segments.")
        key = re.sub(r"/+", "/", key).rstrip("/") or "/"
        if re.match(r"^[A-Za-z]:/", key):
            key = key.lower()
        if kind == "code" and not (key.startswith("/") or re.match(r"^[a-z]:/", key)):
            raise InputError("Code resource key must be a runner-resolved absolute path.")
        access = text(item.get("access"), "resource.access")
        if access not in {"read", "write"}:
            raise InputError("Resource access must be read or write.")
        result.append({"kind": kind, "host": host, "key": key, "access": access})
    return result


def overlaps(left: dict[str, str], right: dict[str, str]) -> bool:
    if left["host"] != right["host"] or left["kind"] != right["kind"]:
        return False
    if left["access"] == right["access"] == "read":
        return False
    a, b = left["key"], right["key"]
    return a == b or a.startswith(b.rstrip("/") + "/") or b.startswith(a.rstrip("/") + "/")


def base(packet: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    if packet.get("schema_version") != 1 or isinstance(packet.get("schema_version"), bool):
        raise InputError("Unsupported schema_version; expected integer 1.")
    for field in ("project_ref", "task_ref", "next_action"):
        text(packet.get(field), field)
    execution = obj(packet.get("execution"), "execution")
    text(execution.get("id"), "execution.id")
    if execution.get("ownership") not in {"confirmed", "uncertain", "released"}:
        raise InputError("execution.ownership is required and must be recognized.")
    source = obj(packet.get("source"), "source")
    ref(source.get("candidate_ref"), "source.candidate_ref")
    text(source.get("evidence_ref"), "source.evidence_ref")
    stamp(source.get("observed_at"), "source.observed_at")
    return execution, source


def preflight(packet: dict[str, Any], peers: dict[str, Any] | None) -> list[dict[str, str]]:
    execution, _ = base(packet)
    found = []
    mutation = flag(execution.get("mutation_requested"), "execution.mutation_requested")
    own_resources = resources(packet.get("resources"))
    if not mutation and any(r["access"] == "write" for r in own_resources):
        found.append(finding("READ_ONLY_WRITE_CLAIM", "Read-only execution declares write resources."))
    if mutation:
        if execution["ownership"] != "confirmed":
            found.append(finding("OWNERSHIP_UNCERTAIN", "Shared/candidate mutations require confirmed ownership."))
        if not evidence(execution.get("authorization_ref")):
            found.append(finding("AUTHORIZATION_POINTER_MISSING", "Locate the current authorization before mutation."))
        if not any(r["access"] == "write" for r in own_resources):
            found.append(finding("RESOURCE_SCOPE_MISSING", "Declare and inspect the actual resources affected."))
    if peers is None:
        found.append(finding("PEER_INVENTORY_UNKNOWN", "No current scoped peer/resource inventory was supplied."))
        return found
    stamp(peers.get("observed_at"), "peers.observed_at")
    if peers.get("complete") is not True or not evidence(peers.get("evidence_ref")):
        found.append(finding("PEER_INVENTORY_UNKNOWN", "Peer inventory is partial or lacks its observation pointer."))
    text(peers.get("scope_ref"), "peers.scope_ref")
    seen = {execution["id"]}
    for entry in items(peers.get("executions"), "peers.executions"):
        peer = obj(entry, "peer")
        peer_exec = obj(peer.get("execution"), "peer.execution")
        peer_id = text(peer_exec.get("id"), "peer.execution.id")
        if peer_id in seen:
            found.append(finding("DUPLICATE_EXECUTION_ID", "A peer reuses an execution ID; do not infer claimant identity."))
        seen.add(peer_id)
        claims = resources(peer.get("resources"))
        state = peer_exec.get("ownership")
        if state == "released" and evidence(peer_exec.get("release_ref")):
            continue
        if state != "confirmed":
            found.append(finding("PEER_OWNERSHIP_UNCERTAIN", "A peer has uncertain ownership or an unproven release."))
        for left in own_resources:
            for right in claims:
                if overlaps(left, right):
                    found.append(finding("RESOURCE_CONFLICT", f"Overlapping {left['kind']} resource with peer {peer_id}."))
    return found


def delivery(packet: dict[str, Any]) -> list[dict[str, str]]:
    execution, source = base(packet)
    candidate = source["candidate_ref"]
    found = []
    required = items(packet.get("required_checks"), "required_checks")
    for name in required:
        text(name, "required_check")
    if len(set(required)) != len(required):
        raise InputError("Duplicate required check names.")
    if not required and not evidence(packet.get("no_checks_reason")):
        found.append(finding("REQUIRED_CHECKS_UNDECLARED", "Declare required checks or an explicit not-required reason."))
    checks = {}
    for raw in items(packet.get("checks", []), "checks"):
        check = obj(raw, "check")
        name = text(check.get("name"), "check.name")
        if name in checks:
            raise InputError("Duplicate check results; reconcile reruns before checking delivery.")
        checks[name] = check
    for name in required:
        check = checks.get(name, {})
        if check.get("status") != "passed":
            found.append(finding("CHECK_PENDING_OR_FAILED", f"Required check {name} has no passing result."))
        elif check.get("candidate_ref") != candidate:
            found.append(finding("CHECK_STALE", f"Required check {name} covers different source."))
        elif not evidence(check.get("evidence_ref")) or not evidence(check.get("environment_ref")):
            found.append(finding("CHECK_EVIDENCE_MISSING", f"Required check {name} lacks evidence/environment pointers."))
    review = obj(packet.get("review"), "review")
    required_review = flag(review.get("required"), "review.required")
    if required_review or review.get("status") == "passed":
        writers = items(review.get("writer_execution_ids", [execution["id"]]), "review.writer_execution_ids")
        if review.get("status") != "passed":
            found.append(finding("REVIEW_PENDING", "Required independent technical review has not passed."))
        elif review.get("candidate_ref") != candidate:
            found.append(finding("REVIEW_STALE", "Review covers different candidate content."))
        elif (not evidence(review.get("reviewer_execution_id")) or review.get("reviewer_execution_id") in writers
              or review.get("reviewer_execution_id") == execution["id"] or review.get("candidate_edited") is not False):
            found.append(finding("REVIEW_NOT_INDEPENDENT", "Declared reviewer is a writer or modified the candidate."))
        elif not evidence(review.get("evidence_ref")):
            found.append(finding("REVIEW_EVIDENCE_MISSING", "Review result lacks an evidence pointer."))
    approval = obj(packet.get("platform_approval", {"required": False}), "platform_approval")
    if flag(approval.get("required"), "platform_approval.required"):
        if approval.get("status") != "approved":
            found.append(finding("PLATFORM_APPROVAL_PENDING", "Required platform approval is not established."))
        elif not evidence(approval.get("author_actor")) or not evidence(approval.get("approval_actor")):
            found.append(finding("PLATFORM_IDENTITY_UNKNOWN", "Platform author/approver identities are missing."))
        elif approval["author_actor"].casefold() == approval["approval_actor"].casefold():
            found.append(finding("SAME_ACCOUNT_APPROVAL", "Multiple agents sharing the author's account are not independent platform approvers."))
        elif approval.get("candidate_ref") != candidate or not evidence(approval.get("evidence_ref")):
            found.append(finding("PLATFORM_APPROVAL_STALE", "Platform approval lacks current candidate evidence."))
    deploy = obj(packet.get("deployment", {"state": "not_attempted"}), "deployment")
    if deploy.get("state") not in {"not_attempted", "unknown", "applied", "verified", "rolled_back"}:
        raise InputError("Unrecognized deployment state.")
    if deploy["state"] in {"unknown", "applied"}:
        found.append(finding("DEPLOYMENT_UNVERIFIED", "Deployment outcome or its required postconditions remain unverified."))
    if deploy["state"] == "verified":
        artifact = ref(deploy.get("artifact_ref"), "deployment.artifact_ref")
        stamp(deploy.get("observed_at"), "deployment.observed_at")
        if deploy.get("source_ref") != candidate or deploy.get("running_artifact_ref") != artifact:
            found.append(finding("DEPLOYMENT_DRIFT", "Verified deployment does not match supplied source/artifact mapping."))
        if not evidence(deploy.get("target")) or not evidence(deploy.get("evidence_ref")):
            found.append(finding("DEPLOYMENT_EVIDENCE_MISSING", "Verified deployment lacks a target/evidence pointer."))
    sync = items(packet.get("sync_targets"), "sync_targets")
    if not sync:
        found.append(finding("SYNC_TARGETS_UNDECLARED", "Declare the canonical task/handoff destinations for this packet."))
    names = set()
    for raw in sync:
        target = obj(raw, "sync_target")
        name = text(target.get("id"), "sync_target.id")
        if name in names:
            raise InputError("Duplicate synchronization targets.")
        names.add(name)
        if target.get("status") != "confirmed":
            found.append(finding("RECORD_SYNC_PENDING", f"Record synchronization remains unconfirmed for {name}."))
        elif target.get("candidate_ref") != candidate or not evidence(target.get("evidence_ref")):
            found.append(finding("SYNC_STALE", f"Record synchronization for {name} lacks current candidate evidence."))
    return found


def integration(packet: dict[str, Any]) -> list[dict[str, str]]:
    found = delivery(packet)
    source = packet["source"]["candidate_ref"]
    data = obj(packet.get("integration"), "integration")
    target = ref(data.get("target_ref"), "integration.target_ref")
    current = items(data.get("candidate_refs"), "integration.candidate_refs")
    tested = items(data.get("tested_candidate_refs"), "integration.tested_candidate_refs")
    if not current or len(set(current)) != len(current):
        raise InputError("Integration candidate refs must be non-empty and unique.")
    for value in current + tested:
        ref(value, "integration candidate ref")
    if data.get("status") != "passed":
        found.append(finding("INTEGRATION_PENDING", "Actual combination has no passing integration result."))
    if data.get("tested_target_ref") != target or current != tested or source not in current:
        found.append(finding("INTEGRATION_STALE", "Target or ordered candidate set differs from the tested combination."))
    if not evidence(data.get("evidence_ref")) or not evidence(data.get("environment_ref")):
        found.append(finding("INTEGRATION_EVIDENCE_MISSING", "Combination test lacks evidence/environment pointers."))
    ref(data.get("result_ref"), "integration.result_ref")
    for raw in items(packet.get("dependencies", []), "dependencies"):
        dep = obj(raw, "dependency")
        text(dep.get("task_ref"), "dependency.task_ref")
        required_ref = ref(dep.get("required_ref"), "dependency.required_ref")
        if dep.get("status") != "fulfilled" or dep.get("observed_ref") != required_ref or not evidence(dep.get("evidence_ref")):
            found.append(finding("DEPENDENCY_UNSATISFIED", "A required version-bound dependency is not fulfilled; task closure alone is insufficient."))
    return found


def run(operation: str, packet: dict[str, Any], peers: dict[str, Any] | None = None) -> dict[str, Any]:
    execution, source = base(packet)
    if operation == "resume":
        found = []
    elif operation == "preflight":
        found = preflight(packet, peers)
    elif operation == "deliver":
        found = delivery(packet)
    elif operation == "integrate":
        found = integration(packet)
    else:
        raise InputError("Unknown operation.")
    return {
        "operation": operation,
        "status": "SNAPSHOT_ONLY" if operation == "resume" else ("ATTENTION_NEEDED" if found else "CHECKS_CLEAR"),
        "snapshot": {"project_ref": packet["project_ref"], "task_ref": packet["task_ref"],
                     "execution_id": execution["id"], "ownership": execution["ownership"],
                     "candidate_ref": source["candidate_ref"], "observed_at": source["observed_at"],
                     "next_action": packet["next_action"]},
        "findings": found, "limits": LIMITS,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("operation", choices=["resume", "preflight", "deliver", "integrate"])
    parser.add_argument("packet", type=Path)
    parser.add_argument("--peers", type=Path, help="Scoped peer inventory; only for preflight.")
    args = parser.parse_args()
    try:
        if args.peers is not None and args.operation != "preflight":
            raise InputError("--peers is only supported by preflight.")
        result = run(args.operation, load_json(args.packet), load_json(args.peers) if args.peers else None)
    except (InputError, TypeError, KeyError) as exc:
        # Never echo arbitrary invalid input, commands, credentials or file content.
        detail = str(exc) if isinstance(exc, InputError) else "Malformed nested snapshot structure."
        print(json.dumps({"status": "INPUT_ERROR", "detail": detail, "limits": LIMITS}, ensure_ascii=False))
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if result["findings"] else 0


if __name__ == "__main__":
    sys.exit(main())
