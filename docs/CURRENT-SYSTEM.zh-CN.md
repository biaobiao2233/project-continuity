# 当前实用系统：从 Project Spine 到 EverOS

这份仓库不是只用于展示概念的文档集合。Project Continuity v1.1 仍是稳定协议基线；`project-workbench/` 当前公开 `2.0.0-rc.1` 完整候选，包含 team workflow、只读 checker、测试、eval 和配套提示词。RC 的本地验证不等于目标平台已经安装或验收。

公开仓库的目标是：**公开方法、协议、模板、Skill 与集成边界；不公开用户真实项目数据。**

## 当前实际组成

```text
每个项目
  └─ Project Spine / README
       ├─ Handoff Card
       ├─ Current Requirements
       ├─ Protected Invariants
       ├─ Active Work Node / Resume Point
       ├─ Closure Memory
       └─ Source Pointers

Project Workbench Skill
  ├─ direction → short task → replaceable executor model
  ├─ continuation / ownership / explicit handoff safety
  ├─ GitHub-first Issue / PR / dependency record
  ├─ interface-contract-first parallel work + early integration
  ├─ source/runtime/live-target resource isolation
  ├─ candidate-bound review / release evidence
  ├─ optional read-only resume/preflight/deliver/integrate checker
  └─ direct connector + EverOS historical recovery routing

EverOS
  └─ derived semantic memory / cross-agent historical index

repo / files / tests / live state
  └─ current reproducible evidence
```

其中：

- **Project Continuity** 保存每个项目的当前状态和 authority；
- **Project Workbench** 决定 Agent 接手项目时按什么顺序读取、验证和执行；
- **GitHub** 在已有正式仓库的项目中负责 durable Issue / PR / commit / CI / merge 记录；
- **EverOS-Tunnel** 是当前优先的历史语义检索入口，旧 EverOS connector 只作 fallback；
- **WebCodex** 为已接入的目标主机提供直接 live/repo 操作路径；
- **repo / files / live state** 负责证明现在真实发生了什么。

## 当前公开了什么

- Project Continuity v1.1 协议；
- Project Spine / Work Node / Resume Point / Closure Memory 模板；
- Multi-Conversation Coordination / Session Pin / `OWNERSHIP_UNCERTAIN`；
- GitHub-first Issue / PR / Review / Release governance 与 local fallback；
- 当前 Project Workbench Skill core；
- local-machine connector / direct server WebCodex / EverOS-Tunnel 路由规则；
- ChatGPT / Codex / Claude Code / generic agent 集成说明；
- Compact / Full 两种示例项目；
- EverOS 与多项目联动的 authority 边界；
- Roadmap 与 prior art。

## 当前不会公开什么

真实运行中的以下数据不属于开源协议本身，也不应该因为“开源记忆系统”而被上传：

- 用户真实项目的 Project Spine / worklogs；
- 原始聊天正文与私人历史；
- 内部服务器、私有 endpoint、账号、token、OAuth secret、private key；
- 私有客户/项目名称、未发布功能、生产运行状态；
- 仅对某台机器成立的绝对路径和运维配置。

公开仓库使用通用模板和脱敏示例来表达同一套运行语义。

## Public parity contract

`project-workbench/` 的默认目标仍是保持 **public-safe parity**，但 parity 必须标明生命周期状态：当前公开目录对应 `2.0.0-rc.1` 本地已验证候选，而不是声称所有平台已经安装或接受。Workflow、authority、tool-routing、review/handoff 语义保持一致；机器专属路径、设备别名或私人配置继续脱敏。

当前 invocation policy 是 **adapter-specific**，不是 canonical core 的单一布尔开关：

- checked-in ChatGPT/OpenAI adapter：`allow_implicit_invocation: true`，但 description 明确只匹配持续/可恢复项目、handoff、continuity、live-state、GitHub governance 或多 Agent 协作，并排除普通聊天、一次性低风险修改和不需要连续性的独立 review；
- Codex：当前仍推荐 explicit `$project-workbench`；
- Claude Code：当前仍推荐 explicit `/project-workbench`。

不同平台可以使用不同 invocation metadata，但共享同一套 authority、scope、ownership、review、EverOS boundary 与安全语义。

## 多项目如何共享记忆但不共享 authority

Project Continuity 的 Project Spine 是 **per-project** 的。Project A 的 `PASS`、授权或 Active Work Node 不会自动传播给 Project B。

EverOS 则可以作为共享的 derived historical layer，让 Project B 的 Agent 找到 Project A 曾经解决过的类似问题、历史实验或 source pointer。

因此联动的目标不是：

> “把所有项目状态合成一个全局大脑。”

而是：

> **“每个项目保持自己的当前真相，同时允许历史经验跨项目被检索和复用。”**

完整流程见 [EVEROS-INTEGRATION.md](EVEROS-INTEGRATION.md)。

## 当前集成状态

已经工作的部分：

- Project Workbench 的 Receiver 流程明确把 EverOS 放在 Project Spine / Closure 之后；
- 当前 ChatGPT dogfood 优先使用 `EverOS-Tunnel` 的 `memory_search` / `memory_get` 等做历史恢复；
- 检索结果只作为 derived clue，必须按需要回 source / repo / live state；
- EverOS Control Center 当前相对成熟的是同步流程；搜索、记忆原件和 pipeline/run history 已有界面与数据链路，但仍属于早期能力，不能替代 source/repo/live verification；
- 已有目标主机直连 WebCodex 时，服务器工作优先直接走对应 connector，而不是默认绕本机 SSH/旧代理；
- GitHub-backed 项目默认使用 GitHub 作为 durable Issue/PR ledger，本地 Continuity 只保留协调与 runtime facts；
- 每个项目仍由自己的 Project Continuity 文件保存当前 state / handoff / acceptance。

目前**没有**自动做的部分：

- 不自动把 EverOS memory 晋升为 Project Continuity `PASS`；
- 不自动把一个项目的授权传播到另一个项目；
- 不自动把所有 Handoff / tool logs 全量写进 EverOS；
- 不依赖后台 daemon 抢占项目 ownership；
- Control Center 目前还不是 Project Continuity 的写入数据库。

当前 v2 RC 仍然依赖 Skill/Agent 进入项目连续性流程；ChatGPT 的 narrow implicit discovery 只是降低手动触发成本，Codex/Claude 仍可保持显式调用。新增只读 checker 也不是后台调度器。这仍不是最终形态。

已明确列入 v3 的长期目标是 automatic project context feed：由 host/runtime/adapter 在 Agent 开始工作之前自动 materialize 当前项目的最小连续上下文，从而降低对 Agent 工具调用积极性和提示词遵循质量的依赖。Codex 是优先目标，其他 coding Agent 和技术上可接入的 Web AI 客户端随后复用同一 Context Packet contract。

这里必须区分：`implicit Skill invocation` 仍由模型决定是否触发；automatic context feed 是模型决策之前的 host/runtime-side context materialization。

这些边界是有意保留的安全设计，不是遗漏。
