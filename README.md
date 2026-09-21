# Project Continuity

**让一个没参与旧聊天的 AI Agent，不重放完整历史，也能安全、准确地接手长期项目。**

[English](README.en.md) · [当前实用系统](docs/CURRENT-SYSTEM.zh-CN.md) · [Agent 安装/迁移](docs/AGENT-SETUP.zh-CN.md) · [规范](docs/SPECIFICATION.zh-CN.md) · [模板](docs/TEMPLATES.md) · [多会话协调](docs/COORDINATION.zh-CN.md) · [EverOS / 多项目联动](docs/EVEROS-INTEGRATION.md) · [路线图](ROADMAP.md)

Project Continuity 是一套面向 ChatGPT、Codex、Claude Code、Antigravity、OpenCode 等 Agent 的**跨会话 / 跨 Agent 项目连续记忆协议**。

它不是聊天记录归档器，也不是向量数据库。它只解决三个问题：

> **现在要记什么？什么能信？下一个 Agent 怎么继续？**

当前公开基线：**Project Continuity v1.1 稳定协议 + Project Workbench `2.0.0-rc.3` 预发布候选**。RC 已通过 50 项本地测试，并把 Codex / OpenCode / ZCode / Antigravity / Claude 的统一 Skill + 全局提示词安装迁移流程正式纳入仓库；fresh receiver 的模型行为仍是独立验收门。详见 [v2.0.0-rc.3 release notes](docs/release-notes-v2.0.0-rc.3.md)。

> 这不是一份只用于介绍想法的概念稿。仓库内 `project-workbench/` 现在公开的是 **2.0.0-rc.3 完整候选源码、测试、示例、跨 Agent 安装脚本、全局提示词源与配套提示词**；它来自本地已验证候选，但不把“文件已写入”或“catalog 可见”写成模型行为已经验收。真实项目的私有 Spine、worklogs、聊天和凭据不会被打包公开。详见 [当前实用系统](docs/CURRENT-SYSTEM.zh-CN.md)。

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

### 授权、当前观测与验收分开

不要再把三种不同问题塞进一条“可信度排序”：

- **允许做什么**：看当前用户授权、任务 scope、权限与仓库策略；
- **现在实际是什么**：看当前 repo / files / tests / process / endpoint / live observations；
- **哪一版曾经通过验收**：看绑定到准确 source/artifact、环境和 required evidence 的验收记录。

因此遇到漂移时应表达为：

```text
A was accepted
B is running now
B has not been accepted yet
```

而不是让历史 PASS 覆盖当前运行事实，也不是让当前运行版本自动继承旧 PASS。

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
GitHub Issue / task
→ short-lived branch / worktree
→ implementation + focused checks
→ PR / candidate-bound review
→ early integration
→ Merge
→ Staging / Release Gate
→ compact handoff / Closure Memory

Work Node 只在执行连续性真的有帮助时补充，不复制完整 GitHub Issue
```

简单修改就保持简单；持续项目也只使用达到正确性与可恢复性所需的最小治理层级。

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

当前 invocation policy 按平台 adapter 区分：

- checked-in ChatGPT/OpenAI adapter：**narrow implicit discovery**，`allow_implicit_invocation: true`；只匹配持续/可恢复项目、handoff、continuity、live-state、GitHub governance 或多 Agent 协作；
- Codex：默认 `$project-workbench` 显式调用；
- Claude Code：默认 `/project-workbench` 显式调用；
- ordinary chat、简单代码问题、一次性低风险修改和不需要连续性/治理的独立 review 不应被完整 Workbench ceremony 劫持。

平台中立全局规则模板见 `prompts/global-guidance.zh-CN.md`；当前 ChatGPT dogfood 的可直接粘贴用户级版本见 `prompts/chatgpt-custom-instructions.zh-CN.md`。

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

更重要的是，EverOS 让**多个彼此独立的项目共享历史经验，而不是共享当前 authority**：

```text
Project A source history ─┐
Project B source history ─┼──► EverOS shared historical index
Project C source history ─┘              ▲
                                         │ semantic search
Current Agent ─► Project B Spine ────────┘
                     │
                     ▼
             source / repo verify
                     │
                     ▼
           only update Project B state
```

因此一个项目里踩过的坑、做过的实验、设计取舍可以被另一个项目找到并复用；但 Project A 的 `PASS`、production state、authorization 或 owner **不会自动传播**给 Project B。

现有 EverOS 开源 fork：<https://github.com/biaobiao2233/EverOS>

桌面控制台：<https://github.com/biaobiao2233/everos-control-center>

完整联动效果、跨项目例子和 authority 边界见 [docs/EVEROS-INTEGRATION.md](docs/EVEROS-INTEGRATION.md)。

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

### v2 — Team workflow + read-only checker（当前 RC）

`2.0.0-rc.1` 已把真实使用中反复出现的摩擦收进候选：

- 长期方向（Lane）与短期可交付任务分开；conversation/Agent 是可替换执行者；
- GitHub Issue / PR / native dependency 作为工程账本，本地只保留 GitHub 不擅长的执行绑定；
- 先约定 versioned interface contract，再并行实现并尽早集成；
- 分别检查 source workspace、runtime resource、live target，worktree 不被误当成生产资源锁；
- review / integration / deployment evidence 绑定准确 candidate 和 environment；
- `resume / preflight / deliver / integrate` 只读 checker 只检查输入快照，不联网、不自动合并、不部署、不授予权限；
- record sync 失败时显式保留 `RECORD_SYNC_PENDING`，不为了补账重复部署。

当前 RC 的真实边界：47 项本地测试通过；尚未把 fresh receiver、真实 GitHub hosted workflow 或生产设备当作“已验收”。后续是否升 stable 由实际 receiver dogfood 决定。

### v3 — Runtime Context Injection / Hooks（实验）

- 长期目标是不再依赖 Agent 主动调用 Skill / 主动读取 Project Spine；
- 由 host/runtime/adapter 在模型开始工作前自动 materialize 当前项目的最小 Project Context Packet；
- 根据 Active Node 选择相关 context，closed-node memory 只投影 Closure Memory；
- 优先覆盖 Codex，并设计可复用到 Claude Code / OpenCode / Antigravity / generic Agent；网页版 AI 在平台能力允许时通过 native hook 或 browser/local companion 接入；
- 自动注入只携带当前项目的 authority context；EverOS / 跨项目 memory 默认仍是 derived clue，不自动晋升为当前事实；
- injection 可见、可关闭、可审计，并 fail-open-to-original-context。

这里的 **automatic context feed 不等于 implicit Skill invocation**：implicit Skill 仍要靠模型主动决定调用，而 v3 目标是在模型做这个决定之前就把最小正确项目上下文送进去。这个方向受到 SpineCodex runtime context management 的启发，但 Project Continuity 不要求 fork Codex，也不把 SpineJIT 作为前提。

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
├─ prompts/                    可选的全局提示词 / ChatGPT 用户级绑定
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

