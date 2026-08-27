# Codex

推荐使用 **explicit-only Project Workbench**：

```text
$project-workbench
```

一个常见的用户级安装位置是：

```text
~/.agents/skills/project-workbench/
```

具体路径和 Skill schema 以当前 Codex runtime 为准，不要盲目复制旧版本目录。

OpenAI/Codex adapter 可以设置：

```yaml
policy:
  allow_implicit_invocation: false
```

这样 ordinary chat / simple edit 不会自动进入 Project Continuity ceremony。

全局 `AGENTS.md` 只保留 always-on stable invariants；Project Workbench 负责 procedure；Project Spine 保存 current project state。

