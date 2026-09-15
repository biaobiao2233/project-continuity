---
name: project-workbench
description: "Use for software/project work that needs continuity, handoff, live-state inspection, multi-agent coordination, GitHub-backed issue/PR governance, or bounded implementation/review. Trigger when continuing or handing off projects, resolving Project Spine/Work Nodes/Session Pins/write ownership, inspecting repos or servers through WebCodex/local connectors, searching historical decisions through EverOS-Tunnel, or managing substantial GitHub Issues/PRs and release gates. For GitHub-hosted projects, prefer GitHub as the durable issue/PR source of truth and keep local continuity for coordination/runtime facts; use local issue tracking only as fallback. Do not use for ordinary chat or unrelated content tasks."
---

# Project Workbench

Use this skill as a compact control plane for repeatable project-development work. Prefer current project files, repository state, and live evidence over remembered conversation state. Keep durable tracking, execution coordination, live runtime evidence, and historical memory on the surface best suited to each job.

## Core workflow

1. **Resolve the real current state first.**
   - Read the project's Project Spine / Handoff when one exists.
   - Route in this order: current explicit user task/switch → existing valid Session Pin → bound Work Node state/ownership → Project Primary Focus / active registry → only an unpinned fresh session defaults to project-level focus.
   - Never assume version, branch, candidate, acceptance state, ownership, blocker, or production state from an old chat when current evidence can answer it.

2. **Choose the canonical surface before writing.**
   - For Project Continuity, Work Nodes, Session Pins, write ownership, acceptance semantics, and local fallback governance: read [references/project-continuity.md](references/project-continuity.md).
   - For GitHub-backed Issues, branches, PRs, commits, CI, and merge lifecycle: read [references/github.md](references/github.md).
   - For Windows/local-machine repos, files, and services: read [references/coding-tools-mcp.md](references/coding-tools-mcp.md).
   - For SG/HK/US/KR or other directly connected servers: read [references/server-connectors.md](references/server-connectors.md).
   - For semantic/historical recovery across prior agent sessions: read [references/everos.md](references/everos.md).
   - For implementation, review, verification, delegation, handoff, and closure patterns: read [references/workflows.md](references/workflows.md).
   - Discover the tools actually available in the current session. Never invent a connector, host alias, mount, path, permission, or capability.

3. **Use GitHub-first governance without creating a second ledger.**
   - If the project has a suitable writable GitHub repository, use GitHub as the durable source of truth for substantial feature/bug Issues and PR candidates.
   - Keep local Project Continuity for execution contracts and transient coordination: Work Node, Session Pin, write ownership, protected invariants, live/deployment evidence, blockers, and next action.
   - Link GitHub Issue/PR identifiers from the Work Node; do not copy their full bodies into a parallel local Issue register.
   - If the project has no suitable GitHub repository, is intentionally local-only, or the user explicitly wants local tracking, use the local Issue/Work Node fallback.
   - Do not force Issue/PR ceremony for small low-risk edits unless repository policy, user intent, or risk requires it.

4. **Classify new friction before changing scope.**
   - **Current-task finding** → keep it in the current implementation/review/repair cycle.
   - **Temporary Blocker** → record it on the current Node; do not create a durable Issue by default.
   - **Independent Issue** → record it in the project's canonical tracker (GitHub when GitHub is canonical; otherwise local) and triage separately.
   - Do not opportunistically widen the Active Work Node.

5. **Respect authority, ownership, and acceptance.**
   - Treat current explicit user intent/authorization as highest authority.
   - Prefer independently verified Accepted Project State and reproducible repo/live evidence over worker reports or summaries.
   - Keep Worker Claim, Reviewer Verdict, Independent Evidence, Primary Acceptance, and Accepted State distinct.
   - Before shared writes, check Session Pins and write scopes. Overlapping writes serialize unless physically isolated.
   - A fresh/cold conversation must not silently reuse an existing logical Session Key. Ambiguous claimant/ownership means shared/candidate writes stay read-only until resolved.

6. **Execute continuously when the path is already clear.**
   - When Objective, scope, authorization, and next action are established, continue through all safe deterministic substeps to the next real gate or acceptance point without asking the user to reply `继续` between routine steps.
   - Treat read → edit → test → repair → retest → package → PR/update → verification as one continuous workflow when each step remains inside the authorized scope.
   - Batch independent reads/checks/tool discovery when practical. Do not emit a status message merely because one tool call finished.
   - Ask only when required input is missing, a new permission or materially broader scope is needed, ownership is ambiguous, an irreversible/high-risk choice is not already authorized, or a genuine blocker has no safe fallback.
   - Do not widen scope or perform optional risky work merely to avoid asking a question.

7. **Verify before claiming completion.**
   - Preserve Objective, Owned Scope, Out of Scope, Acceptance Criteria, Protected Invariants, dependencies, blockers, and next action.
   - Inspect final diff/status and run the checks required by the Work Node or repository policy.
   - For production/staging-sensitive work, independently recheck the relevant live version, endpoint/process ownership, release pointer/artifact, rollback, and cleanup boundaries.
   - A timeout, permission denial, partial test run, provider error, or worker statement is not PASS.

8. **Update only high-signal continuity.**
   - After meaningful work, update the Work Node/Handoff with compact current evidence and the real next action when appropriate.
   - For GitHub-backed work, record Issue/PR/commit links or identifiers instead of duplicating GitHub content.
   - On closure, write compact Closure Memory rather than a chronological transcript.
   - Do not dump raw prompts, long logs, secrets, duplicated source material, or whole diffs into continuity files.

## Default interaction style

- Use tools when the task depends on current files, repo state, machine state, GitHub state, or prior project records; do not substitute generic advice for available evidence.
- Prefer the closest healthy direct connector to the target system. Do not route server work through the user's PC when a direct authorized server connector is available.
- Minimize interaction turns: if the work can proceed safely, keep working and give one consolidated result at the real gate/end. Intermediate updates are for meaningful blockers, risk changes, or major state transitions, not routine substeps.
- Do not take over the desktop/GUI unless the user explicitly asks for GUI control.
- Do not expose credentials, tokens, OAuth secrets, private keys, or secret environment values.
- Apply governance proportionally; avoid ceremony for trivial work.

## Fast routing examples

- **“继续这个项目 / 下一步是什么”** → resolve Pin/Work Node → canonical tracker references → repo/live verification → execute through the next real gate without pausing after each substep.
- **“修 GitHub 上这个 bug”** → GitHub Issue/PR state → local/server working tree → implement/test/repair → PR/review/merge as required.
- **“帮我改服务器上的项目”** → direct target-server connector → repo/runtime state → bounded change → tests/live verification.
- **“之前为什么这么做”** → continuity/source pointers first → EverOS-Tunnel if history is missing → exact source/live verification.
- **“又发现一个问题”** → classify current-task vs Blocker vs Independent Issue → use canonical tracker without duplicating ledgers.
