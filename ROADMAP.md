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

原则：Markdown 仍是人类可读、可审计的 authority surface；helper 不能暗中建立第二套项目真相。

## v3 — Runtime context injection / hooks

实验方向：

- 按 Active Work Node 选择 relevant context；
- Closed Node 只投影 Closure Memory；
- source pointers 按需展开；
- 所有自动注入可见、可关闭、可审计；
- injection 失败时安全回退，不静默删掉用户/系统关键上下文。

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

