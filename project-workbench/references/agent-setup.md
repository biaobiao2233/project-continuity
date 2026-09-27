# Cross-agent installation and migration

## One canonical Skill
Keep one byte-authoritative Project Workbench installation:

`~/.agents/skills/project-workbench`

All agents should discover or link to this same directory. Do not maintain independently edited Codex/Cursor/Antigravity/OpenCode/Claude copies.

## Responsibility split
- **Skill**: Fast Resume, Deep Recovery, GitHub-first, Cloud Queue/CLAIM, worktree isolation principles, review/acceptance, handoff.
- **Host global guidance**: runtime commands, sandbox/approval, native worktree commands, connector/tool routing.
- **Repo-local instructions**: project-specific invariants, build/test conventions, local constraints.

## Migration
1. Inspect host global rules and existing Workbench copies.
2. Back them up.
3. Verify canonical Skill is complete.
4. Compare old host copies.
5. Move cross-agent improvements into canonical Skill.
6. Move runtime-specific behavior into host global guidance.
7. Remove/disable duplicate copies only after discovery is verified.
8. Verify with a fresh receiver.

File presence is not proof that a running agent loaded the Skill.
