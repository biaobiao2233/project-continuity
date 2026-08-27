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

## Future: automatic project context feed

`explicit-only` 是**当前 v1.x 的安全默认**，不是最终目标。

长期方向是不要求 Codex 自己想起来执行 `$project-workbench`。计划研究一个 host/runtime-side Project Context Compiler：在新任务、项目切换或 resume 时，先读取当前 Project Spine / Active Work Node / Handoff / Protected Invariants，生成最小 Context Packet，再把任务交给模型。

```text
Codex task
   ↑
minimal Project Context Packet
   ↑
Project Context Compiler
   ↑
Project Spine / Work Node
```

因此未来的 automatic feed 与 `allow_implicit_invocation: true` 不是一回事。前者不依赖模型的工具调用积极性；后者仍然依赖模型决定是否调用 Skill。

