# Project Workbench Skill

This directory is the reusable workflow layer for Project Continuity.

## ChatGPT

The checked-in `agents/openai.yaml` is the ChatGPT adapter and keeps implicit discovery enabled. Package this directory as a Skill.

## Codex

Use the same `SKILL.md` + `references/`, but set the OpenAI adapter policy to:

```yaml
policy:
  allow_implicit_invocation: false
```

Then invoke explicitly with `$project-workbench`.

## Claude Code

Copy `SKILL.md` + `references/` to the Claude user Skill directory and add:

```yaml
disable-model-invocation: true
```

to the `SKILL.md` frontmatter. Invoke explicitly with `/project-workbench`.

The platform adapters intentionally differ. The workflow body and reference semantics should remain aligned.

