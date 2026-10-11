# Multi-Conversation Coordination

当同一项目存在多个 ChatGPT / Codex / Claude Code / Antigravity 会话时，Project Continuity 使用轻量 Session Pin / ownership 协议，避免“另一个会话更新了项目焦点，我这边就被带跑”。

## 核心对象

### Primary Project Focus

项目级主要推进方向，只是 routing hint，不是所有会话必须立即切换的命令。

### Session Pin

长期/实质性会话可以绑定：

```text
Session key:
Client / Agent:
Bound Work Node:
Role:
Write scope:
Worktree / project path:
State: ACTIVE | PAUSED | OWNERSHIP_UNCERTAIN | RELEASED
Last sync:
Next action:
```

保持：

```text
Session Pin != Work Node Status != Accepted State
```

## Routing order

恢复时按：

```text
当前用户明确任务 / switch
→ 当前会话 valid Session Pin
→ Pin 对应 Work Node 当前 state / ownership
→ Project Primary Focus / Registry
→ fresh + unpinned session default
```

因此 valid Pin 不会因为另一个会话修改 Project Primary Focus 而自动失效。

## Logical Session Key / claimant binding

Logical Session Key 是 coordination identity，不是 cryptographic identity。

规则：

- single allocation / no silent reuse；
- fresh/cold conversation 默认使用新 key；
- 知道旧 key、复制旧 Prompt、看到 Registry row、自称“我是 SESSION-A”，都不足以证明自己就是原 claimant；
- claimant continuity 无法证明或 duplicate claim 时进入 `OWNERSHIP_UNCERTAIN`；
- 相关 shared/candidate writes fail-closed 为 read-only。

## Write ownership

每个 ACTIVE session 声明最小 write scope。

1. scope 重叠：默认串行；
2. 代码并行：优先不同 branch/worktree；
3. Project Spine / issue register / release pointer 等中央面：single-writer/coordinator-owned 为默认；
4. 中央写入必须 read-before-write + narrow patch；
5. context mismatch：重新读取/合并，禁止 stale snapshot 整文件覆盖；
6. Reviewer / Verifier 默认只读 candidate。

## Full handoff

新会话出现、Primary Focus 改变、Last sync 更新、旧 owner 暂时无响应，都**不等于 ownership transfer**。

Full handoff 需要：

```text
original owner explicit release / transfer
→ receiver re-read current state
→ receiver explicitly accepts bounded scope
```

若 ownership 既无法证明仍有效，也无法证明已 handoff：`OWNERSHIP_UNCERTAIN` + read-only。

Cloud Queue claim 的释放和过期见下一节。这里的 `Last sync` 或“暂时无响应”不能直接当成 claim 过期。

## Cloud Queue：难度、自选与接手

`D1` / `D2` / `D3` 是可领取任务的工作量标签，不是 L0–L3 风险层级。Coordinator 发任务时打 GitHub label `difficulty:D1`、`difficulty:D2` 或 `difficulty:D3`，并在正文写 `Difficulty:`。两处必须一致。Label 里不写厂商或模型名。

Worker 按自己剩余的上下文、额度、工具和沙箱选择或放弃任务。放弃就是不发 CLAIM。这是建议，不是厂商/模型排名，也不改变 earliest-valid-CLAIM-wins。

CLAIM 必填 `Role` / `Session` / `Scope`。可选 `Difficulty-fit` 和 `Capability note`。接管旧 claim 时写明 `Takeover`。

Coordinator 和 Worker 都可替换。新 Agent 读同一份 Handoff 和 active Issue/PR 即可继续，不重放聊天。

- **释放**：当前 claimant 还能写时，在 Issue 上发 `RESULT`，`Status: BLOCKED`，`Claim: RELEASED`，并留下 resume point。额度或上下文用尽优先走这条，不要靠猜超时。
- **主人改派**：当前用户明确让本会话接手时，新 CLAIM 写 `Takeover: owner reassignment`。聊天本身不会被下一个 Agent 看见。
- **过期**：只按 Handoff 里的 `Claim staleness`，用该 claimant 在 GitHub 上可见的评论、commit 或 check 判断。别人的评论不刷新这个 claim。项目可写窗口（如 `72h`），或 `explicit release only`。字段空着时用 Skill 默认：72 小时没有该 claim 的可见证据；接手 CLAIM 必须写明用了这条默认。
- **无法证明**：看不出已释放、已改派，也证明不了过期规则已经满足 → `OWNERSHIP_UNCERTAIN`，shared/candidate 只读，询问人。

`Last sync`、聊天停更、额度猜测，都不是 release。

接手者重读当前状态后另发一条新 CLAIM，使用新的 Session key，不复用旧 key。最早的有效 CLAIM 仍然赢。无效的抢占 claim 不会压过仍有效的旧 claim。

Worker 接手不会自动变成 Coordinator。谁可以做 Coordinator 写在项目 Handoff 的 `Coordinator hosts`（主人允许的 host，或能力类别）。Skill 不写死厂商或模型名。字段空着时，任何 Agent 都可以在旧 coordinator claim 已释放、已改派或已过期之后发 `Role: Coordinator` 的新 CLAIM；空着不等于每个 Worker 自动继承中央权限。字段写了但本 host 对不上，或对不上还是不确定，就不要做中央写入，按 `OWNERSHIP_UNCERTAIN` 询问人。Coordinator 失联本身不把部署或中央写入权发给每一个 Worker。

细则以 canonical Skill 的 `project-workbench/references/cloud-queue.md` 为准。

## Parallel Active Work Registry

只有真实并行工作需要时才启用一个 live Registry：

```markdown
| Session | Bound Node | Role | Write scope | State | Last sync | Next action |
|---|---|---|---|---|---|---|
| CHAT-A | NODE-A | Primary | src/a + node-a.md | ACTIVE | ... | ... |
| CODEX-B | NODE-B | Implementer | worktree-b | ACTIVE | ... | ... |
```

Registry 只是 coordination view：

- Work Node 真相仍在 Work Node；
- Issue 真相仍在 Issue；
- Accepted State 仍由 acceptance 决定。

不要维护两份 live Registry。

## Heartbeat boundary

v1.1 不引入 heartbeat / daemon / lock server。

`Last sync` 只说明最后自然检查点，不等于：

- completion；
- ownership release；
- PASS；
- takeover authorization。

未来即使平台提供 liveness event，也只能作为 evidence，不能自动驱动 accepted state。

## Failure modes

- **串台**：global focus 覆盖 session-local Pin；
- **双写**：两个会话同时写同一 candidate/working tree；
- **假 takeover**：把 Session Pin 的 stale timestamp、聊天停更或额度猜测当 ownership release；Cloud Queue 只有明确释放、当前用户改派，或项目 staleness 规则已被 GitHub 证据证明时才可接手；
- **claim spoofing**：fresh conversation 冒用旧 Session Key；
- **reviewer pollution**：Reviewer 修改 candidate 后仍自称 independent；
- **registry as truth**：把 coordination view 当 lifecycle authority。

安全默认都是：先读、先验证、ownership 不清楚就不写。

