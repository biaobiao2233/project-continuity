---
name: project-workbench
description: "Use for software/project work that benefits from the user's repeatable operating workflow: continuing or handing off a project, resolving Project Continuity/Project Spine and Work Nodes, coordinating multiple concurrent ChatGPT/Agent sessions with Session Pin/write-ownership safety, inspecting repo or live state, implementing or reviewing through available coding/local-machine MCPs, recovering historical clues through EverOS, coordinating Codex/Antigravity or other agents, and managing Issue → Work Node → Candidate → Review Gate → staging/release. Trigger on requests like 继续项目、下一步、接上、审查、查账本、并行对话/串台、Session Pin、看 repo 状态、用 EverOS 找历史、用 SG/MCP 改代码、更新 Work Node/Issue/Gate. Do not use for ordinary chat, unrelated research, music, or general writing/content creation without a project-development workflow."
---

# Project Workbench

Use this skill as a compact control plane for repeatable project-development work. Prefer current project files, repository state, and live evidence over remembered conversation state.

## Core workflow

1. **Resolve the real current state first.**
   - Read the project's Project Spine / handoff entry when it exists.
   - Route in this order: current explicit user task/switch → existing valid Session Pin → the bound Work Node's current state/ownership → Project Primary Focus / Parallel Active Work Registry → only an unpinned new session defaults to the project-level focus.
   - A later project-level focus change must not silently reroute a still-valid Session Pin. If claimant continuity for an existing logical Session Key is ambiguous, do not inherit that row/scope; fail closed to read-only and resolve identity/ownership first.
   - Read only the requirements, invariants, relevant predecessor Closure Memory, repo docs, and live state needed for the task.
   - Never assume an Active Node, version, branch, candidate, acceptance state, ownership, or production state from an old chat when current evidence can answer it.

2. **Route to the right evidence/tool layer.**
   - For Project Continuity, Work Nodes, Closure Memory, Issue/Blocker/Gate governance, and RFC/ADR discipline: read [references/project-continuity.md](references/project-continuity.md).
   - For Windows/local-machine, repo, staging, production, host-root, or Coding Tools MCP operations: read [references/coding-tools-mcp.md](references/coding-tools-mcp.md).
   - For semantic/historical recovery across prior agent sessions: read [references/everos.md](references/everos.md).
   - For coding operations inside an SG MCP workspace: read [references/sg-mcp.md](references/sg-mcp.md).
   - For implementation, review, verification, delegation, handoff, and closure patterns: read [references/workflows.md](references/workflows.md).
   - Use the tools actually available in the current account/session. Never invent a tool, connector, mount, path, or capability because another account had it.

3. **Classify new friction before changing scope.**
   - Ask whether a new finding is: **part of the current task**, a **temporary Blocker**, or an **independent Issue**.
   - Keep in-scope findings in the current implementation/review/repair cycle.
   - Keep transient waits, one-off timeouts, normal dependencies, and one-time user interactions as Blockers unless they expose a durable problem.
   - Record durable out-of-scope problems/requirements as Issues for triage; do not opportunistically widen the Active Work Node.

4. **Respect authority and acceptance.**
   - Treat current explicit user intent/authorization as highest authority.
   - Prefer independently verified Accepted Project State and reproducible repo/live evidence over worker reports or summaries.
   - Keep Worker Claim, Reviewer Verdict, Independent Evidence, Primary Acceptance, and Accepted State distinct.
   - When a Work Node or task contract requires independent review/verification, do not let the implementer self-accept that Node; otherwise follow that task's required checks and Primary acceptance policy.

5. **Stay inside scope and verify before claiming completion.**
   - Preserve Objective, Owned Scope, Out of Scope, Acceptance Criteria, Protected Invariants, dependencies, blockers, and next action.
   - Before parallel/shared writes, check active Session Pins and write scopes. Overlapping writes serialize unless physically isolated; central shared surfaces use read-before-write + narrow patch, and any context mismatch requires re-read/merge rather than stale overwrite.
   - A fresh/cold conversation must not silently reuse an existing logical Session Key. Duplicate/ambiguous claimant or ownership evidence means `OWNERSHIP_UNCERTAIN`; shared/candidate writes stay read-only until resolved.
   - Do not perform unrelated cleanup, dependency upgrades, refactors, production changes, or policy changes.
   - Inspect final diff/status and run the focused checks required by the Work Node.
   - For production/staging-sensitive work, independently recheck live version, endpoint/port/process ownership, release pointer/artifact, rollback, and cleanup boundaries as applicable.
   - A timeout, permission denial, partial test run, provider error, or worker statement is not PASS.

6. **Update continuity only with high-signal accepted/current facts.**
   - After meaningful work, update the Work Node/Handoff with compact evidence and the real next action when authorized and appropriate.
   - On closure, write a compact Closure Memory rather than a chronological transcript.
   - Do not dump raw prompts, long logs, secrets, duplicated source material, or whole diffs into project memory.

## Default interaction style

- Use tools when the task depends on current files, repo state, machine state, or prior project records; do not substitute generic advice for available evidence.
- Keep the user informed about meaningful state transitions, blockers, risks, and gate results without narrating every low-level tool call.
- Do not take over the desktop/GUI unless the user explicitly asks for GUI control.
- Do not expose credentials, tokens, OAuth secrets, private keys, or secret environment values.
- When a required tool is unavailable, state the exact limitation and use the nearest safe evidence path; do not fabricate results.
- Apply governance proportionally: use Issue/Milestone/Candidate/Gate/RFC structure when it improves safety or continuity, not as bureaucracy for trivial edits.

## Fast routing examples

- **“继续这个项目 / 下一步是什么”** → current explicit task → valid Session Pin if one exists → bound Work Node → project-level focus only for an unpinned new session → relevant Closure → repo/live verification.
- **“帮我改这个项目”** → continuity contract → inspect repo → implement through the appropriate available coding MCP/tool → tests/diff → Worker Claim → independent verification if required.
- **“独立审查一下”** → read current contract and actual current diff/artifact yourself → stay read-only unless explicitly changed to implementation → evidence-based verdict.
- **“之前为什么这么做”** → Project Continuity first; if insufficient, use EverOS for clues/session IDs, then return to source/current evidence.
- **“又发现一个问题”** → classify current-task vs Blocker vs Issue before acting; do not widen scope automatically.
