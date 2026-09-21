# Project Workbench：给 Codex / OpenCode / Antigravity / ZCode / Claude 的统一安装流程

这份文档的目标很直接：**以后换一个全新的对话，把这个仓库丢给它，它就知道怎么把 Project Workbench Skill 和配套提示词恢复到我的几个 Agent。**

不要靠旧聊天记忆，也不要从某个平台现有文件反向复制。以本仓库当前版本为源，先检查现场，再安装。

## 1. 架构：一个 Skill，五个平台提示词

唯一 Skill 权威副本：

```text
~/.agents/skills/project-workbench
```

统一提示词源：

```text
~/.agents/guidance/
├─ project-workbench-v2-core.md
└─ adapters/
   ├─ codex.md
   ├─ opencode.md
   ├─ zcode.md
   ├─ antigravity.md
   └─ claude.md
```

对应平台生成文件：

| Agent | 全局提示词入口 | Skill |
|---|---|---|
| Codex | `~/.codex/AGENTS.md` | 共享 `~/.agents/skills/project-workbench` |
| OpenCode | `~/.config/opencode/AGENTS.md` | 原生发现共享 `.agents/skills` |
| ZCode | `~/.zcode/AGENTS.md` | 当前用户方案继续使用共享 `.agents/skills` |
| Antigravity / Gemini | `~/.gemini/GEMINI.md` | 两个 native 入口链接到共享 Skill |
| Claude Code | `~/.claude/CLAUDE.md` | 先验证当前版本是否发现 Skill；不要凭其它 Agent 的状态猜 |
| ChatGPT | ChatGPT 账号的个性化 / Custom Instructions | Skill 安装与账号设置是两个独立动作 |

Antigravity 当前约定的 native Skill 入口：

```text
~/.gemini/config/skills/project-workbench
~/.gemini/antigravity-cli/skills/project-workbench
```

它们只应该是 junction/symlink，目标都指向：

```text
~/.agents/skills/project-workbench
```

**不要维护第二份字节副本。**

## 2. 新 Agent 接手时怎么做

### 第一步：先检查，不要直接覆盖

确认：

- 仓库当前 `project-workbench/VERSION`；
- `~/.agents/skills/project-workbench` 是否存在、版本是什么；
- 五个平台全局提示词是否存在；
- Antigravity 的两个 native 入口是链接还是旧副本；
- OpenCode 当前版本与 `opencode debug skill` 结果；
- 当前工作区根目录的 `AGENTS.md / GEMINI.md / CLAUDE.md` 是否还残留会覆盖全局规则的旧流程。

项目级规则可以更具体，但不应重新复制一套旧 Project Continuity 生命周期。

### 第二步：先 dry-run

从本仓库根目录执行：

```powershell
python project-workbench/scripts/install_agent_setup.py
```

默认只打印计划，不写文件。

如果 `--apply` 时发现某个平台现有全局提示词不是本工具生成的 managed 文件，脚本会拒绝覆盖；先人工检查，确认要接管后才使用 `--force-guidance`。Antigravity native Skill 入口如果是实际目录而不是 link，同样会拒绝删除；确认旧副本已备份且应该淘汰后才使用 `--force-links`。

### 第三步：用户已经明确授权后再应用

```powershell
python project-workbench/scripts/install_agent_setup.py --apply --link-antigravity
```

脚本会：

1. 把仓库里的 `project-workbench/` 安装到共享 Skill 权威目录；
2. 把 `assets/global-guidance/` 同步到 `~/.agents/guidance/`；
3. 生成 Codex / OpenCode / ZCode / Antigravity / Claude 的全局提示词；
4. 在 Windows 上为 Antigravity 创建 junction，在类 Unix 系统创建 symlink；
5. 替换前备份旧文件/旧目录；
6. 不碰 provider 凭据、模型设置、MCP 密钥、ChatGPT 账号设置或任何生产服务。

备份默认进入：

```text
~/.agents/backups/project-workbench-agent-setup/<timestamp>/
```

### 只同步提示词

Skill 已经正确，只想重新生成五个平台提示词：

```powershell
python project-workbench/scripts/install_agent_setup.py --apply --guidance-only
```

### 不创建 Antigravity native links

省略 `--link-antigravity` 即可。

## 3. 平台验证

### OpenCode

```powershell
opencode --version
opencode debug paths
opencode debug skill
```

必须能在 Skill catalog 中看到 `project-workbench`，location 指向 `~/.agents/skills/project-workbench/SKILL.md`。

如果 catalog 已经找到 Skill，但 `opencode run` 超时，要区分 provider/runtime 超时和 Skill discovery 失败，不要混为一谈。

### Antigravity / Gemini

检查两个 native 入口是否解析到同一个共享目录，并确认共享目录的 `VERSION`。运行中的旧会话可能已经 snapshot Skill catalog，所以文件正确后仍需要一个 fresh receiver。

### Codex / ZCode / Claude

检查对应全局提示词已经生成，再用新会话做 receiver 验证。**不要因为文件存在就声称 Agent 已经加载。**

Claude Code 尤其要先看当前版本实际 Skill discovery；如果需要 native Skill 路径，应创建指向共享权威目录的链接，而不是复制一份再长期手改。

## 4. ChatGPT

ChatGPT 的配套中文提示词在：

```text
project-workbench/assets/personalization-v2.txt
project-workbench/assets/personalization-v2-compact.txt
```

这是账号级 UI 设置，不属于本地安装脚本的权限范围。不要把“文件已生成”写成“ChatGPT 个性化已应用”。

## 5. 更新 Project Workbench 时

以后仓库发布新版本时：

1. 读 release notes；
2. 备份当前共享 Skill；
3. 从仓库更新 `~/.agents/skills/project-workbench`；
4. 如果 global-guidance 源变化，重新运行同步；
5. 回读版本、manifest、native links；
6. 从安装路径跑测试；
7. 分平台做 discovery；
8. 最后才做 fresh receiver。

不要为了更新 Skill 顺手改 provider、模型、MCP、生产系统。

## 6. 交接给下一个对话的最短说明

> 这是 Project Continuity / Project Workbench 仓库。先读 `project-workbench/references/agent-setup.md` 和 `docs/AGENT-SETUP.zh-CN.md`。先检查本机现状并 dry-run；我确认授权后，再用 `project-workbench/scripts/install_agent_setup.py --apply --link-antigravity` 把共享 Skill 和五个平台提示词同步到正确入口。不要复制多个长期独立 Skill 副本，也不要把文件存在当成 Agent 已加载；最后按平台做 discovery + fresh receiver。
