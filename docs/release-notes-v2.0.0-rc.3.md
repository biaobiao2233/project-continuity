# Project Workbench 2.0.0-rc.3

发布日期：2026-09-21

这是一个面向跨 Agent 部署/迁移的小步预发布版本。目标是让新的对话或维护 Agent 只拿到这个仓库，就能安全恢复 Project Workbench Skill 与配套全局提示词，而不依赖旧聊天里的手工路径说明。

## 主要变化

- 新增 `docs/AGENT-SETUP.zh-CN.md`：给 Codex、OpenCode、ZCode、Antigravity/Gemini、Claude Code 和 ChatGPT 的安装/验证/迁移说明。
- 新增 `project-workbench/references/agent-setup.md`：Skill 内可按需读取的跨 Agent 安装参考。
- 新增 `assets/global-guidance/`：一份公共核心 + 五个平台薄 adapter，避免多个 Agent 各自长期维护一份漂移的提示词。
- 新增 `scripts/install_agent_setup.py`：默认 dry-run；`--apply` 后才写；自动备份；可为 Antigravity 创建 native junction/symlink；拒绝无确认覆盖非托管提示词或真实 Skill 目录。
- OpenCode 继续直接使用共享 `~/.agents/skills/project-workbench`，不会创建 `.config/opencode/skills` 第二份副本。
- Antigravity native Skill 入口只链接到共享权威目录，不维护第二份字节副本。

## 验证

- 完整测试：**50 / 50 PASS**。
- 新增 3 项 installer 测试：dry-run 不写、隔离 HOME 真安装 + 第二次幂等、非托管提示词拒绝覆盖。
- Windows 隔离 HOME 实装：五个平台全局提示词 5/5 生成；共享 Skill VERSION 正确；两个 Antigravity junction 解析到同一共享目录；OpenCode duplicate Skill = false。
- 从隔离安装后的 Skill 路径再次运行原有测试：47 / 47 PASS。
- `git diff --check` 与 public private-marker scan 仍作为发布前 gate。

## 使用

先读：

- `project-workbench/references/agent-setup.md`
- `docs/AGENT-SETUP.zh-CN.md`

默认检查：

```text
python project-workbench/scripts/install_agent_setup.py
```

用户明确授权后应用：

```text
python project-workbench/scripts/install_agent_setup.py --apply --link-antigravity
```

文件已写入、Skill 已发现、fresh receiver 已按预期工作仍然是三个不同结论；脚本不会把其中一个冒充成另一个。
