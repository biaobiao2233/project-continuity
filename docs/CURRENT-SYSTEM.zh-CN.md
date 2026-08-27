# 当前实用系统：从 Project Spine 到 EverOS

这份仓库不是只用于展示概念的文档集合。`project-workbench/` 与 Project Continuity v1.1 文档共同构成当前实际 dogfood 的项目持续记忆系统公开版。

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
  ├─ continuation / handoff routing
  ├─ Session Pin / ownership safety
  ├─ Issue → Work Node → Candidate → Gate
  ├─ Coding Tools / local-machine routing
  ├─ SG coding-workspace routing
  └─ EverOS historical recovery routing

EverOS
  └─ derived semantic memory / cross-agent historical index

repo / files / tests / live state
  └─ current reproducible evidence
```

其中：

- **Project Continuity** 保存每个项目的当前状态和 authority；
- **Project Workbench** 决定 Agent 接手项目时按什么顺序读取、验证和执行；
- **EverOS** 在 Project Spine 信息不足时提供跨会话、跨 Agent、跨项目的历史线索；
- **repo / files / live state** 负责证明现在真实发生了什么。

## 当前公开了什么

- Project Continuity v1.1 协议；
- Project Spine / Work Node / Resume Point / Closure Memory 模板；
- Multi-Conversation Coordination / Session Pin / `OWNERSHIP_UNCERTAIN`；
- GitHub-style Issue / Candidate / Review / Release governance；
- 当前 Project Workbench Skill core；
- Coding Tools MCP / SG MCP / EverOS 路由规则；
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

`project-workbench/` 的默认目标是与当前 accepted user-level Project Workbench package 保持 **public-safe parity**，而不是长期维护一个“公开精简版”。Workflow、authority、tool-routing、review/handoff 语义保持一致；机器专属路径、设备别名或私人配置允许在公开版中脱敏。

当前公开默认策略：

```yaml
policy:
  allow_implicit_invocation: false
```

也就是 **explicit-only**。原因是 Project Workbench 会触发项目状态恢复、repo/live verification 和治理流程；默认显式调用可以避免普通聊天或简单一次性任务被项目工作流劫持。

不同平台可以自行提供 adapter，但如果改变 implicit policy，应把它视为平台策略变化，而不是静默改写 canonical workflow。

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
- 有 EverOS memory tools 时，可以用 `memory_search` / `memory_get` 等做历史恢复；
- 检索结果只作为 derived clue，必须按需要回 source / repo / live state；
- EverOS Control Center 当前真正相对成熟的是**同步流程**；搜索、记忆原件和 pipeline / run history 虽然已有界面和数据链路，但仍属早期实验，其中记忆原件可读性明显不足，不能当成成熟阅读器；
- 每个项目仍由自己的 Project Continuity 文件保存当前 state / handoff / acceptance。

目前**没有**自动做的部分：

- 不自动把 EverOS memory 晋升为 Project Continuity `PASS`；
- 不自动把一个项目的授权传播到另一个项目；
- 不自动把所有 Handoff / tool logs 全量写进 EverOS；
- 不依赖后台 daemon 抢占项目 ownership；
- Control Center 目前还不是 Project Continuity 的写入数据库。

这些边界是有意保留的安全设计，不是遗漏。
