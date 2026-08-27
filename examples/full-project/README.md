# Example Service — Project Spine

## Handoff Card
- Current goal: Ship a safer configuration migration.
- Active node: `EX-02 — migration verification`
- Accepted predecessors: `EX-01 — migration parser` PASS.
- Current state: migration candidate exists; staging verification pending.
- Verification state: CANDIDATE.
- Resume point: `worklogs/EX-02-migration-verification.md`.
- Next action: run isolated staging migration + rollback.
- Blockers: none.
- Protected invariants: production unchanged; old config remains recoverable.
- Critical files: migration module, staging fixture, rollback script.
- Relevant Closure Memories: EX-01 Closure.
- last_verified_at: 2026-08-27

## Current Requirements

1. Existing config must remain readable.
2. Migration must be reversible.
3. Production promotion requires separate authorization.

## Protected Invariants

- Merge != production release.
- Worker COMPLETE != PASS.
- Staging rollback must be demonstrated before acceptance.

## Work Node Index

| Node | Goal | Status | Verification | File / Closure |
|---|---|---|---|---|
| EX-01 | parse old + new config | PASS | tests + review | `worklogs/EX-01-parser.md` |
| EX-02 | staging migration + rollback | CANDIDATE | pending staging gate | `worklogs/EX-02-migration-verification.md` |

## Major Discoveries

- Old config includes an undocumented optional field; parser now preserves it.

## Major Pitfalls

- Do not treat successful parse tests as proof that rollback works.

## Closure Memory Index

- EX-01: parser accepts both schemas and preserves unknown optional fields.

