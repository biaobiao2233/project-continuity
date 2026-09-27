# Lightweight GitHub Cloud Queue for Multi-Agent Work

Use this when several agents can execute independent bounded tasks and GitHub is already canonical.

## Task shape
Prefer one Issue per independently claimable durable task. Include Objective, Owned Scope, Out of Scope, Acceptance Criteria/Required Checks, Protected Invariants, source pointers, allowed writes/actions, and expected completion packet.

## Claim protocol
Before claiming:
1. Read Issue and current comments.
2. Confirm it is open/ready/unclaimed.
3. Post:
```text
CLAIM
Role: Implementer
Session: <fresh unique logical key>
Scope: Issue #42
```
4. Re-read comments immediately.
5. Earliest valid GitHub-created claim wins unless Coordinator resolves otherwise.
6. Losing claimant must not write the task.

Do not rely on private thread IDs or heartbeat/lock servers.

## Execution
After a valid claim, inspect current state independently, use the task's branch/worktree when writable, stay inside scope, continue through safe deterministic steps, and write evidence back to Issue/PR.

## Result
```markdown
## RESULT
Status: COMPLETE | BLOCKED | CANDIDATE | FAIL
### Outcome
...
### Evidence
- commit/PR/checks/live evidence
### Remaining risks
...
### Next action
...
```

Worker COMPLETE is not project PASS.

## Coordinator
Publish bounded tasks, avoid overlapping writable scopes, use worktrees for concurrent code tasks, read results from GitHub rather than user copy/paste, verify before acceptance, and create new work only when the current gate justifies it.
