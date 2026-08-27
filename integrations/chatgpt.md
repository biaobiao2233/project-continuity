# ChatGPT

## Project Workbench

ChatGPT Skill 可以使用仓库里的 `project-workbench/` 作为 canonical core。

推荐 ChatGPT adapter 允许 implicit discovery，但必须靠 description 做 anti-ceremony 边界：普通聊天、无关研究、一次性简单编辑不应触发 Project Continuity。

示例 `agents/openai.yaml`：

```yaml
interface:
  display_name: "Project Workbench"
  short_description: "Project continuity, review, handoff, and multi-agent workflows"
policy:
  allow_implicit_invocation: true
```

平台 metadata 不属于 canonical core；其它 Agent 不需要复制 `agents/openai.yaml`。

## Global instructions

可参考 `prompts/global-guidance.zh-CN.md`，把稳定不变量放入 ChatGPT Custom Instructions。

不要把项目 current state 写进账号级提示词。

## Handoff

fresh ChatGPT conversation 不应因为看到旧 Session Key 就继承旧会话 write authority。接手共享 scope 时使用新 key + explicit handoff，除非平台能提供真实 claimant-continuity evidence。

