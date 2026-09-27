# GitHub-backed Project Governance

Use GitHub as the durable development record when a suitable writable repository exists.

GitHub owns durable Issues, branches, PRs, commits, review discussion, CI/check status, and merge history.

Project Continuity owns execution state GitHub does not model well: optional Work Nodes, Session Pins, write ownership, protected invariants, live/deployment evidence, blocker/Next Action.

A compact coordinator handoff may live in GitHub as an index; it must not duplicate full Issue/PR bodies.

## Substantial change lifecycle
`Issue → branch → worktree when isolation is needed → implementation/tests → PR → checks/review → merge → release verification when applicable`

A PR is a candidate/review surface, not proof of acceptance or production release.

## Research lifecycle
- Scout findings/evidence/alternatives → Issue comments.
- Coordinator synthesis/decision → Issue comment or decision record.
- Accepted durable architecture/knowledge → repo docs/ADR through a PR.

## Cloud queue
When agents can execute independent tasks, use `cloud-queue.md` instead of asking the user to relay prompts/results manually.

Do not force Issue/PR ceremony for trivial low-risk edits.
