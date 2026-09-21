## OpenCode adapter

- Global instructions: `~/.config/opencode/AGENTS.md`.
- Shared Skill authority: `~/.agents/skills/project-workbench`; OpenCode discovers this path natively, so do not maintain a second copy under `.config/opencode/skills` unless an explicit override is intended.
- Project/nested `AGENTS.md` files should contain repository-specific guidance, not a duplicated legacy Project Continuity lifecycle.
- Verify Skill visibility with `opencode debug skill`; check permissions if the native `skill` tool cannot load it.
- Keep provider/model/MCP configuration separate from governance text and never copy credentials into AGENTS or Skill files.
