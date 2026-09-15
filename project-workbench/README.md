# Project Workbench Skill

This directory is the reusable workflow layer for Project Continuity and is intended to stay in **public parity** with the accepted user-level package used for real dogfood.

It includes:

- Project Continuity / ownership / acceptance semantics;
- GitHub-first issue and pull request governance with local fallback;
- proportional task governance so small work stays small;
- local-machine connector routing;
- direct server WebCodex connector routing;
- EverOS-Tunnel historical-memory routing;
- continuous execution so deterministic in-scope workflows do not stop after every substep;
- implementation / review / verification / handoff workflows;
- the current OpenAI adapter and icon.

## Invocation policy

The checked-in ChatGPT/OpenAI adapter uses:

```yaml
policy:
  allow_implicit_invocation: true
```

The description is intentionally narrow: auto-discovery is for ongoing/resumable project work, handoff, continuity, governance, live-state work, or multi-agent coordination. Ordinary chat, isolated code questions, one-off low-risk edits, and isolated reviews that do not need continuity/governance are explicitly excluded. Explicit invocation still works when the user wants to force the workflow.

Other platforms may use different adapter policies. Codex and Claude Code guidance remains explicit by default unless their own adapter is deliberately changed.

## Proportional governance

Use the smallest process that preserves correctness:

```text
L0  ordinary chat / simple question
    → answer directly

L1  one-off low-risk edit
    → inspect → edit → verify → finish

L2  resumable / multi-file project work
    → minimum useful continuity, usually a Work Node + focused checks

L3  multi-agent / production / security / migration / architecture
    → explicit ownership + canonical tracker + required gates/review
```

Do not create Issue/PR/Work Node/review ceremony merely to demonstrate that the workflow was used.

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

Tools, MCPs, Skills, and governance structures are means, not the objective. Choose the shortest safe evidence/tool path that satisfies the user goal. Once the goal or acceptance gate is met, stop instead of expanding into optional optimization.

## Connector routing

Current user deployment examples, when available:

- `EverOS-Tunnel` → historical/semantic memory.
- `WebCodex-SG` / `WebCodex-HK` / `WebCodex-US` / `WebCodex-KR` → direct server operations.
- `WebCodex-PC` → Windows/local-machine operations.
- GitHub connector → canonical GitHub Issues/PRs/commits/CI.

Always discover actual current availability instead of assuming these bindings exist in every session.

## Codex

Invoke explicitly with `$project-workbench` unless the Codex adapter is deliberately configured otherwise.

## ChatGPT

Package this directory as a Skill. Matching ongoing project-continuity requests may invoke it implicitly; users can still invoke it explicitly.

## Claude Code

Copy `SKILL.md` + `references/` to the Claude user Skill directory and add:

```yaml
disable-model-invocation: true
```

to the `SKILL.md` frontmatter. Invoke explicitly with `/project-workbench`.

Platform adapters may differ. Keep the workflow body, authority model, connector routing, EverOS boundary, and safety semantics aligned.
