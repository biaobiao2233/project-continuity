# Reusable Project Workflows

## Continue an existing project

1. Read Project Spine/Handoff Card.
2. Resolve routing: explicit current task → valid Pin → bound Node → project focus/Registry → fresh unpinned default.
3. Verify claimant continuity before reusing an old Logical Session Key.
4. Read the bound Node contract and relevant predecessor Closure.
5. Recheck current repo/live state and overlapping write ownership.
6. Perform the real next action; do not ask the user to repeat information already present in continuity files.

## Classify a new finding

- Current-task finding → current cycle.
- Temporary Blocker → current Node.
- Independent Issue → separate triage.

## Parallel-session conflict check

1. Identify this session's valid Pin/key and bound Node.
2. Read the live Registry if the project uses one.
3. Compare active write scopes.
4. Overlap → serialize unless physically isolated.
5. Central/shared files → read immediately before narrow patch.
6. Ownership/claimant uncertainty → `OWNERSHIP_UNCERTAIN`, read-only.

## Implement a bounded change

1. Read continuity contract and project coding instructions.
2. Inspect repo/status/diff/current code.
3. Make the smallest coherent in-scope change.
4. Run focused checks and useful regressions.
5. Inspect final diff/status.
6. Produce a Candidate/Worker Claim if formal review is required.
7. Do not mark PASS while a required independent gate is pending.

## Independent review

1. Start from the current Work Node contract, not implementer prose.
2. Inspect current actual diff/artifact.
3. Reproduce relevant checks independently.
4. Check scope, invariants and regressions.
5. Return the contract's verdict vocabulary with evidence.
6. Do not modify the candidate during a read-only review.

## Multi-agent orchestration

Prefer bounded stages:

`Implementer → Primary readback → Independent Reviewer/Verifier → Primary acceptance`

Delegation contract should include Objective, Owned/Out-of-Scope, Invariants, Acceptance Criteria, sources, allowed writes and expected completion packet.

## Pause / handoff

A new session appearing does not transfer ownership. Full handoff requires old owner release/transfer + receiver re-read/accept.

Before ending a meaningful session, update current state/next action and compact evidence; avoid copying whole logs/prompts.

## Close a Work Node

Close only after required gates pass and Primary acceptance is established. Write compact Closure Memory and move the Project Spine to the next actual state.

