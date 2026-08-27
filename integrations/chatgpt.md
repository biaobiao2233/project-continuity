# ChatGPT

## Project Workbench

ChatGPT Skill 可以使用仓库里的 `project-workbench/` 作为 canonical core。

当前公开 package 采用 **explicit-only** 作为安全默认值。这样普通聊天、无关研究、一次性简单编辑不会因为 description 误匹配而进入 Project Continuity 工作流。

如果某个 ChatGPT 环境经过真实 anti-ceremony dogfood 后希望自动匹配，可以把 implicit discovery 当成**平台 adapter policy**单独开启；不要静默修改 canonical core。

示例 `agents/openai.yaml`：

```yaml
interface:
  display_name: "Project Workbench"
  short_description: "Project continuity, MCP workflows, review, and handoff"
  icon_small: "./assets/icon.svg"
  icon_large: "./assets/icon.svg"
policy:
  allow_implicit_invocation: false
```

平台 metadata 不属于 canonical core；其它 Agent 不需要复制 `agents/openai.yaml`。

## Global instructions

可参考 `prompts/global-guidance.zh-CN.md`，把稳定不变量放入 ChatGPT Custom Instructions。

不要把项目 current state 写进账号级提示词。

## Handoff

fresh ChatGPT conversation 不应因为看到旧 Session Key 就继承旧会话 write authority。接手共享 scope 时使用新 key + explicit handoff，除非平台能提供真实 claimant-continuity evidence。

