# Project Continuity and Governance

## Authority model

Use this order when evidence conflicts:

1. Current explicit user intent and authorization.
2. Independently verified Accepted Project State.
3. Current repository/files/live reproducible evidence.
4. Worker Claim / executor report.
5. Agent summary or inference.
6. EverOS-derived clue/index memory.

Never upgrade a lower layer into a higher layer without verification.

## Receiver/read order

For project continuation or handoff:

1. Read the Project Spine / Handoff Card.
2. Identify the actual Active Work Node and accepted predecessors.
3. Read current requirements and Protected Invariants needed for the task.
4. Read the Active Work Node contract: Objective, Owned Scope, Out of Scope, Acceptance Criteria, blockers, next action.
5. Read only relevant predecessor Closure Memory or Requirement Anchors.
6. Inspect repo/docs/live state needed to execute or verify the current step.
7. Use EverOS only when the continuity layer does not contain enough history.

Do not default to re-reading entire historical worklogs or old chats.


## Multi-conversation coordination

When the project has concurrent or resumable sessions, keep project-level focus, session-local routing, and write ownership separate.

Use this recovery/routing order:

1. Current explicit user task or explicit switch.
2. Existing valid Session Pin for this continuing interaction.
3. The bound Work Node's current state and ownership.
4. Project Primary Focus and the single live Parallel Active Work Registry, if the project uses one.
5. Only a fresh/unpinned session defaults to project-level focus.

A valid Session Pin is not overwritten merely because another session changed Project Primary Focus. Session Pin, Work Node status, and Accepted State remain distinct.

For logical Session Keys:

- Treat the key as coordination identity, not as cryptographic or platform identity.
- Use single allocation / no silent reuse. A fresh/cold physical conversation should receive a new key unless claimant continuity for the old key is actually established.
- Old prompts, self-claiming a key, or seeing an existing Registry row do not prove claimant identity.
- Duplicate or ambiguous claimants put that key/scope into `OWNERSHIP_UNCERTAIN`; shared/candidate writes fail closed to read-only.
- Full takeover uses explicit release/transfer plus receiver re-read/accept; do not infer takeover from Last sync, recent activity, Primary Focus, or silence.

For writes:

- Registry is a coordination view, not a lifecycle/acceptance source of truth. Keep one live Registry when parallel work actually needs it.
- Declare minimal write scope. Overlapping active write scopes serialize unless physically isolated (for code, typically branch/worktree).
- Central shared surfaces are coordinator/single-writer by default. Use read-before-write + narrow patch; if patch context changed, re-read and merge instead of overwriting from a stale snapshot.
- Reviewer/Verifier stays candidate read-only unless explicitly changing role; editing the candidate ends that independent-review round.
- Temporary non-owner writes to coordinator-owned central fields require a pre-persisted bounded delegation when auditability matters.

Do not introduce heartbeat, daemon, lock server, automatic cross-chat messaging, or a dependency on private ChatGPT thread IDs merely to implement this protocol.

## State semantics

Keep these states distinct:

- `NOT_STARTED`
- `IN_PROGRESS`
- `CANDIDATE`
- `PASS`
- `FAIL`
- `BLOCKED`
- `SUPERSEDED`

`Worker COMPLETE` does not mean project PASS. A typical acceptance path is:

`Worker Claim → Independent Evidence/Review → Primary acceptance → PASS`.

If a previously accepted conclusion is invalidated, mark it `SUPERSEDED` with a reason and replacement; do not silently rewrite history.

## Work Node discipline

A Work Node is a bounded unit of implementation/review/verification, not a date, chat, prompt, or file.

Before acting, preserve:

- Objective
- Owned Scope
- Out of Scope
- Acceptance Criteria
- Protected Invariants
- Dependencies
- Current blocker/next action

Do not enlarge Owned Scope because a reviewer or implementer notices adjacent work.

## Issue / Blocker classification

