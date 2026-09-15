# Roadmap

Project Continuity 的路线图按**真实使用摩擦**推进，不以“版本号存在”为开发授权。

## v1.1 — Current baseline

已完成：

- Project Spine / Handoff Card；
- Work Node lifecycle；
- Current Resume Point；
- Closure Memory；
- Requirement Anchor / Semantic Evidence Filtering；
- Worker Claim / Independent Evidence / Accepted Memory 分层；
- GitHub-style lightweight governance；
- Session Pin / claimant binding / write ownership；
- Project Workbench；
- ChatGPT / Codex / Claude Code / generic-agent adapter；
- EverOS derived-memory integration boundary。

## v1.x — Ergonomics and public dogfood

优先：

- 更多可复制示例；
- Compact Spine 长期维护数据；
- public handoff scorecards；
- lint / schema / cross-file drift detection；
- adapter/core drift checks；
- public Skill parity：公开 `project-workbench/` 与当前 accepted package 的 drift 检查；
- 多项目 × EverOS 的真实 dogfood、source-scope 过滤和公开示例；
- 中英文文档完善。

不做：为了自动化而自动化，不新增第二套 accepted-state database。

## v2 — Optional helper / CLI / MCP

仅当“手工维护漂移”在多个真实项目里重复出现时启动。

候选能力：

- `continuity init`
- `continuity status`
- `continuity validate`
- `continuity handoff`
- `continuity close`
- stale Handoff / duplicate state / missing review gate diagnostics
- Project Workbench adapter packaging
- 可选 project index / locator：在很多 Project Spine 之间只读导航
- accepted Closure Memory 的显式、选择性 EverOS export helper（不自动写）

原则：Markdown 仍是人类可读、可审计的 authority surface；helper 不能暗中建立第二套项目真相。

## v3 — Runtime context injection / hooks

这是一个明确的长期方向：**不要把 Project Continuity 的正确使用建立在 Agent 是否愿意主动调用 Skill、主动打开 Project Spine、或是否完全遵循提示词之上。**

当前 v1.x 仍以 Project Workbench Skill 作为工作流入口，但 invocation policy 已允许按 adapter 区分：ChatGPT/OpenAI adapter 可以使用 narrow implicit discovery，Codex / Claude Code 仍可保持显式调用。未来 runtime injection 的目标与“implicit Skill invocation”不同：

```text
session start / project switch / resume
              ↓
     Project Context Compiler
              ↓
Project Spine / Handoff / Active Node
              ↓
     minimal Context Packet
              ↓
 Codex / other Agent / Web client
```

`implicit Skill invocation` 仍然依赖模型自己决定“要不要调用”；这里希望把最小、当前、可验证的项目连续上下文在**模型作出这个决定之前**由 host/runtime/adapter materialize 进去。

实验方向：

- 在 session start、project switch、resume、handoff/closure 后按需刷新当前 Project Context Packet；
- 自动投影 current project identity、Current Goal、Active/Bound Work Node、Next Action、Protected Invariants、Accepted State / candidate boundary、必要的 Session Pin / ownership 状态；
- 按 Active Work Node 选择 relevant context，Closed Node 默认只投影 Closure Memory；
- source pointers 保持为 pointer，只有需要精确证据时再展开；
- 默认只自动注入**当前项目的 authority context**；EverOS / cross-project related memory 仍作为 derived clue，不静默升级为当前项目事实；
- Context Packet 带 revision/hash/source pointers，使接收端能识别 stale context；
- 所有自动注入可见、可关闭、可审计，并能显示“本轮实际注入了什么”；
- injection 失败时安全回退到原始上下文，不伪造 continuity state，也不静默删掉用户/系统关键上下文；
- ownership / claimant 不确定时，注入 `OWNERSHIP_UNCERTAIN` / read-only 边界，而不是因为自动化而自动授予写权。

### Target adapters

- **Codex CLI / Desktop**：优先研究 launcher / hook / runtime adapter，在新任务进入模型前 materialize Project Context Packet；
- **Claude Code / OpenCode / Antigravity / generic coding agents**：通过各自可用的 hook、plugin、MCP host 或 launcher 接入同一 compiler contract；
- **Web AI / ChatGPT Web 等网页版客户端**：目标同样是不要求用户每次提醒“先读账本”。如果平台没有原生 pre-turn context hook，则研究 browser/local companion 或平台允许的 project/system-context adapter；具体实现取决于平台能力，不能把尚不存在的接口写成已完成能力。

### Design driver

真实使用中，Agent 的工具调用积极性和指令遵循并不稳定。Project Continuity 的长期可靠性不能依赖“模型这次刚好想起来读文件”。因此 v3 的验收重点不是更炫的自动化，而是：**一个低主动性 Agent 也能在开始工作前被动获得正确的最小项目上下文。**

## v4 — Optional local context proxy

研究请求发送前的上下文处理：

- tool result 去噪；
- closed history replacement；
- secret redaction；
- request protocol integrity；
- transparent passthrough；
- local-only memory boundary。

Prior-art research candidates：

- <https://github.com/sliday/tamp>
- <https://github.com/msousa202/ContextPilot>
- <https://github.com/borhen68/TokenTamer>
- <https://github.com/orchetron/secondwind>

这些项目目前只是研究入口，**不代表其实现已进入 Project Continuity**。

## EverOS / Project Continuity convergence

长期希望形成清晰的四层：

```text
Raw Sources
   ↓
EverOS — derived long-term semantic memory / retrieval
   ↓
Project Continuity — current accepted project state / handoff
   ↓
Optional Runtime Context Compiler — session-time materialization
```

任何自动同步都必须保留 provenance：EverOS memory 不能自动晋升为 Accepted Memory；Project Continuity 的 accepted state 也不应该把完整项目流水反向灌入 EverOS。

### EverOS Control Center 联动

后续可以探索：

- 多项目只读 Project Spine / Handoff 切换；
- EverOS search result → source project / source pointer 回源；
- Project Continuity current state 与 EverOS historical memory 的并排视图；
- 选择性 Closure Memory export / backlink，但每次写入都必须显式、可审计。

Control Center 不成为 Accepted State database；任何写入仍受各项目自己的 ownership / review / verification 规则约束。

