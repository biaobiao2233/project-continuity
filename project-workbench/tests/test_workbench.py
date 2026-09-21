from __future__ import annotations

from copy import deepcopy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("workbench", ROOT / "scripts/workbench.py")
wb = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(wb)
A, B, C = "a" * 40, "b" * 40, "c" * 40
STAMP = "2026-09-21T06:00:00+00:00"


def packet():
    return {
        "schema_version": 1, "project_ref": "example/project", "task_ref": "example/project#17",
        "lane": "runtime", "execution": {"id": "run-new", "ownership": "confirmed", "mutation_requested": True,
                                            "authorization_ref": "fixture:current-user-scope"},
        "source": {"candidate_ref": A, "evidence_ref": "fixture:source-readback", "observed_at": STAMP},
        "resources": [{"kind": "code", "host": "sandbox", "key": "/tmp/task-17", "access": "write"}],
        "required_checks": ["unit"],
        "checks": [{"name": "unit", "status": "passed", "candidate_ref": A,
                    "evidence_ref": "fixture:test-log", "environment_ref": "fixture:isolated-python"}],
        "review": {"required": False}, "platform_approval": {"required": False},
        "deployment": {"state": "not_attempted"},
        "sync_targets": [{"id": "canonical-task", "status": "confirmed", "candidate_ref": A,
                          "evidence_ref": "fixture:task-readback"},
                         {"id": "handoff-entry", "status": "confirmed", "candidate_ref": A,
                          "evidence_ref": "fixture:entry-readback"}],
        "next_action": "Perform the separately authorized receiver pilot."
    }


def peers(*executions):
    return {"complete": True, "observed_at": STAMP, "scope_ref": "fixture:shared-host-and-targets",
            "evidence_ref": "fixture:inventory-readback", "executions": list(executions)}


def peer(kind="code", key="/tmp/task-18", host="sandbox", access="write", ownership="confirmed"):
    return {"execution": {"id": "run-peer", "ownership": ownership},
            "resources": [{"kind": kind, "key": key, "host": host, "access": access}]}


def codes(result):
    return {x["code"] for x in result["findings"]}


def reviewed(p):
    p["review"] = {"required": True, "status": "passed", "candidate_ref": A,
                   "reviewer_execution_id": "review-only", "candidate_edited": False,
                   "writer_execution_ids": ["run-new"], "evidence_ref": "fixture:review"}
    return p


def integrated(p):
    p["integration"] = {"target_ref": B, "tested_target_ref": B, "candidate_refs": [A],
                        "tested_candidate_refs": [A], "result_ref": C, "status": "passed",
                        "evidence_ref": "fixture:combined-tests", "environment_ref": "fixture:integration-tree"}
    return p