When a new problem or requirement appears, classify it before acting:

- **Current-task finding**: already inside the Active Work Node acceptance scope. Keep it in that Node's implementation/review/repair cycle; do not duplicate it as an Issue.
- **Blocker**: a transient wait, one-off timeout, normal dependency, unavailable external service, or one-time user interaction that prevents the current next step. Record it on the current Node; do not automatically create an Issue.
- **Independent Issue**: a durable problem/requirement that is out of scope, needs later work, needs a separate decision/verification, or should survive after the current Node closes. Record it in the project's Issue register and triage it later.

If a transient Blocker reveals a durable underlying defect, create/link an Issue for the durable defect while keeping the immediate Blocker on the current Node.

## GitHub-style governance

Use this lifecycle when the project/change is substantial enough to benefit from it:

`Issue → Triage/Milestone → Work Node → Candidate Change Packet → Required Review Gate → PASS/REPAIR_FIRST/FAIL → Source Merge → Staging/Release Gate → Release/Promotion`.

Key rules:

- **Issue records a problem, not a decision.**
- Use the project's stable Issue ID convention if one exists; do not invent a global prefix.
- Issue and Work Node may be many-to-many.
- Milestone is a planning aggregation/view, not another source of truth.
- Candidate Change Packet is a review surface/Worker Claim, not PASS.
- Required Review Gate determines which checks are mandatory. Missing required checks block PASS.
- Automated tests do not replace independent review when independent review is required, and independent review does not replace required tests/live verification.
- `Accepted/Merged Source != Staging Accepted != Production Released`.
- Do not create Project Boards, complex labels, bots, fork automation, auto issue/PR sync, or CODEOWNERS automation merely to imitate GitHub. Add them only when repeated real usage justifies them.

## Triage and Milestone

Triage decides whether an Issue is real/duplicate, its impact/priority, whether to act now, its target stage/version, and whether it needs one or more Work Nodes. Preserve reasons for `DEFER`, `WONT_FIX`, or `DUPLICATE` when those states are used.

A Milestone may group Issues and Work Nodes around a target release or phase, but it must not become a second state machine.

## Candidate Change Packet

For a formal candidate, capture compactly:

- Candidate revision
- Worker/executor
- Linked Issues
- Objective/why
- Owned Scope
- Changed files/artifacts
- What changed
- Acceptance criteria addressed
- Automated checks and results
- Known risks/unresolved questions
- Breaking changes
- Rollback/recovery
- Source/staging/production boundary
- Worker Claim
- Independent review status
- Merge readiness
- Release readiness

After a substantive repair, update the candidate revision/evidence. Do not imply an older review still covers a changed candidate.

## Required Review Gate

Use an explicit gate for important/high-risk nodes. Common checks:

- Focused tests
- Regression tests
- Lint/compile
- Security/adversarial review
- Scope/diff check
- Live-state/staging verification
- Independent reviewer verdict
- Cleanup/rollback verification
- Primary acceptance

Required checks must be satisfied before PASS.

## RFC / ADR discipline

For high-impact or hard-to-reverse decisions—architecture, security boundary, permission model, persistence/data model, migrations, protocol/public API, deployment topology, or major dependency choices—consider a lightweight RFC/ADR before implementation.

Capture at least: Context/Problem, Constraints, Options, Trade-offs, Decision, Consequences, and follow-up verification.

Do not create RFC/ADR documents for routine bug fixes or obvious low-risk implementation choices.

## Continuity writes

Write only high-signal accepted/current material:

- Handoff Card: current goal/state/next action/blockers/invariants.
- Execution Record: executor, purpose, scope, worker claim, changed artifacts, verification, verdict, next action.
- Closure Memory: accepted outcome, durable capabilities, inherited requirements, invariants, evidence, risks, what future agents may/may not assume.

Do not paste full prompts, giant logs, diffs, code, external docs, or secrets into Project Continuity.
