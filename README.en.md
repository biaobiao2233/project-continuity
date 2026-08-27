# Project Continuity

**A cross-agent project memory and handoff protocol for long-running work.**

[中文](README.md) · [Specification](docs/SPECIFICATION.zh-CN.md) · [Templates](docs/TEMPLATES.md) · [EverOS integration](docs/EVEROS-INTEGRATION.md) · [Roadmap](ROADMAP.md)

Project Continuity helps a fresh AI agent safely resume a project without replaying the entire conversation history.

It is not a chat archive or a vector database. It focuses on three questions:

> **What should be remembered now? What should be trusted? How should the next agent continue?**

Current public baseline: **v1.1 Markdown Protocol + Project Workbench**.

## Core model

```text
Project Spine
  ├─ Handoff Card
  ├─ Current Requirements
  ├─ Protected Invariants
  ├─ Work Node
  ├─ Current Resume Point
  ├─ Closure Memory
  └─ Source Pointers
```

The acceptance test is intentionally simple:

> Can a strong agent that never saw the previous conversation safely start the next step using only the Project Spine, relevant Closure Memory, and necessary project files?

## Main ideas

- **Lifecycle over chronology** — create Work Nodes around independently closable work, not around dates or chats.
- **Closure over replay** — closed work leaves compact Closure Memory instead of staying in the default active context.
- **Authority separation** — User Evidence, Worker Claim, Independent Evidence and Accepted Memory are not interchangeable.
- **In-flight resume state** — Current Resume Point records the physical boundary of unfinished work.
- **Fail-closed multi-session coordination** — ambiguous ownership becomes `OWNERSHIP_UNCERTAIN`; shared/candidate writes become read-only.
- **Proportional governance** — formal review gates are used when the task or node contract needs them, not for every tiny edit.

## EverOS integration

Project Continuity is the current-state / authority layer. EverOS is a derived semantic memory and historical retrieval layer.

```text
raw conversations / artifacts
          ↓
       EverOS
  historical clues
          ↓
Project Continuity
 current state / handoff
          ↓
 repo / live verification
```

EverOS can help locate relevant history, but its compressed memory must not silently replace exact source evidence, current authorization, or live state.

Open EverOS fork: <https://github.com/biaobiao2233/EverOS>

## Prior art

The current design incorporates ideas—not source code—from:

- **SpineCodex** — task lifecycle and closed-node memory;
- **GitHub workflows** — Issues, milestones, PR-style candidates, required checks, and Merge != Release;
- **Orca** — explicit ownership transfer, authority decomposition, worktree isolation, and fail-closed recovery;
- **EverOS integration experience** — derived semantic memory is a clue/source locator, not raw ground truth.

See [docs/PRIOR_ART.md](docs/PRIOR_ART.md) for the exact boundaries.

## Roadmap

- **v1.x:** improve Markdown ergonomics, examples, and drift validation.
- **v2:** optional CLI/MCP helpers only if manual drift becomes a repeated problem.
- **v3:** experimental runtime context injection / hooks.
- **v4:** optional local context proxy and request-time compression research.

The project deliberately avoids adding a database, daemon, heartbeat, proxy or automatic context rewriting until real usage justifies the additional authority and failure modes.

## Quick start

1. Copy `examples/compact-project/README.md` into a small project, or use the full example for long-running work.
2. Make that file the stable Project Spine.
3. Ask the agent to read the Spine, restore current state and invariants, and inspect repo/live state only as needed.
4. Close finished Work Nodes with Closure Memory.
5. Use `project-workbench/` for a reusable on-demand workflow.

Platform notes are under `integrations/`.

## License

MIT. No source code from SpineCodex, Orca, or other prior-art repositories is included in this repository.

