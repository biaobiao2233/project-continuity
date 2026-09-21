# Cross-agent installation and migration

Use this when a new conversation or maintainer needs to install Project Workbench and the paired global guidance across the user's coding agents.

## Single authority

Keep exactly one byte-authoritative Skill installation:

`~/.agents/skills/project-workbench`

Do not maintain independently edited copies for each host. Host-native Skill directories may point to this directory with a junction/symlink when that host needs a native path.

Keep the shared guidance sources in `~/.agents/guidance/`. The repository copies under `assets/global-guidance/` are the portable source used to recreate the user's setup.

## Platform map

| Host | Global guidance target | Skill path / behavior | Verification |
|---|---|---|---|
| Codex | `~/.codex/AGENTS.md` | shared `~/.agents/skills/project-workbench` | fresh session / host catalog |
| OpenCode | `~/.config/opencode/AGENTS.md` | natively discovers shared `.agents/skills` | `opencode debug skill` |
| ZCode | `~/.zcode/AGENTS.md` | shared `.agents` authority in the user's current setup | fresh session |
| Antigravity / Gemini | `~/.gemini/GEMINI.md` | native junctions/symlinks point to the shared Skill | link readback + fresh session |
| Claude Code | `~/.claude/CLAUDE.md` | do not assume Skill discovery; verify the current host before adding a native link | fresh session |
| ChatGPT | account personalization/custom-instruction UI | supported ChatGPT Skill flow; account settings are a separate action | new chat receiver |

Current Antigravity native links used by this setup:

- `~/.gemini/config/skills/project-workbench`
- `~/.gemini/antigravity-cli/skills/project-workbench`

Both must resolve to `~/.agents/skills/project-workbench`.

## Recommended procedure

1. Read `docs/AGENT-SETUP.zh-CN.md` and the current release notes.
2. Inspect the target machine first. Do not assume old files, links or host versions still match.
3. Back up every existing global guidance target and any existing Skill directory before replacing it.
4. Install the repository's `project-workbench/` directory to the single shared Skill authority.
5. Copy `assets/global-guidance/core.md` and the five host adapters to `~/.agents/guidance/`.
6. Run `python project-workbench/scripts/install_agent_setup.py --apply` from a trusted repository checkout. The default dry-run performs no writes.
7. For Antigravity, use the script's native-link option or create equivalent junctions/symlinks to the shared Skill.
8. Verify files/links and each host's discovery separately. Copying files is not proof that a running host loaded them.
9. Keep model/provider/MCP credentials outside these files.
10. Record what was installed, what was merely generated, and what still needs a fresh-receiver test.

## Safety

The installer is dry-run by default. `--apply` backs up replaced targets under `~/.agents/backups/project-workbench-agent-setup/<timestamp>/`. It never changes provider credentials, model configuration, ChatGPT account settings, production services, or project repositories other than the user's home guidance/Skill files.

For a machine-specific customization, keep private paths/credentials outside the public repository and layer them locally after this public setup.
