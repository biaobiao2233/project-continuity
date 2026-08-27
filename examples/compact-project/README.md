# Example App — Compact Project Spine

## Handoff Card
- Current goal: Add export-to-JSON to the example app.
- Current state: Basic export function implemented; tests pending.
- Verification state: CANDIDATE, not PASS.
- Next action: Run focused export tests and inspect final diff.
- Blockers: none.
- Protected invariants: existing CSV export must remain unchanged; no production deployment.
- last_verified_at: 2026-08-27

## Current Resume Point
- Last completed action: Added `exportJson()` implementation.
- Current physical state: source modified, no commit yet.
- Last verification: typecheck passed; export tests not run.
- In-flight issue: JSON escaping not independently tested.
- Safe next action: run export-focused tests.
- Do NOT repeat: do not rewrite CSV exporter.

## Current Requirements

1. Add JSON export.
2. Keep CSV export compatible.
3. No deployment in this task.

## Protected Invariants

- Do not change public CSV format.
- Do not commit secrets or sample customer data.

## Active Work Node
- Objective: implement and verify JSON export.
- Owned scope: export module + export tests.
- Out of scope: UI redesign, deployment.
- Acceptance criteria: focused tests pass; CSV regression passes; final diff stays in scope.
- Status: CANDIDATE.

## Verification Evidence

- typecheck: PASS
- JSON tests: pending
- CSV regression: pending

## Closure Memory

> Fill only after the node is accepted.

## Sources / Related Docs

- `src/export.*`
- `test/export.*`

