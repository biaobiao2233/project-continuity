# Project Continuity Reference

## Authority model

Use this order when evidence conflicts:

1. Current explicit user intent and authorization.
2. Independently verified Accepted Project State.
3. Current repository/files/tests/live reproducible evidence.
4. Worker Claim / executor report.
5. Agent summary or inference.
6. EverOS/other derived historical memory.

Never upgrade a lower layer into a higher layer without verification.

## Receiver read order

1. Project Spine / Handoff Card.
2. Current Resume Point when work is in-flight.
3. Current Requirements / Protected Invariants.
4. Active/bound Work Node contract.
5. Relevant predecessor Closure Memory.
6. Repo/docs/live state needed for the next step.
7. Derived historical memory only when the continuity layer is insufficient.

## Multi-session routing

Use:

```text
explicit current task/switch
→ valid existing Session Pin
→ bound Work Node state/ownership
→ Project Primary Focus / Registry
→ fresh unpinned default
```

A valid Pin is not overwritten merely because another session changes project-level focus.

### Logical Session Keys

- Coordination identity, not platform/cryptographic identity.
- Single allocation / no silent reuse.
- Fresh/cold sessions default to a new key unless claimant continuity is actually proven.
- Old prompts, self-claims and visible Registry rows do not prove identity.
- Ambiguous/duplicate claimants → `OWNERSHIP_UNCERTAIN`; shared/candidate writes fail closed to read-only.
- Full takeover requires explicit release/transfer plus receiver re-read/accept.

### Writes

- Registry is a coordination view, not lifecycle truth.
- Declare minimal write scope.
- Overlapping active scopes serialize unless there is real physical isolation.
- Central files use read-before-write + narrow patch.
- Reviewer/Verifier remains candidate read-only; editing the candidate ends that independent-review round.

## State semantics

Keep these distinct:

`NOT_STARTED / IN_PROGRESS / CANDIDATE / PASS / FAIL / BLOCKED / SUPERSEDED`

Worker COMPLETE does not mean project PASS.

## Work Node discipline

Preserve:

- Objective
- Owned Scope
- Out of Scope
- Acceptance Criteria
- Protected Invariants
- Dependencies
- Current blocker / next action

Do not enlarge scope because an adjacent problem was noticed.

## Issue / Blocker classification

- **Current-task finding:** already in the Node acceptance scope.
- **Blocker:** transient wait, timeout, dependency or one-time interaction.
- **Independent Issue:** durable out-of-scope problem/requirement needing later work.

## Governance

For substantial work, optional lifecycle:

`Issue → Triage/Milestone → Work Node → Candidate → Required Review Gate → PASS/REPAIR_FIRST/FAIL → Merge → Staging/Release → Closure Memory`

Keep Merge and Release separate.

## Closure

Write high-signal memory only: accepted outcome, capabilities, requirements/invariants, evidence, risks and source pointers. Do not paste full prompts/logs/diffs/secrets.

