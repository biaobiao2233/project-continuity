# EverOS × Project Continuity

Project Continuity 与 EverOS 是互补层，不是二选一。

## 分层

```text
Raw sources
  conversations / artifacts / repo / logs
            │
            ▼
          EverOS
 derived semantic memory / historical index
            │
     semantic clue / source locator
            ▼
     Project Continuity
 current accepted project state / handoff
            │
            ▼
 repo / files / tests / live verification
```

## EverOS 适合保存 / 提炼

- 跨应用历史线索；
- 可复用事实和长期偏好；
- 历史会话语义索引；
- source app / session / artifact pointer；
- “以前为什么这么做”的检索入口。

## Project Continuity 适合保存

- 当前有效需求；
- 当前 Work Node；
- 当前 Next Action；
- accepted / candidate / blocked 状态；
- Protected Invariants；
- Closure Memory；
- ownership / handoff 边界；
- independent review / acceptance state。

## 不能自动互相升级

### EverOS → Project Continuity

EverOS 返回的 memory 默认是 **derived evidence**。

它可以帮助找到：

- 相关旧决策；
- source conversation；
- repo / artifact；
- 可能的历史 requirement。

但不能只凭一个 memory summary 就自动写成：

- 当前用户授权；
- PASS；
- production state；
- exact requirement wording。

关键内容必须回源或 live verify。

### Project Continuity → EverOS

也不要把每次 Prompt、每个 tool result、每条 Resume Point 全量同步到 EverOS。

更适合进入长期 memory 的是：

- durable requirement；
- accepted Closure Memory；
- 重大 discovery；
- 重大 pitfall；
- 稳定 source pointer。

## 推荐检索流程

```text
Project Spine / Active Work Node
        ↓ insufficient history
EverOS semantic search
        ↓ source clue
source conversation / artifact
        ↓ current fact?
repo / live verification
```

## 多项目联动：共享历史，不共享当前真相

Project Continuity 是 **per-project authority layer**。每个项目拥有自己的 Project Spine、Work Node、Handoff、Closure Memory 和 acceptance state。

EverOS 则可以作为多个项目共同使用的 derived historical layer：不同 Agent / 会话 / 项目的历史被语义索引后，当前项目在需要时可以检索其它项目曾经出现过的相关经验。

```text
Project A source sessions ─┐
Project B source sessions ─┼────► EverOS
Project C source sessions ─┘   shared derived historical index
                                      ▲
                                      │ semantic search
                                      │
Current Agent ──► Project B Spine ────┘
                     │
                     │ source clue found in A / old B
                     ▼
              source / artifact / repo
                     │
                     ▼
              verify for Project B
                     │
                     ▼
             record Project B outcome
```

这带来的联动效果是：

- **跨项目经验复用**：另一个项目已经踩过的坑、做过的实验、采用过的设计，可以被当前 Agent 找到；
- **跨 Agent 连续性**：历史可能来自 ChatGPT、Codex、Claude、Antigravity、OpenCode 等不同来源，不要求当前 Agent 参与过旧会话；
- **减少重复研究**：Project Spine 没必要复制其它项目的大段 Closure，只需在历史不足时通过 EverOS 找 source clue；
- **保持项目隔离**：Project A 的 `PASS`、production state、authorization、owner 不会自动成为 Project B 的事实；
- **保留可追溯性**：关键决策最终仍回到 source conversation / artifact / repo / live evidence，而不是引用一条 AI 摘要结束验证。

### 一个典型例子

假设 Project A 曾经解决过一个 Windows updater 的 rollback 问题，并留下 source pointer；几周后 Project B 遇到相似更新失败。

Project B 的 Receiver 正常先读取自己的 Project Spine。若本项目没有足够历史，再通过 EverOS 搜索 rollback / updater 相关历史，可能找到 Project A 的旧案例。

正确做法是：

```text
EverOS 找到 Project A 相关历史
→ 定位旧 source / artifact
→ 理解当时为什么这样修
→ 检查 Project B 当前代码 / 约束 / live state
→ 只把适用于 B 的结论写入 B 的 Work Node / Closure
```

错误做法是：

```text
Project A = PASS
→ 推断 Project B 同样 PASS
```

或者：

```text
EverOS summary 说“可以上线”
→ 当成 Project B 的当前发布授权
```

### Project linkage ≠ state merge

这里的“项目之间联动”是 **knowledge transfer / historical retrieval**，不是把多个 Project Spine 合并成一个全局状态机。

每个项目继续独立维护：

- Current Requirements；
- Protected Invariants；
- Active Work Node；
- Candidate / PASS / FAIL；
- write ownership；
- release / production state。

EverOS 负责让这些项目背后的历史经验彼此可发现。

## 桌面端

配套的 EverOS Control Center 当前提供这些界面，但完成度并不相同：

- **显式同步操作 / sync manifest / progress：目前主要可用、完成度最高的部分；**
- EverOS health：基础状态查看；
- memory search：仍属实验性界面；
- Markdown memory / “记忆原件”：目前非常粗糙，排版、导航、信息层级和长文本可读性都不足，暂时更接近开发/诊断视图；
- pipeline / runs：主要用于可观测与诊断，还不是成熟的普通用户工作台。

因此当前不要把 Control Center 描述成“所有 EverOS 记忆能力都已经日常可用”的完整 GUI。**现阶段真正正常、优先保证体验的是同步页，其它页面更多是在验证数据链路和未来交互方向。**

它不应该直接成为 Project Continuity 的 accepted-state database。

未来可以增加**只读 Project Continuity 面板**，显示当前 Project Spine / Handoff / Closure pointers，但写入仍应遵循项目自己的 ownership / review contract。

后续可以继续探索：

- Control Center 中的多项目只读 Project Spine / Handoff 切换；
- EverOS search result → source project / source pointer 的一键回源；
- accepted Closure Memory 的显式、选择性记忆导出；
- cross-project related-memory 提示，但默认不自动注入当前 context；
- Project Workbench 对 project identity / source scope 的更强过滤，避免跨项目召回污染。

这些都必须继续满足一个原则：**跨项目可以共享知识线索，但不能静默共享 authority。**

## Open-source components

- EverOS fork: <https://github.com/biaobiao2233/EverOS>
- Project Continuity: <https://github.com/biaobiao2233/project-continuity>
- EverOS Control Center: <https://github.com/biaobiao2233/everos-control-center>

