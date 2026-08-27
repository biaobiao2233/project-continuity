# Evolution

公开版不保留所有内部执行流水，只保留影响当前设计的演进节点。

## v1.0 — Project Spine / Work Node / Closure Memory

最初目标：证明一个 fresh Agent 不依赖旧聊天，只读结构化项目状态也能继续。

形成：

- Project Spine；
- Handoff Card；
- Work Node；
- Closure Memory；
- Requirement Anchor；
- Worker Claim / Independent Evidence / Accepted Memory 分层。

关键纠正：derived memory 不等于 raw history / current truth。

## v1.1 — Resume and ergonomics

真实多轮 Review / Repair 暴露：Closed Memory 无法描述“工作做到一半”的物理状态。

新增：

- Current Resume Point；
- Compact Spine；
- execution-round aggregation；
- optional Independent Reviewer Contract；
- 更低噪音的接手 read order。

## Governance extension

借鉴 GitHub collaboration model，增加：

- Feedback / Issue；
- Milestone；
- Candidate Change Packet；
- Required Review Gate；
- Merge / Release boundary。

同时明确：这些是治理辅助，不是新的 truth database。

## Multi-conversation coordination

真实并行会话曾出现：一个会话更新 Primary Focus 后，另一个正在工作的会话被错误路由到新 Node。

因此加入：

- Session Pin；
- Parallel Active Work Registry；
- write ownership / overlap check；
- explicit handoff；
- claimant binding；
- `OWNERSHIP_UNCERTAIN` fail-closed。

后续 prior-art review 又进一步确认：heartbeat、last-sync、terminal/worktree handle 都不能单独证明 completion / ownership。

## Instruction-layer normalization

Project Continuity 规则开始传播到多个 Agent 后，又出现另一个风险：

> global prompt、project instructions、Skill、Project Spine 各复制一整套协议，最终形成 double authority。

因此收敛为：

```text
Global instructions = always-on stable invariants
Project Workbench    = on-demand workflow / procedure
Project Spine        = current project state
coordination.md      = detailed multi-session protocol
repo/live state      = implementation/runtime evidence
```

普通聊天和简单编辑不得被 Project Continuity ceremony 劫持。

## Project Workbench rollout

在 Codex / Claude Code 中采用 explicit-only 作为安全默认：

- Codex: `$project-workbench`
- Claude Code: `/project-workbench`

Receiver dogfood 验证了：

- ordinary task anti-ceremony；
- valid Pin > Project Primary Focus；
- fresh claimant spoof → `OWNERSHIP_UNCERTAIN`；
- explicit release → receiver accept；
- independent reviewer 保持 candidate read-only。

ChatGPT adapter 可以根据产品能力保留 implicit discovery，但 canonical core 不依赖隐式触发。

## EverOS integration

EverOS 被定位为 derived semantic memory / historical clue，而 Project Continuity 负责 current accepted project state。

这使两个系统能够互补：

- Project Continuity 不需要保存所有历史；
- EverOS 不需要承担 current authority；
- exact evidence 有需要时回到 source / repo / live state。

