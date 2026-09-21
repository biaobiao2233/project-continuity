# Project Workbench 2.0.0-rc.2

发布日期：2026-09-21

这是 `2.0.0-rc.1` 的小步预发布更新，重点修复 **OpenCode 仍被旧工作流注入** 的真实使用问题，并把 OpenCode 纳入同一套“一份 Skill 权威源 + 平台薄适配器”结构。

## 主要变化

- 新增 `references/opencode.md`：记录 OpenCode 当前的全局 `AGENTS.md`、Skill discovery、same-name precedence、权限和验证方式。
- 新增 `assets/adapters/opencode.md`：明确 OpenCode 使用自己的全局 `~/.config/opencode/AGENTS.md`，而 Project Workbench Skill 继续复用 `~/.agents/skills/project-workbench`，不维护第二份副本。
- Skill 导航增加 OpenCode 入口；rollout / sources / README / validation report 同步到 `2.0.0-rc.2`。
- 保留 v2 的 EverOS derived-only、GitHub-first、Work Node 可选化、early integration、candidate-bound evidence 与“下一步明确就持续执行到真实 gate”行为。

## 真实 OpenCode 验证

在 Windows 上用 OpenCode `1.18.3` 验证：

- `opencode debug paths` 返回全局配置目录 `~/.config/opencode`；
- `opencode debug skill` 能真实找到 `project-workbench`；
- catalog location 指向共享 `~/.agents/skills/project-workbench/SKILL.md`；
- OpenCode 全局 `AGENTS.md` 回读包含 v2 核心规则。

一次 fresh `opencode run` 的模型级 receiver 探针在 120 秒内没有返回，因此本 RC **不声称 OpenCode 模型自动调用行为已经验收**。这与 Skill catalog / 配置解析是否成功是两个不同 gate。

## 测试

- Python 标准库测试：**47 / 47 PASS**。
- `git diff --check`：PASS。
- public private-marker scan：0 命中。
- OpenCode catalog deterministic check：PASS。

## 边界

这是 prerelease RC。Project Continuity v1.1 仍是稳定协议基线。rc.2 不授权生产变更、不改变 ChatGPT 账号个性化设置，也不把 provider/runtime timeout 当成 Skill discovery failure。
