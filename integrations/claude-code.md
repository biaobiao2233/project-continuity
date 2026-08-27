# Claude Code

Claude Code 可以把 canonical core 放到个人 Skill：

```text
~/.claude/skills/project-workbench/SKILL.md
~/.claude/skills/project-workbench/references/...
```

推荐 explicit-only：

```yaml
---
name: project-workbench
description: <project continuity / handoff / review description>
disable-model-invocation: true
---
```

然后由用户显式调用：

```text
/project-workbench
```

Claude 的 `~/.claude/CLAUDE.md` 只保存 always-on stable invariants，不复制完整 Project Continuity schema。

平台 adapter 不需要复制 OpenAI 的 `agents/openai.yaml`、icon 或 `allow_implicit_invocation` metadata。

