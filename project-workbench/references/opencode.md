# OpenCode integration

Checked on 2026-09-21 against OpenCode 1.18.3 and current official documentation.

## Global instructions

- Use `~/.config/opencode/AGENTS.md` as OpenCode's explicit user-level global instruction file.
- Project and nested `AGENTS.md` files add project-specific guidance. Keep reusable Project Workbench governance in the global/core layer and keep repository-specific facts near the repository.
- OpenCode can fall back to `~/.claude/CLAUDE.md` when its own global AGENTS file is absent on compatible versions. Prefer an explicit OpenCode global AGENTS file when workflows differ so Claude compatibility does not silently reintroduce stale policy.
- Do not rely on an `instructions` config array unless the installed OpenCode version is verified to resolve it. `AGENTS.md` is the portable active path.

## Skill discovery

OpenCode discovers global Skills from `~/.config/opencode/skills`, `~/.claude/skills`, and `~/.agents/skills`, plus corresponding project-local paths. A shared Project Workbench installation under `~/.agents/skills/project-workbench` therefore does not need a duplicate OpenCode copy.

Avoid duplicate IDs unless an override is intentional: OpenCode applies source precedence, so a same-name OpenCode-native Skill can override the shared `.agents` definition.

Each Skill needs YAML `name` and `description`. OpenCode advertises eligible skills by metadata and loads the full body through its native `skill` tool when needed. Verify `permission.skill`/general permissions if a Skill is unexpectedly hidden or blocked.

## Deterministic checks

Prefer these checks before a model-level receiver test:

```text
opencode --version
opencode debug paths
opencode debug skill
```

Confirm the expected Skill name and canonical location. A model/provider timeout in `opencode run` is not evidence that Skill discovery failed; distinguish provider/runtime failure from catalog discovery.

## Current-source references

- https://opencode.ai/docs/skills
- https://opencode.ai/docs/zh-cn/rules/
- https://opencode.ai/docs/zh-cn/agents/
- https://dev.opencode.ai/docs/config/
