# Project Workbench v2 candidate

Version: **2.0.0-rc.4**.

rc.4 makes Project Workbench a smaller cross-agent control plane:

- Fast Resume by default; Deep Recovery only when needed.
- GitHub-first durable ledger.
- Compact Handoff as an index, not a duplicate database.
- Lightweight Cloud Queue + CLAIM protocol.
- Explicit branch/worktree isolation for concurrent writable tasks.
- One canonical Skill shared by every agent.
- Host/runtime differences moved to global guidance.

Canonical local authority:

`~/.agents/skills/project-workbench`

Active references: `fast-resume.md`, `project-continuity.md`, `github.md`, `cloud-queue.md`, `git-worktrees.md`, `everos.md`, `workflows.md`, `agent-setup.md`.

Older rc.3 checker/install assets remain for historical compatibility but are no longer required to understand the core workflow.

File presence, Skill discovery, and correct receiver behavior remain separate gates. The rc.3 50-test result does not automatically certify the changed rc.4 Skill.
