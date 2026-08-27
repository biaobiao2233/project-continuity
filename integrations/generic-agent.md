# Generic Agent / Antigravity / OpenCode

任何能读取 Markdown / repo 文件的 Agent 都可以使用 Project Continuity，不要求专用 runtime。

最小接手 Prompt：

```text
这是一个已有 Project Continuity 的项目。

先读取项目的 Project Spine，并按当前 Handoff / Work Node 恢复真实状态。
不要依赖旧聊天猜当前版本、Accepted State 或 ownership。

按需读取：
1. Handoff Card
2. Current Resume Point
3. Current Requirements / Protected Invariants
4. Bound/Active Work Node
5. Relevant Closure Memory
6. repo/files/live evidence

如果历史仍不足，再使用可用的 derived memory（例如 EverOS）找 source clue，关键事实继续回源。
```

如果该 Agent 会写代码或共享文件，还应遵守 Session Pin / write ownership / overlap isolation 规则。

