# Project Workbench Skill

This directory is the reusable workflow layer for Project Continuity and is intended to stay in **public parity** with the accepted user-level package used for real dogfood.

It includes:

- current Project Continuity / governance semantics;
- GitHub-first issue and pull request governance;
- Coding Tools MCP / local-machine routing;
- direct server WebCodex connector routing;
- EverOS-Tunnel historical-recovery routing;
- implementation / review / verification / handoff workflows;
- the current OpenAI adapter and icon.

## Default invocation policy

The checked-in `agents/openai.yaml` uses:

```yaml
policy:
  allow_implicit_invocation: false
```

This remains the explicit-only baseline. It reduces accidental activation of project governance during ordinary chat or one-off work.

## Governance model

For GitHub-backed projects:

```text
GitHub Issue → branch/worktree → PR → checks/review → merge
```

Project Workbench keeps coordination state that GitHub does not own:

- Work Nodes
- Session Pins
- write ownership
- protected invariants
- live/deployment evidence
- handoff

For local-only projects, local fallback tracking remains available.

## Codex

Invoke explicitly with `$project-workbench`.

## ChatGPT

Package this directory as a Skill. The public default remains explicit-only.

## Claude Code

Copy `SKILL.md` + `references/` to the Claude user Skill directory and add:

```yaml
disable-model-invocation: true
```

to the `SKILL.md` frontmatter. Invoke explicitly with `/project-workbench`.

Platform adapters may differ. The workflow body, authority model, connector routing, EverOS boundary, and safety semantics should remain aligned.
