# ChatGPT

> Project Workbench `2.0.0-rc.1` 是预发布候选：本地测试通过不等于当前 ChatGPT 账号已经安装、发现或接受该 Skill。

## Project Workbench

ChatGPT Skill 可以使用仓库里的 `project-workbench/` 作为 canonical core。

当前 checked-in ChatGPT/OpenAI adapter 开启 **implicit discovery**，但触发边界是刻意收窄的：只面向持续/可恢复项目、handoff、Project Continuity、live-state、GitHub 治理或多 Agent 协作。普通聊天、简单代码问题、一次性低风险编辑，以及不需要连续性/治理的独立 review 不应自动进入完整 Project Workbench 流程。

示例 `agents/openai.yaml`：

```yaml
interface:
  display_name: "Project Workbench"
  short_description: "Independent directions, continuous integration, verified handoffs"
  icon_small: "./assets/icon.svg"
  icon_large: "./assets/icon.svg"
policy:
  allow_implicit_invocation: true
```

这里的 implicit discovery 是 **ChatGPT adapter policy**，不是 Project Continuity authority model 本身。其它平台可以继续显式调用。

## Global instructions

平台中立模板见 `prompts/global-guidance.zh-CN.md`。

当前 v2 RC 的可直接粘贴 ChatGPT 用户级绑定见：

- `prompts/chatgpt-custom-instructions.zh-CN.md`：仓库级完整版本；
- `project-workbench/assets/personalization-v2.txt`：Skill 内完整副本；
- `project-workbench/assets/personalization-v2-compact.txt`：字符受限场景的短版。

完整/短版二选一，不要叠加。账号级提示词只保存长期行为原则和 connector routing；详细项目 SOP 继续由 Project Workbench Skill 负责，不要把项目 current state 写进账号级提示词。

## Handoff

fresh ChatGPT conversation 不应因为看到旧 Session Key 就继承旧会话 write authority。接手共享 scope 时使用新 key + explicit handoff，除非平台能提供真实 claimant-continuity evidence。

## Future: Web automatic context feed

implicit Skill invocation 仍由模型决定是否触发；它不等于 automatic project context feed。

长期理想状态是在平台能力允许时，由 native project/system-context hook、browser/local companion 或其它可审计 adapter，在模型开始处理任务前提供当前项目的最小 Context Packet。这样模型即使没有主动想到调用 Skill，也能先拿到必要的 current project context。

当前仓库**没有声称这个 Web 自动注入已经实现**。具体实现必须以目标平台真实暴露的能力为准；如果不存在可靠 pre-turn injection surface，就保持当前 Skill/显式读取路径，而不是伪造“无感自动接手”。
