# Project Continuity

**让一个没参与旧聊天的 AI Agent，不重放完整历史，也能安全、准确地接手长期项目。**

[English](README.en.md) · [规范](docs/SPECIFICATION.zh-CN.md) · [模板](docs/TEMPLATES.md) · [多会话协调](docs/COORDINATION.zh-CN.md) · [EverOS 联动](docs/EVEROS-INTEGRATION.md) · [路线图](ROADMAP.md)

Project Continuity 是一套面向 ChatGPT、Codex、Claude Code、Antigravity、OpenCode 等 Agent 的**跨会话 / 跨 Agent 项目连续记忆协议**。

它不是聊天记录归档器，也不是向量数据库。它只解决三个问题：

> **现在要记什么？什么能信？下一个 Agent 怎么继续？**

当前公开基线：**v1.1 Markdown Protocol + Project Workbench**。

## 为什么需要它

长项目最常见的问题不是模型完全失忆，而是：

- 新对话不知道项目真正做到哪；
- Worker 说“完成”被后续摘要误写成 PASS；
- 几个并行 Agent 修改同一项目后发生串台或双写；
- 为了恢复上下文，被迫重读几万字旧聊天和巨型 worklog；
- AI 生成的历史摘要被当成当前事实或生产授权；
- 已经关闭的阶段仍然长期占据活跃上下文。

Project Continuity 把这些问题拆成几个稳定对象：

```text
Project Spine
  ├─ Handoff Card              当前交接面
  ├─ Current Requirements      当前有效需求
  ├─ Protected Invariants      绝不能破坏的边界
  ├─ Work Node                 可独立推进 / 验收 / 关闭的工作单元
  ├─ Current Resume Point      半路暂停时的物理执行边界
  ├─ Closure Memory            已关闭阶段留下的压缩记忆
  └─ Source Pointers           需要时回到 repo / artifact / 原始证据
```

核心验收标准只有一个：

> **一个完全没参与前面工作的强 Agent，仅通过 Project Spine、相关 Closure Memory 和必要项目文件，能否安全开始下一步？**

## 核心原则

### Lifecycle over chronology

按**工作生命周期**拆 Work Node，不按日期、聊天次数或 Prompt 数量拆账本。已完成 Node 生成 Closure Memory，详细过程退出正常恢复路径。

### Authority / Provenance 分层

默认可信顺序：

```text
当前用户明确意图 / 授权
  > 独立验证后接受的项目状态
  > repo / files / live reproducible evidence
  > Worker Claim
  > Agent summary / inference
  > derived historical memory
```

因此：

```text
Worker COMPLETE != PASS
Candidate != Accepted State
Merged Source != Staging Accepted != Production Released
```

### Closure over replay

正常接手优先读 Closure Memory，不重放完整旧聊天。

### In-flight 与 Closed Memory 分开

Closure Memory 适合“已经结束的阶段”；Current Resume Point 适合“文件改了一半、测试刚失败、临时服务还在跑”的中途接手。

### Multi-session fail closed

同一个项目可以有多个会话，但：

- 当前明确任务优先于项目级焦点；
- 有效 Session Pin 不被后来更新的 Primary Focus 静默带跑；
- fresh/cold conversation 不静默复用旧 Logical Session Key；
- claimant / ownership 无法证明时进入 `OWNERSHIP_UNCERTAIN`；
- shared/candidate 写入默认 fail-closed 为只读；
- 重叠写入串行，或用 branch/worktree 做真实物理隔离。

### Governance proportionality

不是所有任务都要 Issue、Milestone、Reviewer 和 RFC。高风险或长期工程可以使用：

```text
Issue
→ Triage / Milestone
→ Work Node
→ Candidate Change Packet
→ Required Review Gate
→ PASS / REPAIR_FIRST / FAIL
→ Merge
→ Staging / Release Gate
→ Closure Memory
```

简单修改就保持简单。

## 5 分钟开始使用

### 方式 A：纯 Markdown

复制：

- `examples/compact-project/README.md`：小项目；
- `examples/full-project/README.md` + `worklogs/`：长期项目；
- `docs/TEMPLATES.md`：完整模板。

把项目入口固定为一个 Project Spine，然后告诉 Agent：

```text
先读取本项目的 Project Spine。
恢复当前目标、有效需求、Protected Invariants、当前 Work Node、
Relevant Closure Memory 和 Next Action。
不要默认重放全部旧聊天；当前事实需要时重新检查 repo/live state。
```

### 方式 B：Project Workbench Skill

仓库内提供 `project-workbench/`，把 Project Continuity 变成按需工作流控制面。

平台适配见：

- [ChatGPT](integrations/chatgpt.md)
- [Codex](integrations/codex.md)
- [Claude Code](integrations/claude-code.md)
- [Antigravity / generic agents](integrations/generic-agent.md)

推荐策略：

- ChatGPT：可以允许自动匹配项目工作；
- Codex：`$project-workbench` explicit-only；
- Claude Code：`/project-workbench` explicit-only；
- 普通聊天 / 一次性代码修改不应被治理流程劫持。

## 与 EverOS 联动

Project Continuity 和 EverOS 解决的是不同层：

