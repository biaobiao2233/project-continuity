## 【平台适配：Codex】
- 这是 Codex 用户级全局入口；项目/子目录 `AGENTS.md` 可以按范围补充更具体规则，但不能扩大用户授权或绕过安全边界。
- 用户级 Project Workbench 的唯一 Skill 源是 `~/.agents/skills/project-workbench`。持续项目、交接、多 Agent 协作、正式集成/发布等任务可按 Skill description 自动触发；普通问答和一次性低风险修改不要强制触发。
- 以当前会话实际暴露的工具为准：GitHub 工程记录优先 GitHub connector；Windows 目标优先 WebCodex-PC；SG/HK/US/KR 目标优先对应 WebCodex；历史语义检索优先 EverOS-Tunnel。某能力未暴露时先发现，再使用已授权 fallback，不猜工具存在。
