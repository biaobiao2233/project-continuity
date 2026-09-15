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
5. Resolve any linked canonical tracker item (for example GitHub Issue/PR) when it materially affects the task.
6. Read only relevant predecessor Closure Memory or Requirement Anchors.
7. Inspect repo/docs/live state needed to execute or verify the current step.
8. Use EverOS only when the continuity layer and source records do not contain enough history.

Do not default to re-reading entire historical worklogs, old chats, or duplicated Issue bodies.

## Multi-conversation coordination

When the project has concurrent or resumable sessions, keep project-level focus, session-local routing, and write ownership separate.

Use this recovery/routing order:

1. Current explicit user task or explicit switch.
2. Existing valid Session Pin for this continuing interaction.
3. The bound Work Node's current state and ownership.
4. Project Primary Focus and the single live Parallel Active Work Registry, if the project uses one.
5. Only a fresh/unpinned session defaults to project-level focus.

A valid Session Pin is not overwritten merely because another session changed Project Primary Focus. Session Pin, Work Node status, GitHub Issue/PR state, and Accepted State remain distinct.

For logical Session Keys:

- Treat the key as coordination identity, not cryptographic or platform identity.
- Use single allocation / no silent reuse. A fresh/cold physical conversation should receive a new key unless claimant continuity for the old key is actually established.
- Old prompts, self-claiming a key, or seeing an existing Registry row do not prove claimant identity.
- Duplicate or ambiguous claimants put that key/scope into `OWNERSHIP_UNCERTAIN`; shared/candidate writes fail closed to read-only.
- Full takeover uses explicit release/transfer plus receiver re-read/accept; do not infer takeover from Last sync, recent activity, Primary Focus, or silence.

For writes:

- Registry is a coordination view, not a lifecycle/acceptance source of truth. Keep one live Registry only when parallel work actually needs it.
- Declare minimal write scope. Overlapping active write scopes serialize unless physically isolated, typically by branch/worktree/sandbox.
- Central shared surfaces are coordinator/single-writer by default. Use read-before-write + narrow patch; if patch context changed, re-read and merge instead of overwriting from a stale snapshot.
- Reviewer/Verifier stays candidate read-only unless explicitly changing role; editing the candidate ends that independent-review round.

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

`Worker Claim → required evidence/review → Primary acceptance → PASS`.

If a previously accepted conclusion is invalidated, mark it `SUPERSEDED` with a reason and replacement; do not silently rewrite history.

## Work Node discipline

A Work Node is a bounded unit of implementation/review/verification, not a date, chat, prompt, GitHub Issue, PR, or file.

Before acting, preserve:

- Objective
- Owned Scope
- Out of Scope
- Acceptance Criteria
- Protected Invariants
- Dependencies
- Current blocker/next action
- Canonical tracker links when relevant

Do not enlarge Owned Scope because a reviewer or implementer notices adjacent work.

## Choose the canonical tracker

Do not maintain two durable Issue systems for the same project.

- **Writable GitHub repository available and used for development** → GitHub is the default durable tracker for substantial bugs/features and PR candidates.
- **No suitable GitHub repository / intentionally local-only project / explicit local preference** → local Issue register is the fallback durable tracker.
- **Small bounded low-risk edit** → may need neither a durable Issue nor a formal Work Node if continuity/risk does not justify it.

Project Continuity still owns execution coordination even when GitHub is canonical: Work Nodes, Session Pins, write ownership, protected invariants, blockers, live/deployment evidence, and next action.

When GitHub is canonical, store only compact references such as `Issue #42`, `PR #57`, branch/commit, acceptance state, and live rollout state. Do not copy the full Issue/PR discussion into local continuity.

## Issue / Blocker classification

When a new problem or requirement appears, classify it before acting:

- **Current-task finding**: already inside the Active Work Node acceptance scope. Keep it in that Node's implementation/review/repair cycle; do not duplicate it as a new Issue.
- **Blocker**: a transient wait, one-off timeout, normal dependency, unavailable external service, or one-time user interaction that prevents the current next step. Record it on the current Node; do not automatically create a durable Issue.
- **Independent Issue**: a durable problem/requirement that is out of scope, needs later work, needs a separate decision/verification, or should survive after the current Node closes. Record it in the project's canonical tracker and triage it later.

If a transient Blocker reveals a durable underlying defect, create/link an Independent Issue in the canonical tracker while keeping the immediate Blocker on the current Node.

## GitHub-first lifecycle

For a substantial change in a GitHub-backed project, prefer the repository's real development lifecycle:

`GitHub Issue → branch/worktree → Work Node execution → Pull Request → required checks/review → merge → staging/release gate → release/promotion`.

Key rules:

- An Issue records a durable problem/request, not current execution ownership.
- A Work Node executes or verifies bounded scope and may link one or more Issues/PRs.
- A PR is a candidate/review surface, not proof of PASS or production release.
- Automated tests do not replace independent review when independent review is required; independent review does not replace required tests/live verification.
- `Merged Source != Staging Accepted != Production Released`.
- Do not create a local mirror Issue merely to imitate GitHub.
- Do not add Project Boards, complex labels, bots, CODEOWNERS, or workflow automation unless repeated real usage justifies them.

## Local fallback lifecycle

When GitHub is not the canonical tracker, use the lightweight local lifecycle only when the work benefits from durable tracking:

`Local Issue → Work Node → Candidate → required review/verification → PASS/REPAIR_FIRST/FAIL → release gate if applicable`.

Use the project's existing Issue ID convention if one exists; do not invent global IDs. Keep this fallback lightweight and migrate to the repository tracker rather than maintaining duplicate ledgers if the project later adopts GitHub as canonical.

## Candidate / Required Review Gate

For a formal candidate, capture only what reviewers need:

- candidate revision / branch / PR / commit
- linked canonical Issues
- Objective and Owned Scope
- changed files/artifacts
- acceptance criteria addressed
- automated checks and results
- known risks/unresolved questions
- rollback/recovery when relevant
- source/staging/production boundary
- Worker Claim
- independent review status when required
- merge/release readiness

After a substantive repair, update the candidate revision/evidence. Do not imply an older review still covers a changed candidate.

For important/high-risk nodes, define required checks such as focused/regression tests, lint/compile, security/adversarial review, scope/diff check, live-state verification, independent reviewer verdict, cleanup/rollback verification, and Primary acceptance. Required checks must run before PASS.

## RFC / ADR discipline

For high-impact or hard-to-reverse decisions—architecture, security boundary, permission model, persistence/data model, migrations, protocol/public API, deployment topology, or major dependency choices—consider a lightweight RFC/ADR before implementation.

Capture at least: Context/Problem, Constraints, Options, Trade-offs, Decision, Consequences, and follow-up verification.

Do not create RFC/ADR documents for routine bug fixes or obvious low-risk implementation choices.

## Continuity writes

Write only high-signal accepted/current material:

- Handoff Card: current goal/state/next action/blockers/invariants.
- Execution Record: executor, purpose, scope, worker claim, changed artifacts, verification, verdict, next action, canonical Issue/PR links when relevant.
- Closure Memory: accepted outcome, durable capabilities, inherited requirements, invariants, evidence, risks, what future agents may/may not assume.

Do not paste full prompts, giant logs, diffs, code, external docs, GitHub discussions, or secrets into Project Continuity.
