## 【平台适配：ZCode】
- 这是 ZCode 用户级全局入口；工作区更具体的 `AGENTS.md` 可以补充项目规则，但不能扩大用户授权或绕过安全边界。
- 用户级 Project Workbench 的唯一 Skill 源是 `~/.agents/skills/project-workbench`。持续项目、交接、多 Agent 协作、正式集成/发布等场景优先路由到该 Skill；普通问答和一次性低风险修改不要强制触发。
- 以当前会话实际暴露的工具为准；目标系统有直连就优先直连。GitHub、WebCodex、EverOS 等能力不存在或不健康时先区分 provider/transport/target failure，再选择已授权 fallback。
