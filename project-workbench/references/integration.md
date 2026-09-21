# Continuous integration and controlled rollout

## Default integration path

Use short-lived task branches from the current integration baseline. Deliver a compatible slice and integrate it early; do not wait for an entire direction to finish. Use a temporary integration candidate only for changes that truly must be tested together. Keep a pinned manifest for a multi-repository delivery.

Record the tested target ref, ordered candidate refs, and resulting integration ref/artifact. Target/head changes require affected checks again; update dependency consumers if the contract changed. A merge without textual conflicts is not a semantic compatibility test.

An integrator owns coordination and verification, not unrestricted product repair. Send substantial conflicts back to their owning task or obtain a scope change. Do not merge a candidate that lacks required technical review or platform approval.

## Three isolation surfaces

1. Code: distinct runner-resolved worktree/checkout paths; preserve shared refs/config and lockfiles. Git branches alone do not isolate the same working directory.
2. Runtime: separate test ports, database/schema, container/project names, output paths and mutable caches when necessary. Account for shared resource limits.
3. Live target: serialize overlapping mutations on the same device/service/security boundary even if source worktrees differ. Declare a common resource key such as `device/athena/network`, not only a service-local file name.

Use actual backend ownership/concurrency controls where available. A JSON claim, a reviewer label, a Git worktree lock or a GitHub Actions concurrency group is not a universal production lock. If paths can bypass the chosen writer, coordinate/fence those paths or keep live mutations blocked. Never infer exclusivity solely from an empty stale registry.

## Release evidence

Before an authorized rollout, verify candidate identity, build provenance, target, rollback material, operation scope, current owner and the postconditions to test. Afterward read back the running artifact/config and exercise the task's user-facing behavior.

Keep source accepted/merged, staging accepted and production released distinct. A listening port or completed TLS handshake establishes only that narrow condition, not login, app functionality, throughput, long-term stability or cold-boot persistence.

For firmware/network work, do not reboot, flush rules, restart unrelated services, or enable an old owner to satisfy a generic test plan. An explicit approved rollback is a separate bounded action, not permission to restore arbitrary backups.

## Failure and interruption

Record the last confirmed step and unknown outcomes. Read back before retrying an operation that may already have changed state. On failed postconditions follow the authorized rollback contract. Record rollback success only after verification.

If deployment is healthy and only reporting failed, retain `RECORD_SYNC_PENDING`; do not roll back healthy production merely to synchronize a document. The pending record must name its target and reconciliation action without duplicating all tracker contents.

## Integration receipt

Keep task/PR refs, exact source/artifact refs, target baseline, contract version, required check/review links, actual deployment target/observation time, rollback pointer, pending-sync targets and next action. Omit deployment fields for a code-only task. The optional local checker validates supplied structure, not those remote facts.
