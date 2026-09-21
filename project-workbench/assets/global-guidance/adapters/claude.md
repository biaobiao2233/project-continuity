## 【平台适配：Claude Code】
- 这是 Claude Code 用户级全局入口；项目/子目录 `CLAUDE.md` 可补充更具体规则，但不能扩大用户授权或绕过安全边界。
- 若当前 Claude Code 会话实际发现 `project-workbench` Skill，则在持续项目、交接、多 Agent 协作、正式集成/发布等场景使用它；若当前会话未发现，不凭别的平台状态假设存在。
- 以当前会话实际暴露的工具为准；优先离目标最近、已授权且健康的直连能力，GitHub/服务器/Windows/历史检索均先发现后使用。
