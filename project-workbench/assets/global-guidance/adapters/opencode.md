## 【平台适配：OpenCode】
- 这是 OpenCode 用户级全局入口；权威全局规则文件是 `~/.config/opencode/AGENTS.md`。项目/子目录 `AGENTS.md` 只补充项目特定规则，不应重新复制一套旧 Project Continuity 生命周期。
- Project Workbench 的唯一 Skill 源继续使用 `~/.agents/skills/project-workbench`。OpenCode 原生会发现全局 `.agents/skills`；不要再复制到 `~/.config/opencode/skills`，除非明确需要用 OpenCode-native 同名 Skill 覆盖共享版本。
- OpenCode 的 Skill 通过 description 出现在可用 Skill 列表，并由原生 `skill` 工具按需加载。若权限策略被收紧，必须确认 `skill` 未被 deny。
- 不依赖 `~/.claude/CLAUDE.md` fallback 作为 OpenCode 主规则来源；显式生成 OpenCode 自己的全局 `AGENTS.md`，避免 Claude/OpenCode 工作流互相遮蔽。
- 以当前会话实际暴露的 MCP/工具为准：GitHub 工程记录优先 GitHub connector；Windows 目标优先 WebCodex-PC；SG/HK/US/KR 目标优先对应 WebCodex；历史语义检索优先 EverOS-Tunnel。缺失能力先发现，再使用已授权 fallback。
