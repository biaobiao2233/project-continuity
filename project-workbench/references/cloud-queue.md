# Lightweight GitHub Cloud Queue for Multi-Agent Work

Use this when several agents can execute independent bounded tasks and GitHub is already canonical.

Coordinators and workers are replaceable roles. A fresh agent continues from the same Handoff plus the active Issue/PR. Do not replay chat to resume a role or a task.

## Task shape
Prefer one Issue per independently claimable durable task. Include Objective, Owned Scope, Out of Scope, Acceptance Criteria/Required Checks, Protected Invariants, source pointers, allowed writes/actions, and expected completion packet.

## Difficulty
`D1` / `D2` / `D3` records effort for a claimable task. L0-L3 remains the governance-risk scale. A low-risk edit can be `D3` when it needs wide context; a high-risk change can be `D1` when the edit itself is small.

| Tag | Effort |
|---|---|
| D1 | simple: narrow change, obvious checks |
| D2 | moderate: several steps, or one integration boundary |
| D3 | hard: wide context, scarce tools, or tricky invariants |

The Coordinator sets it when posting the task, as both:

- GitHub label `difficulty:D1`, `difficulty:D2`, or `difficulty:D3`;
- body field `Difficulty: D1|D2|D3`.

The label and the body field must match. Leave vendor and model names out of the label. Create the three labels if the repository does not have them yet; do not add a broader priority matrix. If Difficulty is missing, the task may still be claimed; treat fit as unknown.

## Self-selection
Before claiming, prefer a task that fits remaining context size, quota or turn budget, required tool access, and sandbox or write limits. Decline a harder task by not claiming it. Describe fit with those capability terms. Leave vendor and model names out of the note. An optional non-claim comment must not use the CLAIM header.

This choice is advisory. It does not reorder the queue, and a higher Difficulty is not reserved for a specific product. The earliest valid CLAIM still wins.

## Claim protocol
Before claiming:

1. Read the Issue and current comments.
2. Confirm it is open and unclaimed, or that the prior claim is released, owner-reassigned, or stale under the rule below.
3. Post:

```text
CLAIM
Role: Implementer
Session: <fresh unique logical key>
Scope: Issue #42
Difficulty-fit: D2
Capability note: remaining context and repo write tools cover this scope
Takeover: none
```

`Role`, `Session`, and `Scope` are required. `Difficulty-fit` and `Capability note` are optional. Include `Takeover` when replacing a prior claim: `released claim by <session>`, `stale claim by <rule>`, or `owner reassignment`.

4. Re-read comments immediately.
5. The earliest valid GitHub-created CLAIM wins unless the Coordinator resolves otherwise.
6. A losing or invalid claimant must not write the task.

Use a new Session key. Copying the previous claimant's key does not prove continuity. Do not rely on private thread IDs or a heartbeat/lock server.

A worker takeover CLAIM is valid only when the prior claim on that Issue is released, explicitly reassigned by the current user, or the staleness rule is shown from GitHub evidence. A `Role: Coordinator` CLAIM also requires that `Coordinator hosts`, when set, allows this host. An earlier but invalid takeover does not beat a still-active claim. If two takeover claims conflict and GitHub order or the user grant cannot be shown, stop at `OWNERSHIP_UNCERTAIN`.

## Release, staleness, uncertainty
A claim is **released** when its claimant posts `Claim: RELEASED` on the Issue. When the agent can still write, do that inside `RESULT` with `Status: BLOCKED` and a resume point. Quota or context exhaustion should use this path, not a guessed timeout.

A claim is **owner-reassigned** when the current user explicitly tells this session to take the task or the coordinator role. Record that in the new CLAIM. User authorization is not visible to the next agent unless the Issue says so.

A claim is **stale** only by the project's rule, using GitHub-visible evidence from that claimant (Issue/PR comment, commit, or check). Another person's comment does not refresh the claim. Record the rule on the Handoff as `Claim staleness:`.

- Example window: `72h`.
- `explicit release only` disables timeout takeover.
- If the field is unset, the skill default is **72h without claimant evidence**. The takeover CLAIM must say it used that default.

Session Pin `Last sync`, chat silence, or an inferred quota failure is not release. If release, reassignment, or the staleness window cannot be shown from the Issue/PR, stop at `OWNERSHIP_UNCERTAIN`: shared and candidate writes stay read-only, and ask the human. Post:

```text
OWNERSHIP_UNCERTAIN
Scope: Issue #42
Reason: prior CLAIM is neither released nor shown stale under <rule>
Next: human confirms release, or names the next claimant
```

## Takeover
Outgoing agent, if it can still write: post `RESULT` with `Status: BLOCKED`, `Claim: RELEASED`, and a resume point on the active Issue. Update the Handoff only when the gate, blocker, or Next Action changed.

Incoming agent:

1. Re-read the Handoff and the active Issue/PR. Do not replay chat.
2. Post a new CLAIM that names the released, stale, or owner-reassigned claim.
3. Re-read comments. Write only if that CLAIM is the earliest valid one.

Taking a worker task does not make the new claimant the Coordinator.

## Coordinator policy
Who may be Coordinator is per project. On the Handoff, set `Coordinator hosts:` to a project allowlist or a capability class, for example "hosts that can update the Handoff and Issues, and must not deploy". Do not hardcode vendor or model names in this skill. Concrete host names belong in the project, not here.

If `Coordinator hosts` is unset, any agent may claim `Role: Coordinator` after the prior coordinator claim is released, owner-reassigned, or stale. Unset is not a lock, and it does not let a worker inherit the role without that CLAIM.

If the field is set and this host is outside it, do not take central writes. Finish only an already-owned isolated worker task. If this host cannot be matched to the field, `OWNERSHIP_UNCERTAIN` and ask the human.

A vanished Coordinator does not transfer central or deployment authority by absence alone. The same release, staleness, and uncertainty rules apply.

## Execution
After a valid claim, inspect current state independently, use the task's branch/worktree when writable, stay inside scope, continue through safe deterministic steps, and write evidence back to the Issue/PR.

## Result
```markdown
## RESULT
Status: COMPLETE | BLOCKED | CANDIDATE | FAIL
Claim: ACTIVE | RELEASED
### Outcome
...
### Resume point
... required when Status is BLOCKED or Claim is RELEASED
### Evidence
- commit/PR/checks/live evidence
### Remaining risks
...
### Next action
...
```

Worker COMPLETE is not project PASS.

## Coordinator duties
Publish bounded tasks with a Difficulty label and body field, avoid overlapping writable scopes, use worktrees for concurrent code tasks, read results from GitHub rather than user copy/paste, verify before acceptance, and create new work only when the current gate justifies it. When leaving, release the coordinator claim with a resume point.
