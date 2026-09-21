# Minimal continuity and evidence

## Three independent questions

**Authorization:** what may this execution do, to which scope and target, under which user/repository policy?

**Observation:** which source/artifact/config/process is actually present now, with what evidence and timestamp?

**Acceptance:** which exact candidate and environment passed which required checks and received which decision?

Never rank an old accepted record above contrary current observations as if acceptance could change physical reality. Never let a current deployment retroactively accept its source. Preserve all three and report drift.

## Bounded recovery

Read the stable project entry → pinned task/PR → current source and required environment → needed evidence/next action. Consult predecessor closure and EverOS only for a specific missing fact. Do not read entire historical worklogs as a default startup cost.

Current explicit task/switch outranks a continuing pin; a project-level focus change alone does not. A fresh unpinned execution follows current project focus only after checking the actual task state.

## Execution identity and takeover

Use a new execution ID for a new conversation. Reuse runtime-provided session mechanisms rather than creating another runner/inbox system. Record a minimal logical ID only when needed; private ChatGPT thread IDs are not required.

A task, direction, branch or path is not a claimant identity. A copied ID, inactivity, timeout, disconnected connector or old handoff is not proof of release.

Normal takeover: old owner explicitly releases/transfers the scope → receiver re-reads current task/source/resources → receiver acknowledges the new bounded ownership using a new execution identity. Preserve predecessor identity in history.

If the owner cannot respond, only a currently authorized user/coordinator may reassign the scope. First confirm/fence the old write path using actual runtime controls or real isolated resources. Do not invent leases, automatic timeout takeovers or fencing tokens the backend cannot enforce. An ownership flag written into JSON is not a lock.

When claimant or shared ownership is uncertain, keep shared/candidate writes read-only. Continue isolated read-only investigation where safe. A clean new sandbox does not grant production authority.

## Shared records

Keep one chosen live coordination source. Central fields have one writer or explicit non-overlapping delegation. Before audit-relevant non-owner central writes, persist grantor, grantee, exact fields, purpose, and expiry/return condition; temporary delegation is not ownership transfer.

Read immediately before a narrow SHA/context-guarded write. On drift, re-read and reconcile; do not weaken match guards or overwrite from an old snapshot. Preserve unrelated uncommitted changes and pending jobs.

## Handoff contents

Reference the canonical task/PR, exact candidate, current executor/transfer, required checks and their evidence, relevant environment/rollback, unresolved blockers, pending synchronization, and next action. Keep the full requirements in the canonical task.

Use the repository for architecture, interfaces and durable invariants. Use an existing runtime/session ledger for execution coordination where possible. Treat any locally generated dashboard as a timestamped projection, never a second authoritative registry.

Prefer README as a stable entry/index; when a project already relies on a current-state card, update that single entry at delivery or report the pending sync. Merely adding a worklog is not a reason to claim the entry is current.

## Partial completion

Distinguish NOT_ATTEMPTED, UNKNOWN outcome, observed success/failure, and pending record sync at the relevant step; do not create a new universal task-state taxonomy. Reconcile unknown operations by readback before retry. If source/deployment succeeded but record sync failed, keep both truths and retry only the unconfirmed synchronization.

Record acceptance only for the exact candidate/environment and required decisions. Preserve worker claim, reviewer evidence and Primary acceptance separately; do not turn an optional local checker result into project PASS.

Mark obsolete accepted conclusions SUPERSEDED with a reason and replacement pointer instead of rewriting their historical content.
