# Project Continuity v1.1 — Specification

## 1. 目标

让一个没有参与此前对话的 Agent，只读取项目连续记忆，就能安全、准确地接手项目，而不要求用户重新讲一遍历史，也不要求新 Agent 重读完整聊天流水。

v1.1 只解决：

1. **记什么**；
2. **信什么**；
3. **怎么交接**。

不要求数据库、Hook、向量检索、网络代理或自动 token 压缩。

## 2. 核心术语

```text
Project Continuity  整套跨 Agent 项目连续记忆方法
Project Spine       一个项目的稳定入口 / 当前状态骨架
Handoff Card        当前交接面
Work Node           可独立推进、验收、收口的工作单元
Current Resume Point 未关闭 Node 的物理执行边界
Closure Memory      已关闭 Work Node 留给未来工作的压缩记忆
Requirement Anchor  长期重要用户需求的稳定引用
Session Pin         会话级临时路由 / ownership 协调元数据
```

## 3. 信息层分工

### Source Conversations / Raw Artifacts

最接近原始证据：原始会话、文件、git history、测试 artifact、live state。

### Derived historical memory

例如 EverOS。适合语义检索、历史 clue、source locating；不自动承担当前事实、验收、授权或 raw audit。

### Project Continuity

当前连续状态层，保存当前需求、项目状态、Work Node、关键发现、踩坑、不变量、验收和 Closure Memory。

### Repository documentation

实现本身的长期技术真相继续放在 README / DESIGN / ADR / docs / code 中。Project Continuity 链接它们，不复制第二份完整版。

### Live state

动态版本、生产服务、网络、价格、运行进程等必须在操作前重新 live verify。

## 4. Authority / Provenance

默认证据顺序：

```text
1. 当前用户明确意图 / 授权
2. independently verified Accepted Project State
3. repo / files / tests / live reproducible evidence
4. Worker Claim / executor report
5. Agent summary / inference
6. derived historical memory / clue
```

必须保持：

```text
User Evidence
!= Worker Claim
!= Independent Evidence
!= Accepted Memory
```

Worker 报告 `COMPLETE` 不自动等于 PASS。

## 5. Project Spine

推荐结构：

```text
Project Spine
├─ Handoff Card
├─ Current Resume Point（in-flight 时）
├─ Current Requirements
├─ Requirement Anchors / Source refs
├─ Protected Invariants
├─ Work Node Index
├─ Major Discoveries
├─ Major Pitfalls
├─ Verification State
├─ Closure Memory Index
├─ Open Questions / Blockers
└─ Related Docs / Sources
```

长期项目建议最多两层：

```text
projects/<project>/README.md
projects/<project>/worklogs/<work-node>.md
```

小项目可以使用 Compact Spine，把少量 Active Work Node 和 Closure Memory 内嵌在 README。

## 6. Handoff Card

推荐保持紧凑：

```text
Current goal:
Active node:
Accepted predecessors:
Current state:
Verification state:
Resume point:
Next action:
Blockers:
Protected invariants:
Project path:
Critical files:
Relevant Closure Memories:
last_verified_at:
```

它是可重写的**当前状态面**，不是历史日志。

## 7. Current Resume Point

未关闭 Node 在 pause / handoff 前记录：

```text
Last completed action:
Current physical state:
Last verification:
In-flight issue:
Safe next action:
Do NOT repeat:
```

只记录当前执行边界。Node 关闭后由 Closure Memory 取代。

## 8. Semantic Evidence Filtering

消息角色 `user` 不代表整段文本都是用户原创需求。

例如用户说“帮我验一下这个”，后面粘贴 9000 字 Worker 报告：

- “帮我验一下这个” = User Intent；
- Worker 报告 = execution/context payload。

长期 User Evidence 只保留真正的目标、约束、优先级、纠正、决策和验收条件。

## 9. Requirement Anchor

只对跨多个 Work Node 仍需精确引用的重要需求建立稳定 anchor。

不要为了“结构完整”给所有普通需求编号。

## 10. Work Node

Work Node 应能独立：

