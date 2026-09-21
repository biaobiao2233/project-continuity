## 【平台适配：Antigravity / Gemini】
- 这是 Antigravity/Gemini 用户级全局上下文；项目中的 `GEMINI.md` 可补充更具体规则，但不能扩大用户授权或绕过安全边界。
- Project Workbench 的权威内容仍只有 `~/.agents/skills/project-workbench`；`~/.gemini/config/skills/project-workbench` 与 `~/.gemini/antigravity-cli/skills/project-workbench` 仅作为 native 入口链接到同一目录，禁止维护第二份副本。
- 以当前会话实际暴露的工具为准；优先离目标最近的 connector / MCP / SSH / API。GitHub 工程记录优先 GitHub connector；历史检索优先 EverOS-Tunnel；服务器/Windows 有 WebCodex 直连时优先对应直连。
- 实质性创建或修改 UI 时，读取最近且适用的 `DESIGN.md`，并保持已批准的路由、字段、文案、权限、行为、可访问性、响应式规则与设计 tokens。
