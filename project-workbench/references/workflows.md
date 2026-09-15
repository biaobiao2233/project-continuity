# Reusable Project Workflows

## Continue an existing project

1. Read Project Spine/Handoff Card.
2. Resolve routing in this order: explicit current task/switch → existing valid Session Pin → bound Work Node state/ownership → Project Primary Focus/Registry → fresh unpinned-session default.
3. If an old logical Session Key is being reused, verify claimant continuity; fresh/cold or ambiguous claimant must not inherit the existing row/write scope. Use a new key or fail closed to `OWNERSHIP_UNCERTAIN` / read-only until resolved.
4. Read the bound Node contract, linked canonical tracker items when relevant, and only the predecessor Closure needed for this task.
5. Recheck current repo/live state and overlapping write ownership where it can change.
6. Perform the real next action and continue through deterministic in-scope steps to the next actual gate; do not ask the user to repeat information already present or to say `继续` between routine substeps.

## Continuous execution

When Objective, scope, authorization, and next action are already established:

1. Treat safe deterministic steps as one execution chain, for example `inspect → edit → test → repair → retest → package → PR/update → verify`.
2. Batch independent reads, searches, and health/status checks when practical.
3. If a test or validator exposes an in-scope defect with an obvious safe repair, repair it and rerun the affected check instead of stopping for permission.
4. Give intermediate user updates only for a real blocker, materially changed risk/scope, new required authorization/input, or a meaningful gate the user must act on.
5. Stop before an irreversible/high-risk action not already authorized, before taking ownership that is ambiguous, or when no safe fallback exists.
6. Do not widen scope or perform optional risky work merely to avoid asking a question.

## Classify a new finding

Before changing scope, classify the finding:

- **Current-task finding** → keep it in the current implementation/review/repair cycle.
- **Temporary Blocker** → record on the current Node and continue when unblocked.
- **Independent Issue** → record in the project's canonical tracker with symptom/evidence/impact, then triage separately.

If a Blocker exposes a durable underlying defect, keep the immediate Blocker and create/link an Issue in the canonical tracker for the durable defect.

## Parallel-session conflict check

Before substantial shared writes when multiple sessions/agents may be active:

1. Identify this session's valid Pin/key and bound Node.
2. Check the live Registry if the project uses one; verify claimant/ownership evidence rather than trusting a copied prompt or stale row.
3. Compare active write scopes. Overlap means serialize unless there is real physical isolation.
4. For central/shared files, read immediately before writing and use the narrowest patch possible. Context mismatch means re-read and merge; never replace from a stale whole-file snapshot.
5. If ownership or claimant identity cannot be proven, enter `OWNERSHIP_UNCERTAIN`: inspect/read is allowed, shared/candidate writes are not.
6. A Project Primary Focus change is a project-level coordination signal, not a command to reroute a still-valid Session Pin.

## Implement a bounded change

1. Read the continuity contract, canonical GitHub Issue/PR when relevant, and project coding instructions.
2. Inspect repo/status/diff/current code.
3. Make the smallest coherent change inside Owned Scope.
4. Run focused checks, repair in-scope failures, rerun, then run useful regression checks.
5. Inspect final diff/status.
6. Update the GitHub PR/candidate evidence when GitHub is canonical, or the local Candidate Change Packet when local fallback is canonical.
7. Continue to the required review/verification gate without pausing between those routine steps.
8. Do not mark the Node PASS if independent review/verification is still required.

## GitHub-backed substantial change

Use this flow when the repository and change warrant formal GitHub tracking:

`Issue → branch/worktree → implementation/tests → PR → required checks/review → merge → release verification`

- Link Issue/PR/commit identifiers from the Work Node; do not duplicate full GitHub bodies locally.
- Keep Session Pin, ownership, live deployment state, blockers, and protected invariants in Project Continuity.
- Small low-risk changes may skip Issue and/or PR when repository policy and user intent allow it.

## Independent review

1. Start from the current Work Node contract and canonical candidate (for example the current PR), not the implementer's summary.
2. Inspect the actual current diff/artifact and workspace hygiene.
3. Reproduce relevant checks/findings independently.
4. Check scope, protected invariants, regressions, and the exact reviewer contract.
5. Return the contract's verdict vocabulary with evidence by severity.
6. Do not modify the candidate or accepted state during a read-only review.

## Verify a gate

Use a separate verifier context when independence matters. Verify concrete postconditions such as exact revision, clean tree, required test/CI status, listener/process ownership, staging cleanup, release pointer, rollback, and production invariants. Return PASS/FAIL/BLOCKED only after the required observable checks ran.

## High-impact decision / RFC-ADR

Before implementing a hard-to-reverse architecture, security boundary, permission, persistence, migration, protocol/API, deployment, or major dependency decision, consider a lightweight RFC/ADR:

`Context/Problem → Constraints → Options → Trade-offs → Decision → Consequences → Verification`.

Do not create RFC/ADR overhead for routine fixes or obvious low-risk choices.

## Multi-agent orchestration

Prefer bounded stages instead of one giant prompt:

`Implementer → Primary readback → Independent Reviewer/Verifier → Primary acceptance`.

When delegating to Codex/Antigravity/another agent, provide a compact task contract containing:

- Objective
- Owned Scope
- Out of Scope
- Protected Invariants
- Acceptance Criteria / Required Checks
- Source pointers / GitHub Issue or PR when canonical
- Allowed write/read behavior
- Expected completion packet/verdict

Require the receiver to inspect current files/repo rather than depend on the delegator's summary. Separate role/context is more important for review independence than merely changing permissions.

## Pause / handoff

A new session appearing does not transfer ownership. For full handoff, the old owner explicitly releases/transfers the relevant scope and the receiving session re-reads current state and accepts it; otherwise the new session is only a peer/helper/reviewer with its bounded scope.

Before ending a meaningful session:

- update current Node status and next action
- record compact Worker/Reviewer/Verifier evidence
- link current GitHub Issue/PR/commit when relevant
- update Handoff Card if current state changed
- record new requirements/invariants/issues only if actually established
- avoid copying full logs/prompts/GitHub discussions

A clean handoff should let a fresh agent safely start the next step without re-reading the entire conversation.

## Close a Work Node

Close only after all required acceptance gates pass and Primary acceptance is established. Write Closure Memory with accepted outcome, durable capabilities, inherited requirements, invariants, verification evidence, remaining risks, canonical tracker references, and what future agents may/may not assume. Then move the Project Spine to the next actual Node.
