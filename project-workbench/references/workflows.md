# Reusable Project Workflows

## Continue an existing project

1. Read Project Spine/Handoff Card.
2. Resolve routing in this order: explicit current task/switch → existing valid Session Pin → bound Work Node state/ownership → Project Primary Focus/Registry → fresh unpinned-session default.
3. If an old logical Session Key is being reused, verify claimant continuity; fresh/cold or ambiguous claimant must not inherit the existing row/write scope. Use a new key or fail closed to `OWNERSHIP_UNCERTAIN` / read-only until resolved.
4. Read the bound Node contract and relevant predecessor Closure.
5. Recheck current repo/live state and overlapping write ownership where it can change.
6. State the real current state and perform the Node's next action; do not ask the user to repeat information already present in the continuity files.

## Classify a new finding

Before changing scope, classify the finding:

- **Current-task finding** → keep in current implementation/review/repair cycle.
- **Temporary Blocker** → record on current Node and continue when unblocked.
- **Independent Issue** → record with symptom/evidence/affected state/impact, then triage separately.

If a Blocker exposes a durable underlying defect, keep the immediate Blocker and create/link an Issue for the durable defect.


## Parallel-session conflict check

Before substantial shared writes when multiple sessions/agents may be active:

1. Identify this session's valid Pin/key and bound Node.
2. Check the single live Registry if the project uses one; verify claimant/ownership evidence rather than trusting a copied prompt or stale row.
3. Compare active write scopes. Overlap means serialize unless there is real physical isolation.
4. For central/shared files, read immediately before writing and use the narrowest patch possible. Context mismatch means stop, re-read, and merge; never replace from a stale whole-file snapshot.
5. If ownership or claimant identity cannot be proven, enter `OWNERSHIP_UNCERTAIN`: inspect/read is allowed, shared/candidate writes are not.
6. A Project Primary Focus change is a project-level coordination signal, not a command to reroute a still-valid Session Pin.

## Implement a bounded change

1. Read continuity contract and project coding instructions.
2. Inspect repo/status/diff/current code.
3. Make the smallest coherent change inside Owned Scope.
4. Run focused checks, then useful regression checks.
5. Inspect final diff/status.
6. Produce a Worker Claim / Candidate Change Packet when the change is material enough to require review.
7. Do not mark the Node PASS if independent review/verification is still required.

## Independent review

1. Start from the current Work Node contract, not the implementer's summary.
2. Inspect the current actual diff/artifact and workspace hygiene.
3. Reproduce relevant checks/findings independently.
4. Check scope, protected invariants, regressions, and the exact reviewer contract.
5. Return the contract's verdict vocabulary (for example `PASS_FOR_<NODE>` / `REPAIR_FIRST` / `FAIL`) with evidence by severity.
6. Do not modify the candidate or accepted state during a read-only review.

## Verify a gate

Use a separate verifier context when independence matters. Verify concrete postconditions such as exact revision, clean tree, test results, listener/process ownership, staging cleanup, release pointer, rollback, and production invariants. Return PASS/FAIL/BLOCKED only after the required observable checks ran.

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
- Source pointers
- Allowed write/read behavior
- Expected completion packet/verdict

Require the receiver to inspect the current files/repo rather than depend on the delegator's summary. Separate role/context is more important for review independence than merely changing permissions.

## Pause / handoff

A new session appearing does not transfer ownership. For full handoff, the old owner explicitly releases/transfers the relevant scope and the receiving session re-reads current state and accepts it; otherwise the new session is only a peer/helper/reviewer with its bounded scope.

Before ending a meaningful session:

- update current Node status and next action
- record compact Worker/Reviewer/Verifier evidence
- update Handoff Card if current state changed
- record new requirements/invariants/issues only if actually established
- avoid copying full logs/prompts

A clean handoff should let a fresh agent safely start the next step without re-reading the entire conversation.

## Close a Work Node

Close only after all required acceptance gates pass and Primary acceptance is established. Write Closure Memory with accepted outcome, durable capabilities, inherited requirements, invariants, verification evidence, remaining risks, and what future agents may/may not assume. Then move the Project Spine to the next actual Node.
