# EX-02 — Migration Verification

## Node Contract
- Objective: prove the candidate migration and rollback in isolated staging.
- Owned scope: staging fixture, migration command, rollback evidence.
- Out of scope: production promotion, unrelated parser refactor.
- Acceptance criteria: migration succeeds; rollback restores exact pre-image; focused regression passes.
- Protected invariants: production untouched; pre-image preserved.
- Dependencies: EX-01 PASS.

## Current Status
- Worker status: candidate implementation complete.
- Independent verification: pending.
- Accepted status: CANDIDATE.
- Blockers: none.
- Next action: isolated staging migration + rollback.

## Current Resume Point
- Last completed action: staging fixture prepared.
- Current physical state: no migration run yet.
- Last verification: fixture hash recorded.
- In-flight issue: rollback has not been exercised.
- Safe next action: run staging migration, inspect, then rollback.
- Do NOT repeat: do not touch production.

## Independent Reviewer Contract
- Review objective: verify migration/rollback evidence independently.
- Read-only sources: candidate diff, staging logs, before/after hashes.
- Required checks: exact pre-image restore; no production change; regression tests.
- Forbidden actions: modify candidate or production.
- Required verdict: PASS_FOR_EX02 | REPAIR_FIRST | FAIL.

## Closure Memory

> Fill only after required gates and Primary acceptance.

