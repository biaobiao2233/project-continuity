# Project Workbench Skill

This directory is the reusable workflow layer for Project Continuity and is intended to stay in **public parity** with the accepted user-level package used for real dogfood.

It includes:

- Project Continuity / ownership / acceptance semantics;
- GitHub-first issue and pull request governance with local fallback;
- local-machine connector routing;
- direct server WebCodex connector routing;
- EverOS-Tunnel historical-memory routing;
- continuous execution so deterministic in-scope workflows do not stop after every substep;
- implementation / review / verification / handoff workflows;
- the current OpenAI adapter and icon.

## Invocation policy

The checked-in `agents/openai.yaml` uses:

```yaml
policy:
  allow_implicit_invocation: true
```

The Skill description is intentionally narrow enough to auto-discover Project Workbench for real software/project continuity work while excluding ordinary chat and unrelated content tasks. Explicit invocation still works when the user wants to force the workflow.

## Governance model

For substantial work in GitHub-backed projects:

```text
GitHub Issue → branch/worktree → Work Node execution → PR → checks/review → merge
```

GitHub is the durable development ledger. Project Workbench keeps coordination/runtime facts GitHub does not own:

- Work Nodes
- Session Pins
- write ownership
- protected invariants
- blockers/next action
- live/deployment evidence
- handoff/Closure Memory

Do not maintain a duplicate local Issue register when GitHub is canonical. For local-only projects or projects without a suitable repository, local fallback tracking remains available. Trivial low-risk edits need not be forced through Issue/PR ceremony.

## Execution behavior

Once objective, scope, authorization, and next action are clear, continue through safe deterministic steps to the next real gate rather than asking the user to reply `继续` after each step. Pause only for missing input, new authorization, ownership ambiguity, meaningful scope/risk change, or an actual blocker without a safe fallback.

## Connector routing

Current user deployment examples, when available:

- `EverOS-Tunnel` → historical/semantic memory.
- `WebCodex-SG` / `WebCodex-HK` / `WebCodex-US` / `WebCodex-KR` → direct server operations.
- `WebCodex-PC` → Windows/local-machine operations.
- GitHub connector → canonical GitHub Issues/PRs/commits/CI.

Always discover actual current availability instead of assuming these bindings exist in every session.

## Codex

Invoke explicitly with `$project-workbench`.

## ChatGPT

Package this directory as a Skill. Matching project-development requests may invoke it implicitly; users can still invoke it explicitly.

## Claude Code

Copy `SKILL.md` + `references/` to the Claude user Skill directory and add:

```yaml
disable-model-invocation: true
```

to the `SKILL.md` frontmatter. Invoke explicitly with `/project-workbench`.

Platform adapters may differ. Keep the workflow body, authority model, connector routing, EverOS boundary, and safety semantics aligned.
