# Contributing

欢迎贡献真实 dogfood、失败案例、模板精简、跨 Agent 兼容性和小型工具。

## 先判断问题属于哪一层

- **Protocol bug**：会让新 Agent 恢复错误状态、混淆 authority、破坏 handoff。
- **Ergonomics**：规则正确，但维护成本过高。
- **Adapter bug**：某个平台无法正确加载 / 调用 Project Workbench。
- **Runtime experiment**：Hook / MCP / context injection / proxy 研究。

不要因为一个 runtime experiment 很酷，就修改 v1.1 的 authority model。

## Pull request 建议

较大的变更请说明：

- Problem / evidence
- Scope
- What changed
- Compatibility
- Verification
- Risks
- Rollback

若变更触及 authority、ownership、release、secret handling 或 destructive behavior，建议由另一个 context / agent 做独立 review。

普通文档错字和小修不需要机械创建复杂治理流程。

## Privacy

提交 example / bug report 前请删除：

- token / password / API key；
- 私有域名/IP；
- 真实客户/用户内容；
- 未公开项目名；
- 完整 AI 会话和隐藏 reasoning。

