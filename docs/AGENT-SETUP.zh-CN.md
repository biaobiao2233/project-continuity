# Project Workbench：统一 Skill + 各 Agent 全局规则

## 目标架构

只维护一份：

`~/.agents/skills/project-workbench`

所有 Agent 使用完全相同的 Skill 内容；运行时差异只放各自全局规则。

Skill 负责 Fast Resume / Deep Recovery、GitHub-first、Handoff、Cloud Queue / CLAIM、branch/worktree isolation 原则、角色、review/acceptance、continuous execution、high-signal continuity。

全局规则负责 sandbox/approval、native worktree 命令、connector/tool routing、Skill 调用语法、UI/运行时行为。

公开模板：
- `prompts/global-guidance.zh-CN.md`
- `prompts/chatgpt-custom-instructions.zh-CN.md`
- `prompts/codex-agents.zh-CN.md`
- `prompts/cursor-user-rules.zh-CN.md`

## 迁移旧副本
发现 `~/.codex/skills/project-workbench`、`~/.cursor/skills/project-workbench` 或其它独立副本时：
1. 先比较，不直接删。
2. 跨 Agent 改进合并回 canonical Skill。
3. runtime-specific 内容移到对应全局规则。
4. 确认目标 Agent 能发现 canonical Skill。
5. 再删除、停用或改成链接。
6. fresh receiver 验证；文件存在不等于 Agent 已加载。

## Cursor
Worktree 命令放 Cursor User Rules：优先 `/worktree`；需要应用时按当前版本使用 `/apply-worktree`；安全保存且无人使用后再 `/delete-worktree`；不可用时 dedicated branch + `git worktree`。

## Codex
Codex 特有 sandbox/approval/MCP/worktree 行为放 `~/.codex/AGENTS.md`。不要把完整 Workbench 再复制进去。

以后升级 Workbench 只更新 canonical Skill 一份。
