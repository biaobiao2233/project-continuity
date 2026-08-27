---
name: project-workbench
description: "Use for software/project work that benefits from repeatable project continuity, handoff, implementation, review, verification, local/repo tool routing, or multi-agent coordination. Trigger on requests to continue/resume a project, inspect a Project Spine or Work Node, coordinate parallel sessions, review a candidate, recover historical clues, or manage Issue → Work Node → Candidate → Review/Release gates. Do not use for ordinary chat, unrelated research, or simple one-off edits that do not need project continuity."
---

# Project Workbench

Use this skill as a compact control plane for repeatable project-development work. Prefer current project files, repository state, and live evidence over remembered conversation state.

## Core workflow

1. **Resolve the real current state first.**
   - Read the project's Project Spine / handoff entry when it exists.
   - Route in this order: current explicit user task/switch → existing valid Session Pin → bound Work Node state/ownership → Project Primary Focus / Parallel Active Work Registry → only an unpinned new session defaults to project-level focus.
   - A later project-level focus change must not silently reroute a still-valid Session Pin.
   - A fresh/cold conversation must not silently reuse an old logical Session Key; ambiguous claimant continuity fails closed to read-only.
   - Read only the requirements, invariants, relevant predecessor Closure Memory, repo docs, and live state needed for the task.

2. **Route to the right evidence/tool layer.**
   - For Project Continuity, Work Nodes, Closure Memory, Issue/Blocker/Gate governance and coordination: read [references/project-continuity.md](references/project-continuity.md).
   - For local-machine, repo, staging, production and coding-tool operations: read [references/local-tools.md](references/local-tools.md).
   - For semantic/historical recovery through EverOS or another derived memory system: read [references/everos.md](references/everos.md).
   - For implementation, review, verification, delegation, handoff and closure patterns: read [references/workflows.md](references/workflows.md).
   - Use only tools actually available in the current account/session. Never invent capabilities because another agent or machine had them.

3. **Classify new friction before changing scope.**
   - Current-task finding → keep in the current implementation/review/repair cycle.
   - Temporary Blocker → record on the current Node and continue when unblocked.
   - Independent Issue → record/triage separately; do not opportunistically widen the Active Work Node.

4. **Respect authority and acceptance.**
   - Treat current explicit user intent/authorization as highest authority.
   - Prefer independently verified Accepted State and reproducible repo/live evidence over worker reports or summaries.
   - Keep Worker Claim, Reviewer Verdict, Independent Evidence, Primary Acceptance and Accepted State distinct.
   - When a Work Node or task contract requires independent review/verification, do not let the implementer self-accept that Node; otherwise follow that task's required checks and Primary acceptance policy.

5. **Stay inside scope and verify before claiming completion.**
   - Preserve Objective, Owned Scope, Out of Scope, Acceptance Criteria, Protected Invariants, dependencies, blockers and next action.
   - Before parallel/shared writes, check active Session Pins and write scopes. Overlap serializes unless physically isolated.
   - Central/shared files use read-before-write + narrow patch. Context mismatch requires re-read/merge, not stale overwrite.
   - Do not perform unrelated cleanup, dependency upgrades, refactors, production changes or policy changes.
   - A timeout, permission denial, partial test run, provider error or worker statement is not PASS.

6. **Update continuity only with high-signal current/accepted facts.**
   - Update the Work Node/Handoff with compact evidence and the real next action when appropriate.
   - On closure, write compact Closure Memory rather than a chronological transcript.
   - Do not dump raw prompts, giant logs, secrets, duplicated source material or whole diffs into project memory.

## Default interaction style

- Use tools when the task depends on current files, repo state, machine state or prior project records.
- Keep the user informed about meaningful state transitions, blockers, risks and gate results without narrating every low-level tool call.
- Do not take over desktop/GUI unless explicitly asked.
- Do not expose credentials, tokens, OAuth secrets, private keys or secret environment values.
- Apply governance proportionally: formal structure is for safety/continuity, not bureaucracy.

## Fast routing examples

- **“继续这个项目 / 下一步是什么”** → current task → valid Pin → bound Node → project-level focus only for an unpinned new session → relevant Closure → repo/live verification.
- **“帮我改这个项目”** → continuity contract → inspect repo → bounded implementation → tests/diff → Worker Claim → independent verification if required.
- **“独立审查一下”** → read current contract and actual candidate/diff → stay read-only → evidence-based verdict.
- **“之前为什么这么做”** → Project Continuity first; if insufficient, use EverOS/derived memory for clues, then return to source/current evidence.
- **“又发现一个问题”** → classify current-task vs Blocker vs Issue before acting.

