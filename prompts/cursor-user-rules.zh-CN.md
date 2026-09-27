# Cursor User Rules — Project Workbench

Canonical Skill: `~/.agents/skills/project-workbench`

详细流程来自共享 canonical Skill，不复制进 User Rules。

在 `global-guidance.zh-CN.md` 基础上补：

```text
【Cursor 运行时】
持续项目、跨会话恢复、多 Agent、GitHub-first 项目治理时使用 Project Workbench。

不要维护 ~/.cursor/skills/project-workbench 的长期独立副本；若当前 Cursor 版本要求 native Skill 路径，使用链接/注册指向 canonical 目录。

当 Workbench 要求 worktree isolation 时，优先使用 Cursor 当前版本提供的原生 worktree 能力（如 /worktree）。需要应用结果时按当前版本能力使用 /apply-worktree；worktree 已安全提交/保存且无人继续使用后才使用 /delete-worktree。

如果原生机制不可用，fallback 到 dedicated branch + git worktree。多个 writable Agent 不共享同一个 working directory/worktree。

Cursor 特有命令、Agent UI 和本机工具路由只存在于 Cursor User Rules，不写回 Skill。
```
