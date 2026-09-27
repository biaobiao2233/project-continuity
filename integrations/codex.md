# Codex

Codex 与其它 Agent 共用：

`~/.agents/skills/project-workbench`

不要长期维护 `~/.codex/skills/project-workbench` 的独立内容分叉；若当前版本要求 native Skill 路径，使用链接/注册到 canonical Skill。

Codex 特有行为放 `~/.codex/AGENTS.md`，建议基于：
- `prompts/global-guidance.zh-CN.md`
- `prompts/codex-agents.zh-CN.md`

Sandbox / approval / MCP / worktree 等运行时差异属于 AGENTS.md，不属于 Skill。

并发隔离使用 dedicated branch + `git worktree` 或当前 Codex 版本提供的等价可靠机制。不同 writable Agent 不共享 working directory。