class PacketTests(unittest.TestCase):
    def test_resume_is_snapshot_not_acceptance(self):
        result = wb.run("resume", packet())
        self.assertEqual(result["status"], "SNAPSHOT_ONLY")
        self.assertIn("No GitHub/live queries", result["limits"])

    def test_valid_delivery_is_not_project_pass(self):
        self.assertEqual(wb.run("deliver", packet())["status"], "CHECKS_CLEAR")

    def test_uncertain_owner_blocks_mutation(self):
        p = packet(); p["execution"]["ownership"] = "uncertain"
        self.assertIn("OWNERSHIP_UNCERTAIN", codes(wb.run("preflight", p, peers())))

    def test_released_owner_cannot_mutate(self):
        p = packet(); p["execution"]["ownership"] = "released"
        self.assertIn("OWNERSHIP_UNCERTAIN", codes(wb.run("preflight", p, peers())))

    def test_authorization_pointer_needed(self):
        p = packet(); del p["execution"]["authorization_ref"]
        self.assertIn("AUTHORIZATION_POINTER_MISSING", codes(wb.run("preflight", p, peers())))

    def test_fresh_identity_cannot_reuse_peer_id(self):
        p = packet(); other = peer(); other["execution"]["id"] = "run-new"
        self.assertIn("DUPLICATE_EXECUTION_ID", codes(wb.run("preflight", p, peers(other))))

    def test_distinct_worktrees_do_not_conflict(self):
        self.assertEqual(wb.run("preflight", packet(), peers(peer()))["status"], "CHECKS_CLEAR")

    def test_parent_worktree_write_conflicts(self):
        other = peer(key="/tmp/task-17/subdir")
        self.assertIn("RESOURCE_CONFLICT", codes(wb.run("preflight", packet(), peers(other))))

    def test_adjacent_path_is_not_parent(self):
        self.assertNotIn("RESOURCE_CONFLICT", codes(wb.run("preflight", packet(), peers(peer(key="/tmp/task-170")))))

    def test_windows_case_and_slash_normalization(self):
        p = packet(); p["resources"][0]["key"] = "D:\\Example\\Task"
        self.assertIn("RESOURCE_CONFLICT", codes(wb.run("preflight", p, peers(peer(key="d:/example/task/src")))))

    def test_runtime_port_conflicts_even_with_other_worktree(self):
        p = packet(); p["resources"].append({"kind": "runtime", "host": "sandbox", "key": "port/tcp/8080", "access": "write"})
        self.assertIn("RESOURCE_CONFLICT", codes(wb.run("preflight", p, peers(peer("runtime", "port/tcp/8080")))))

    def test_same_router_serializes_different_service_tasks(self):
        p = packet(); p["resources"].append({"kind": "production", "host": "device-host", "key": "device/athena/network", "access": "write"})
        other = peer("production", "device/athena/network/dns", "device-host")
        self.assertIn("RESOURCE_CONFLICT", codes(wb.run("preflight", p, peers(other))))

    def test_missing_peer_inventory_is_not_empty_inventory(self):
        self.assertIn("PEER_INVENTORY_UNKNOWN", codes(wb.run("preflight", packet())))

    def test_partial_peer_inventory_is_not_complete(self):
        inv = peers(); inv["complete"] = False
        self.assertIn("PEER_INVENTORY_UNKNOWN", codes(wb.run("preflight", packet(), inv)))

    def test_unproven_release_is_not_resource_freedom(self):
        self.assertIn("PEER_OWNERSHIP_UNCERTAIN", codes(wb.run("preflight", packet(), peers(peer(ownership="released")))))

    def test_proven_declared_release_no_collision(self):
        other = peer(key="/tmp/task-17", ownership="released"); other["execution"]["release_ref"] = "fixture:release"
        self.assertEqual(wb.run("preflight", packet(), peers(other))["status"], "CHECKS_CLEAR")

    def test_read_only_investigation_does_not_require_write_grant(self):
        p = packet(); p["execution"].update(ownership="uncertain", mutation_requested=False)
        p["resources"][0]["access"] = "read"
        self.assertNotIn("OWNERSHIP_UNCERTAIN", codes(wb.run("preflight", p, peers())))

    def test_read_only_cannot_hide_write_claim(self):
        p = packet(); p["execution"]["mutation_requested"] = False
        self.assertIn("READ_ONLY_WRITE_CLAIM", codes(wb.run("preflight", p, peers())))

    def test_candidate_drift_invalidates_check(self):
        p = packet(); p["source"]["candidate_ref"] = B
        self.assertIn("CHECK_STALE", codes(wb.run("deliver", p)))

    def test_zero_declared_checks_need_reason(self):
        p = packet(); p["required_checks"] = []
        self.assertIn("REQUIRED_CHECKS_UNDECLARED", codes(wb.run("deliver", p)))

    def test_required_check_missing(self):
        p = packet(); p["checks"] = []
        self.assertIn("CHECK_PENDING_OR_FAILED", codes(wb.run("deliver", p)))

    def test_check_environment_missing(self):
        p = packet(); del p["checks"][0]["environment_ref"]
        self.assertIn("CHECK_EVIDENCE_MISSING", codes(wb.run("deliver", p)))

    def test_required_independent_review_pending(self):
        p = packet(); p["review"]["required"] = True
        self.assertIn("REVIEW_PENDING", codes(wb.run("deliver", p)))

    def test_required_review_is_candidate_bound(self):
        p = reviewed(packet()); p["review"]["candidate_ref"] = B
        self.assertIn("REVIEW_STALE", codes(wb.run("deliver", p)))

    def test_reviewer_modified_candidate(self):
        p = reviewed(packet()); p["review"]["candidate_edited"] = True
        self.assertIn("REVIEW_NOT_INDEPENDENT", codes(wb.run("deliver", p)))

    def test_reviewer_was_a_writer(self):
        p = reviewed(packet()); p["review"]["writer_execution_ids"].append("review-only")
        self.assertIn("REVIEW_NOT_INDEPENDENT", codes(wb.run("deliver", p)))

    def test_same_github_account_cannot_be_two_approvers(self):
        p = packet(); p["platform_approval"] = {"required": True, "status": "approved", "author_actor": "Owner",
                                               "approval_actor": "owner", "candidate_ref": A, "evidence_ref": "fixture:approval"}
        self.assertIn("SAME_ACCOUNT_APPROVAL", codes(wb.run("deliver", p)))

    def test_deployment_drift_does_not_become_accepted(self):
        p = packet(); p["deployment"] = {"state": "verified", "source_ref": B, "artifact_ref": "sha256:" + "d"*64,
                                         "running_artifact_ref": "sha256:" + "e"*64, "observed_at": STAMP,
                                         "target": "fixture:staging", "evidence_ref": "fixture:readback"}
        self.assertIn("DEPLOYMENT_DRIFT", codes(wb.run("deliver", p)))

    def test_verified_deployment_and_sync_pending_coexist(self):
        p = packet(); p["deployment"] = {"state": "verified", "source_ref": A, "artifact_ref": "sha256:" + "d"*64,
                                         "running_artifact_ref": "sha256:" + "d"*64, "observed_at": STAMP,
                                         "target": "fixture:staging", "evidence_ref": "fixture:readback"}
        p["sync_targets"][1]["status"] = "pending"
        before = deepcopy(p)
        result = wb.run("deliver", p)
        self.assertEqual(codes(result), {"RECORD_SYNC_PENDING"})
        self.assertEqual(p, before)
        self.assertEqual(p["deployment"]["state"], "verified")

    def test_reconciled_sync_can_be_rechecked_without_redeploy(self):
        p = packet(); p["sync_targets"][0]["status"] = "pending"
        self.assertIn("RECORD_SYNC_PENDING", codes(wb.run("deliver", p)))
        p["sync_targets"][0]["status"] = "confirmed"
        self.assertEqual(wb.run("deliver", p)["status"], "CHECKS_CLEAR")

    def test_integration_exact_combination(self):
        self.assertEqual(wb.run("integrate", integrated(packet()))["status"], "CHECKS_CLEAR")

    def test_integration_target_changed(self):
        p = integrated(packet()); p["integration"]["target_ref"] = C
        self.assertIn("INTEGRATION_STALE", codes(wb.run("integrate", p)))

    def test_integration_candidate_order_changed(self):
        p = integrated(packet()); p["integration"]["candidate_refs"] = [A, B]; p["integration"]["tested_candidate_refs"] = [B, A]
        self.assertIn("INTEGRATION_STALE", codes(wb.run("integrate", p)))

    def test_closed_dependency_not_enough(self):
        p = integrated(packet()); p["dependencies"] = [{"task_ref": "example/project#9", "required_ref": B,
                                                         "observed_ref": C, "status": "closed", "evidence_ref": "fixture:issue"}]
        self.assertIn("DEPENDENCY_UNSATISFIED", codes(wb.run("integrate", p)))

    def test_branch_alias_is_not_immutable_ref(self):
        p = packet(); p["source"]["candidate_ref"] = "main"
        with self.assertRaises(wb.InputError): wb.run("resume", p)

    def test_timestamp_needs_timezone(self):
        p = packet(); p["source"]["observed_at"] = "2026-09-21T06:00:00"
        with self.assertRaises(wb.InputError): wb.run("resume", p)

    def test_string_boolean_rejected(self):
        p = packet(); p["execution"]["mutation_requested"] = "false"
        with self.assertRaises(wb.InputError): wb.run("preflight", p, peers())

    def test_duplicate_json_fields_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            path = Path(d)/"input.json"; path.write_text('{"schema_version":1,"schema_version":2}')
            with self.assertRaises(wb.InputError): wb.load_json(path)

    def test_cli_unknown_input_never_executes_commands(self):
        with tempfile.TemporaryDirectory() as d:
            path = Path(d)/"input.json"; sentinel = Path(d)/"should-not-exist"
            p = packet(); p["command"] = "touch " + str(sentinel)
            data = json.dumps(p); path.write_text(data)
            result = subprocess.run([sys.executable, str(ROOT/"scripts/workbench.py"), "deliver", str(path)], capture_output=True, text=True, timeout=10)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertFalse(sentinel.exists()); self.assertEqual(path.read_text(), data)
            self.assertNotIn("command", json.loads(result.stdout)["snapshot"])

    def test_cli_invalid_json_returns_bounded_error(self):
        with tempfile.TemporaryDirectory() as d:
            path = Path(d)/"input.json"; path.write_text('{invalid secret-not-to-echo')
            result = subprocess.run([sys.executable, str(ROOT/"scripts/workbench.py"), "resume", str(path)], capture_output=True, text=True, timeout=10)
            self.assertEqual(result.returncode, 2)
            self.assertNotIn("secret-not-to-echo", result.stdout)
            self.assertEqual(json.loads(result.stdout)["status"], "INPUT_ERROR")

    def test_oversized_input_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            path = Path(d)/"input.json"; path.write_bytes(b" "*(wb.MAX_BYTES+1))
            with self.assertRaises(wb.InputError): wb.load_json(path)


if __name__ == "__main__":
    unittest.main()
