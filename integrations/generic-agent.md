# Generic Agent / Antigravity / OpenCode / other coding agents

Project Workbench 采用 **one canonical Skill, many runtime adapters**：

`~/.agents/skills/project-workbench`

如果 Agent 原生扫描 `~/.agents/skills`，直接使用该目录。如果它要求专用 Skill 路径，优先 symlink/junction/native registration 指向 canonical Skill，而不是复制后长期分别维护。

平台差异只写在该 Agent 的全局提示词/规则：native worktree 命令、sandbox/approval、connector/tool routing、Skill 调用语法、UI 行为。

最小接手 Prompt：
```text
使用 Project Workbench Fast Resume，从项目当前 canonical handoff / active tracker 恢复。
只读取完成 Next Action 所需的当前证据；handoff 冲突或缺失时再升级 Deep Recovery。
继续执行到下一个真实 gate。
```
