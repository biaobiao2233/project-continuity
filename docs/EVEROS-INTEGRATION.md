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

## 桌面端

配套的 EverOS Control Center 负责：

- EverOS health；
- memory search；
- Markdown memory 浏览；
- sync manifest / runs / progress observability；
- 显式同步操作。

它不应该直接成为 Project Continuity 的 accepted-state database。

未来可以增加**只读 Project Continuity 面板**，显示当前 Project Spine / Handoff / Closure pointers，但写入仍应遵循项目自己的 ownership / review contract。

## Open-source components

- EverOS fork: <https://github.com/biaobiao2233/EverOS>
- Project Continuity: <https://github.com/biaobiao2233/project-continuity>
- EverOS Control Center: <https://github.com/biaobiao2233/everos-control-center>

