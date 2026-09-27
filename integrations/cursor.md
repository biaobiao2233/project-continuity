# Cursor

Cursor 与其它 Agent 共用：

`~/.agents/skills/project-workbench`

不要长期维护 `~/.cursor/skills/project-workbench` 的独立内容分叉；若当前版本要求 native Skill 路径，使用链接/注册到 canonical 目录。

Cursor 特有行为放 User Rules / global rules，建议基于：
- `prompts/global-guidance.zh-CN.md`
- `prompts/cursor-user-rules.zh-CN.md`

当 Workbench 要求 physical isolation 时，优先使用当前 Cursor 版本提供的原生 worktree workflow（例如 `/worktree`）；需要应用/删除 worktree 时按当前版本支持的 `/apply-worktree` / `/delete-worktree` 行为执行。原生能力不可用时 fallback 到 dedicated branch + `git worktree`。

这些命令属于 Cursor runtime adapter，不进入 canonical Skill。
