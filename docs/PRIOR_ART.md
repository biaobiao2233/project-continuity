# Prior Art & Design Lineage

Project Continuity 不是下列项目的 fork。本仓库没有复制其源代码；这里记录的是**设计思想的来源和我们选择的边界**。

## 1. SpineCodex

Repository: <https://github.com/GhabiX/SpineCodex>

我们吸收：

- task / work node lifecycle；
- Active Node 保留详细上下文；
- Closed Node 生成 compact memory；
- 已完成阶段退出未来默认活跃上下文；
- “什么时候可以只留下 memory”比“按日期记日志”更重要。

Project Continuity 的 `Work Node` / `Closure Memory` 与这类思想高度相关，但目标不同：

- SpineCodex 更靠近 Codex runtime/context management；
- Project Continuity v1.1 更靠近跨天、跨会话、跨 Agent 的长期可读 project state。

我们没有照搬：

- 不 fork Codex；
- 不要求 SpineJIT runtime；
- 不把树形 runtime state 变成 Markdown 项目的必要条件。

## 2. GitHub collaboration model

我们吸收：

- Issue 是 problem surface，不是 accepted decision；
- Milestone 是 planning aggregation；
- Pull Request 类比 Candidate Change Packet；
- Required Checks；
- branch/worktree 是物理隔离；
- Merge != Release。

我们没有照搬：

- 不为本地 Agent 项目重造完整 GitHub UI；
- 不默认 Project Board / Bot / Webhook / complex labels；
- 不让 GitHub workflow 变成第二套 project truth。

## 3. Orca

Repository: <https://github.com/stablyai/orca>

Orca 的公开 orchestration / worktree 模型强化了 Project Continuity 多会话协议中的几个边界：

- task / lifecycle authority / routing / filesystem placement 应分开；
- supervised helper 与 full handoff 是不同 ownership 语义；
- explicit ownership transfer；
- worktree 是物理隔离，不是 session identity；
- liveness / timeout / UI status 不等于 completion 或 release；
- authority 无法证明时 fail closed，比“猜一个 owner”安全。

这些思想进入了 `Session Pin`、`OWNERSHIP_UNCERTAIN`、claimant-binding 和 explicit handoff 设计。

我们没有照搬：

- daemon；
- orchestration database；
- heartbeat-driven ownership；
- PTY / terminal handle 作为 Markdown protocol 的必要条件。

## 4. EverOS

Upstream / fork used by this project: <https://github.com/biaobiao2233/EverOS>

EverOS 给 Project Continuity 的最大价值不是“替代 Project Spine”，而是帮助确定**derived memory 的正确 authority 边界**。

我们吸收 / 验证：

- AI 提炼后的 Episode / Fact / Profile / Case 等适合历史检索；
- semantic memory 应保留 provenance / source locator；
- 历史 recall 和 current project truth 是两个不同问题。

因此 Project Continuity 明确：

```text
EverOS result = derived historical evidence
!= raw source
!= current Accepted State
!= current authorization
```

## 5. Future context-runtime research

以下项目目前只是未来 v3/v4 研究入口：

- Tamp — <https://github.com/sliday/tamp>
- ContextPilot — <https://github.com/msousa202/ContextPilot>
- TokenTamer — <https://github.com/borhen68/TokenTamer>
- secondwind — <https://github.com/orchetron/secondwind>

它们涉及 request-time context compression / proxy / tool-output reduction 等方向。

**这些实现尚未进入 Project Continuity v1.1。** README 中不能把它们描述成“已吸收能力”。

## Attribution policy

- 公开引用项目名和公开 URL；
- 不声称对方 endorsement；
- 不把对方 benchmark/marketing claim 当成本项目实测结果；
- 如未来复制或修改第三方源码，必须按其实际 license 单独处理 attribution；
- 当前仓库的 v1.1 协议和 Project Workbench 文本为本项目自己的实现/文档。

