# Project Continuity and Governance

## Authority model
1. Current explicit user intent and authorization.
2. Independently verified Accepted Project State.
3. Current repository/files/live reproducible evidence.
4. Worker claim/executor report.
5. Agent summary/inference.
6. Historical memory clue/index.

Never promote a lower-authority statement into accepted fact without verification.

## Fast receiver order
1. Read canonical Handoff / Fast Resume.
2. Identify active Issue/PR/Work Node and Next Action.
3. Read only its current contract/latest evidence.
4. Recheck only repo/live facts that could invalidate the Next Action.
5. Execute through the next real gate.

## Session identity and ownership
- Fresh/cold conversation gets a fresh claimant identity unless continuity is independently established.
- Old prompts, copied Session Keys, or seeing a registry row do not prove claimant identity.
- Ambiguous/duplicate claimants enter `OWNERSHIP_UNCERTAIN`: reads allowed, shared/candidate writes blocked.
- Full takeover requires explicit release/transfer or a canonical handoff that permits fresh coordinator takeover, plus receiver re-read.

## Write isolation
- Declare the smallest writable scope.
- Overlapping writes serialize unless physically isolated and semantically non-overlapping.
- Concurrent code tasks use separate branches/worktrees.
- Central coordination surfaces are single-writer by default.
- Reviewer/Verifier remains candidate-read-only during independent review.

## State semantics
Keep `NOT_STARTED`, `IN_PROGRESS`, `CANDIDATE`, `PASS`, `FAIL`, `BLOCKED`, and `SUPERSEDED` distinct.

`Worker COMPLETE` does not mean `PASS`.

## Work Node discipline
A Work Node is a bounded execution/review/verification unit, not a chat, date, Issue, PR, or file. Preserve only what execution continuity needs: Objective, Owned Scope, Out of Scope, Acceptance Criteria, Protected Invariants, Dependencies, blocker/Next Action, canonical tracker links.

Do not duplicate a complete GitHub Issue contract locally when the Issue is already canonical.

## Handoff writes
Write only high-signal current material: Fast Resume header, objective/gate/active item, blockers/invariants, accepted facts, tracker references, exact Next Action. Do not paste full prompts, giant logs, code, diffs, external docs, or secrets.
