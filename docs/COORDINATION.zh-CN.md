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
- **假 takeover**：把 stale timestamp 当 ownership release；
- **claim spoofing**：fresh conversation 冒用旧 Session Key；
- **reviewer pollution**：Reviewer 修改 candidate 后仍自称 independent；
- **registry as truth**：把 coordination view 当 lifecycle authority。

安全默认都是：先读、先验证、ownership 不清楚就不写。

