# Project Workbench Skill

This directory is the reusable workflow layer for Project Continuity and is intended to stay in **public parity** with the accepted user-level package used for real dogfood.

It includes:

- current Project Continuity / governance semantics;
- Coding Tools MCP / local-machine routing;
- SG MCP coding-workspace routing;
- EverOS historical-recovery routing;
- implementation / review / verification / handoff workflows;
- the current OpenAI adapter and icon.

## Default invocation policy

The checked-in `agents/openai.yaml` uses:

```yaml
policy:
  allow_implicit_invocation: false
```

This is the current accepted **explicit-only** baseline. It reduces accidental activation of project governance during ordinary chat or one-off work.

## Codex

Invoke explicitly with `$project-workbench`.

## ChatGPT

Package this directory as a Skill. The public default remains explicit-only. A ChatGPT deployment may deliberately opt into implicit discovery after testing its anti-ceremony boundary; that is an adapter policy choice, not a change to the canonical workflow.

## Claude Code

Copy `SKILL.md` + `references/` to the Claude user Skill directory and add:

```yaml
disable-model-invocation: true
```

to the `SKILL.md` frontmatter. Invoke explicitly with `/project-workbench`.

The platform adapters may differ. The workflow body, authority model, EverOS boundary and safety semantics should remain aligned.

