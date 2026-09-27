# Codex Global AGENTS.md — Project Workbench

Canonical Skill: `~/.agents/skills/project-workbench`

详细流程来自共享 canonical Skill，不复制进 AGENTS.md。

在 `global-guidance.zh-CN.md` 基础上补：

```text
【Codex 运行时】
持续项目、跨会话恢复、多 Agent、GitHub-first 项目治理时使用 Project Workbench。

不要维护 ~/.codex/skills/project-workbench 的长期独立副本；若当前 Codex 版本要求 native Skill 路径，使用链接/注册指向 canonical 目录。

遵循当前 Codex sandbox、approval、MCP 和工具能力。运行时差异只放本 AGENTS.md，不写回 Skill。

需要并发隔离时使用 dedicated branch + git worktree；不同 writable Agent 不共享一个 working directory/worktree。

用户级 AGENTS.md 只保存稳定运行时原则；repo 内更具体的 AGENTS.md 可补项目约束，但不要复制完整 Project Workbench。
```
