# Project Workbench 2.0.0-rc.4

## Added
- Fast Resume default cold-start path and Deep Recovery escalation.
- Compact GitHub coordinator Handoff template.
- Lightweight GitHub Cloud Queue / CLAIM protocol.
- Explicit branch/worktree isolation reference.
- Cursor integration and Cursor User Rules template.
- Codex global AGENTS template.

## Changed
- GitHub is the preferred durable development ledger when available.
- Handoff is an index into canonical evidence, not a duplicate archive.
- Project Workbench is explicitly platform-neutral.
- One canonical Skill is shared at `~/.agents/skills/project-workbench`.
- Runtime-specific commands/tool routing move to host global guidance.
- Global guidance is shortened to stable principles; detailed governance remains in the Skill.

## Migration
Compare old host-specific copies, move reusable cross-agent improvements into canonical Skill, move host-specific behavior into global rules, verify discovery, then remove/disable duplicate copies.

## Validation boundary
This update does not claim every host has loaded rc.4. File installation, discovery, and model behavior remain separate gates. The rc.3 50-test result must not be reused as if it automatically covered rc.4.
