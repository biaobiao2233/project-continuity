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

实验方向：

- 按 Active Work Node 选择 relevant context；
- Closed Node 只投影 Closure Memory；
- source pointers 按需展开；
- cross-project related-memory 提示，但默认不把其它项目的 memory 自动注入当前 authority context；
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

### EverOS Control Center 联动

后续可以探索：

- 多项目只读 Project Spine / Handoff 切换；
- EverOS search result → source project / source pointer 回源；
- Project Continuity current state 与 EverOS historical memory 的并排视图；
- 选择性 Closure Memory export / backlink，但每次写入都必须显式、可审计。

Control Center 不成为 Accepted State database；任何写入仍受各项目自己的 ownership / review / verification 规则约束。

