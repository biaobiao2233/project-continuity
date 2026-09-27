# ChatGPT

ChatGPT 与其它 Agent 使用完全相同的 canonical Project Workbench Skill：

`~/.agents/skills/project-workbench`

如果产品安装流程不能直接读取该目录，则安装内容一致的副本，并以 canonical Skill 为更新源；不要长期分叉。

Global rules:
- `prompts/global-guidance.zh-CN.md`
- `prompts/chatgpt-custom-instructions.zh-CN.md`

账号级提示词保存稳定偏好和 ChatGPT runtime/tool routing。Fast Resume、Cloud Queue、CLAIM、worktree、review、acceptance 只在 Skill 中维护。

更新后用 fresh conversation 验证 ordinary low-risk chat 仍轻量、项目接管优先 Fast Resume、handoff 冲突时能升级 Deep Recovery。
