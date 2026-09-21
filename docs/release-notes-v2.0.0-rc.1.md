# Project Workbench 2.0.0-rc.1

发布日期：2026-09-21

这是 Project Continuity v1.1 稳定协议之上的 **Project Workbench v2 预发布候选**。目标不是增加更多流程对象，而是让多个方向像真实项目组一样独立推进、尽早集成，并把 GitHub 工程记录、执行协调和 live truth 放到各自合适的表面。

## 主要变化

- 长期方向（Lane）与短期可交付任务分开；conversation / Agent 是可替换执行者。
- GitHub Issue / PR / native dependencies 优先作为工程账本；Work Node 只在执行连续性需要时补充。
- 授权、当前观测、准确版本的验收分开判断，不再用一条“可信度排序”混在一起。
- 先固定 versioned interface contract，再并行实现并进行 early integration。
- 分别检查 source workspace、runtime resource、live target；worktree 不等于生产资源锁。
- Reviewer / integration / deployment evidence 绑定到准确 candidate 和 environment；candidate 改变后旧 verdict 不自动延续。
- 记录同步失败显式保留 `RECORD_SYNC_PENDING`，不为补账重复部署。
- 新增标准库只读工具 `scripts/workbench.py`：`resume`、`preflight`、`deliver`、`integrate`。它只检查调用方提供的 JSON 快照，不联网、不查询 GitHub、不抢 ownership、不 merge、不 deploy、不 auto-accept。

## 配套内容

- 完整 ChatGPT 中文提示词：`prompts/chatgpt-custom-instructions.zh-CN.md` 与 `project-workbench/assets/personalization-v2.txt`。
- 字符受限短版：`project-workbench/assets/personalization-v2-compact.txt`。
- Codex explicit-only adapter 示例：`project-workbench/assets/adapters/codex-openai.yaml`。
- receiver scenarios、validation report、synthetic packets 与完整单元测试均随源码公开。

## 已验证

候选在发布前通过 **47 项本地测试，0 skipped**，包含：

- checker / packet validation；
- candidate/review drift；
- shared resource conflict；
- 一个临时 Git 仓库中的双 worktree + integration pilot；
- bundle/reference/prompt checks。

## 仍未宣称

这个 RC **不声称**以下事项已经完成：

- fresh AI receiver 行为验收；
- 当前用户 ChatGPT / Codex 实际安装、发现或加载；
- GitHub-hosted CI / merge queue 的真实 dogfood；
- 任何生产路由器/服务器部署。

因此 `2.0.0-rc.1` 应按预发布使用；稳定版升级取决于后续真实 receiver / 多方向项目 dogfood。