1. 定义目标；
2. 推进；
3. 验收 / 拒绝 / 阻塞；
4. 收口；
5. 完成后让详细过程退出正常恢复路径。

不要因为日期、换对话、换 Agent、发新 Prompt 或改了几个文件就自动新建 Node。

推荐 Node Contract：

```text
Objective:
Owned Scope:
Out of Scope:
Acceptance Criteria:
Protected Invariants:
Dependencies:
Blockers:
Next Action:
```

## 11. 状态

统一使用：

```text
NOT_STARTED
IN_PROGRESS
CANDIDATE
PASS
FAIL
BLOCKED
SUPERSEDED
```

- `CANDIDATE`：实现已形成，但 required acceptance 仍未完成；
- `PASS`：满足任务定义的 acceptance gate；
- `SUPERSEDED`：历史结论被新证据/设计替代，必须保留原因和 replacement。

## 12. Closure Memory

关闭后的 compact continuation memory：

```text
Final status:
Closed at:
Goal:
Accepted outcome:
Durable capabilities:
Inherited user requirements:
Protected invariants:
Major discoveries:
Major pitfalls:
Verification evidence:
Remaining risks:
What future work may assume:
What future work must NOT assume:
Source / evidence links:
```

验收标准：一个没参与该阶段的 Agent 只读 Closure Memory + 当前需求，能否安全进入下一阶段？

## 13. Closed Memory Integrity

Accepted Closure Memory 近似不可变。

旧结论失效时：

```text
PASS — <old date>
SUPERSEDED — <new date>
Reason: ...
Replacement: ...
```

不要把历史改写成“从来没错过”。

## 14. Discoveries / Pitfalls

Discoveries 只记录未来可复用的发现：

```text
Finding:
Evidence:
Impact:
Reuse:
Verification status:
```

Pitfalls 应产生长期保护：

```text
Pitfall:
Root cause:
Consequence:
Permanent rule:
Regression protection:
```

## 15. Execution Record

按有独立意义的执行轮次记录，不为每个命令生成历史条目：

```text
Executor:
Purpose:
Owned scope:
Source conversation/task:
Worker claimed result:
Important findings:
Changed files/artifacts:
Independent verification:
Accepted verdict:
Next action:
```

完整日志留在 source conversation / artifact / CI / repo。

## 16. Cross-Agent Handoff Read Order

接手时按需读取：

1. Handoff Card；
2. Current Resume Point；
3. Current Requirements；
4. Protected Invariants；
5. Active Work Node；
6. relevant predecessor Closure Memory；
7. Blockers / Next Action；
8. repository / files / live evidence。

历史仍不足时再升级：

```text
Project Continuity
  ↓ insufficient
derived historical memory (e.g. EverOS)
  ↓ source clue
source conversation / artifact
  ↓ if current fact
live verification
```

## 17. Independent Review

只有 Node / task contract 要求时才强制 independent review；普通低风险修改不机械升级流程。

Reviewer 必须：

- 重新读取当前 candidate / diff / evidence；
- 默认只读；
- 可以返回否定 verdict；
- 一旦修改 candidate，本轮 independent review 终止。

## 18. Repository / production boundary

保持：

```text
Accepted/Merged Source
!= Staging Accepted
!= Production Released
```

生产操作需要当前明确授权和 live verification，不从旧 Handoff 或历史 memory 自动继承。

## 19. v1.1 不要求的东西

- SQLite / vector DB；
- background daemon；
- heartbeat；
- automatic context injection；
- network proxy / MITM；
- automatic deletion of conversation context。

这些能力不属于 v1.1 acceptance baseline。

其中 `automatic context injection` 已因真实 dogfood 中的 Agent 工具调用积极性 / 指令遵循差异，被记录为 v3 的明确研究方向：目标是在 Agent 主动调用 Skill 或主动读取 Project Spine **之前**，由 host/runtime/adapter 提供当前项目的最小 Project Context Packet。它仍需独立设计、实现和验证，不能因为写入 roadmap 就倒推为 v1.1 已有能力。