```text
Source conversations / raw artifacts
                 │
                 ▼
              EverOS
  derived semantic memory / historical clue
                 │
       历史缺口时检索 source clue
                 ▼
         Project Continuity
 current project state / authority / handoff
                 │
                 ▼
       repo / files / live verification
```

**EverOS 不等于 Project Continuity，Project Continuity 也不替代 EverOS。**

- Project Continuity：回答“这个项目现在应该相信什么、下一步是什么”；
- EverOS：回答“过去可能发生过什么、相关来源在哪里”；
- 原始会话 / repo / live state：在需要精确证据时回源。

现有 EverOS 开源 fork：<https://github.com/biaobiao2233/EverOS>

桌面控制台：<https://github.com/biaobiao2233/everos-control-center>

详细边界见 [docs/EVEROS-INTEGRATION.md](docs/EVEROS-INTEGRATION.md)。

## 吸收了哪些项目 / 方法的优点

Project Continuity 不是这些项目的 fork，也没有复制它们的源代码。它吸收的是公开设计思想，再通过自己的跨 Agent dogfood 重新约束。

| 来源 | 吸收的核心思想 | 没有照搬的部分 |
|---|---|---|
| [SpineCodex](https://github.com/GhabiX/SpineCodex) | Work Node lifecycle、closed-node memory、完成阶段退出活跃上下文 | 不 fork Codex；v1 不做 SpineJIT runtime |
| GitHub 工程协作 | Issue、Milestone、PR-style Candidate、required checks、Merge ≠ Release | 不重造完整 Project Board / Bot / Webhook |
| [Orca](https://github.com/stablyai/orca) | authority decomposition、显式 ownership transfer、worktree 物理隔离、无法证明时 fail closed | 不引入 daemon / heartbeat / orchestration DB 作为 v1 前提 |
| EverOS 联动实践 | derived semantic memory 只做历史 clue / source locator | 不把 AI 压缩历史当 raw ground truth 或当前授权 |

完整 prior art 和边界见 [docs/PRIOR_ART.md](docs/PRIOR_ART.md)。

## 已实际验证过什么

公开设计来自真实 dogfood，不是只写了模板：

- fresh ChatGPT 在不读取旧聊天的情况下完成项目接手；
- ChatGPT → Antigravity → ChatGPT bounded handoff + independent review；
- 多会话 `Session Pin vs Primary Focus` 冲突；
- fresh claimant 冒用旧 Logical Session Key 时 fail-closed；
- explicit release → new receiver re-read/accept handoff；
- Codex Project Workbench explicit invocation / anti-ceremony Receiver Eval；
- Reviewer 修改 candidate 会使本轮独立性失效的边界验证。

设计演进见 [docs/EVOLUTION.md](docs/EVOLUTION.md)。

## 未来准备怎么更新

不会为了版本号强行堆功能。路线按真实摩擦触发：

### v1.x — Markdown ergonomics

- 更多真实项目 dogfood；
- Compact Spine 的长期维护收益量化；
- 公共示例与多平台安装说明；
- schema / drift lint，不改变 authority model。

### v2 — Helper / CLI / MCP

只有手工漂移成为稳定问题才做：

- `init / status / validate / handoff / close` helper；
- 自动检查重复 state、stale Handoff、missing review gate；
- Skill adapter 构建与跨平台 core drift 检查；
- 默认仍以 Markdown 为可审计 Source of Truth。

### v3 — Runtime Context Injection / Hooks（实验）

- 根据 Active Node 选择相关 context；
- closed-node memory 的运行时投影；
- 可关闭、可审计、fail-open-to-original-context 的 injection。

### v4 — Optional Local Context Proxy（研究）

- 请求发送前的工具输出去噪 / 上下文压缩；
- passthrough / secret redaction / protocol integrity；
- 不把 HTTPS MITM 作为默认方案。

`Tamp`、`ContextPilot`、`TokenTamer`、`secondwind` 目前只属于 v4 prior-art research，**尚未进入 Project Continuity v1.x 实现**。

详见 [ROADMAP.md](ROADMAP.md)。

## 仓库结构

```text
.
├─ docs/                       协议、模板、治理、并发、prior art
├─ examples/                   可直接复制的示例项目
├─ integrations/               ChatGPT / Codex / Claude Code / generic agent
├─ prompts/                    可选的全局提示词模板
├─ project-workbench/          canonical Skill core
├─ ROADMAP.md
├─ CONTRIBUTING.md
└─ LICENSE
```

## 安全 / 隐私

Project Continuity 文件通常会保存项目状态，因此可能间接暴露：路径、内部架构、服务状态、客户信息或未发布功能。

公开仓库不要提交：

- token / password / OAuth secret / private key；
- 私有生产 endpoint；
- 用户完整聊天历史；
- 未经授权的第三方源码或日志；
- 把 derived memory 当成用户原话的内容。

生产或权限操作永远需要当前授权和 live verification，不能因为 Handoff 写着“可操作”就自动继承授权。

## License

MIT。详见 [LICENSE](LICENSE)。

Prior art 只做设计引用；本仓库没有包含 SpineCodex、Orca 或其它 prior-art 项目的源代码。

