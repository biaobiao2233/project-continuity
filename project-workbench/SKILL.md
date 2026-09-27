---
name: project-workbench
description: "Resume, coordinate, implement, review, and hand off persistent projects across sessions and agents. Use for ongoing/resumable GitHub-backed work, canonical handoffs, multi-agent task queues, branch/worktree isolation, formal review/verification, or reconciliation of repository and live state. Keep governance proportional; do not impose this workflow on ordinary chat, simple code questions, one-off low-risk edits, or isolated reviews without continuity needs."
---

# Project Workbench

Use this skill as a compact, platform-neutral control plane for ongoing project work. Keep current repo/live evidence authoritative, keep GitHub as the durable development ledger when available, and keep handoff/coordination compact enough that a fresh agent can resume quickly.

Runtime-specific commands, connector names, sandbox policy, installation paths, and host UI behavior belong in that agent's global guidance or integration adapter, not in this Skill.

## 1. Route before doing work
Resolve in this order:
1. Current explicit user task or switch.
2. Existing valid Session Pin for this continuing interaction.
3. Bound Work Node and its ownership/scope.
4. Canonical project handoff / active tracker item.
5. Project-level focus only for a fresh, unpinned session.

Never inherit a stale Session identity merely because an old prompt names one.

## 2. Fast Resume is the default cold-start path
For a fresh coordinator/session on a GitHub-backed project:
1. Locate the canonical coordinator/project handoff when one exists.
2. Read its `Fast Resume` header or equivalent current-state section.
3. Read only the explicitly referenced active Issue/PR and latest evidence needed for the stated Next Action.
4. Recheck only repo/live facts that could invalidate that Next Action.
5. Execute the Next Action through the next real gate.
6. Update the handoff only when the gate/current objective/active item materially changes.

Do **not** scan all Issues, PRs, historical chats, or old closures by default.
Read [references/fast-resume.md](references/fast-resume.md).

## 3. Escalate to Deep Recovery only when needed
Use broader recovery only when the handoff is missing, conflicting, stale, authorization/ownership is ambiguous, a referenced active item materially changed, high-impact risk requires wider verification, or the user explicitly requests a full audit.

Stop once the real current state and safe Next Action are established.

## 4. Choose the canonical surface
- **GitHub**: durable Issues, branches, PRs, commits, reviews, CI, merge history, research threads.
- **Project Continuity**: Work Nodes, Session Pins, write ownership, protected invariants, blockers, live/deployment evidence, next action.
- **Handoff**: compact current-state index, never a duplicate project archive.
- **Repo docs/ADR**: accepted long-lived knowledge, not raw agent search logs.
- **Historical memory**: discovery/source location only when higher-authority current sources are insufficient.

Read on demand:
- [fast-resume.md](references/fast-resume.md)
- [project-continuity.md](references/project-continuity.md)
- [github.md](references/github.md)
- [cloud-queue.md](references/cloud-queue.md)
- [git-worktrees.md](references/git-worktrees.md)
- [everos.md](references/everos.md)
- [workflows.md](references/workflows.md)
- [agent-setup.md](references/agent-setup.md)

Discover the capabilities actually available in the current agent/session. Never invent a connector, host alias, repo path, permission, or runtime feature.

## 5. Scale governance to task risk
- **L0** ordinary chat/simple question → answer directly.
- **L1** one-off low-risk edit → inspect → edit → verify → finish.
- **L2** resumable/multi-file/substantial Git work → minimum continuity, normally a canonical Issue plus branch; use a worktree when isolation helps.
- **L3** multi-agent/production/security/migration/architecture → explicit ownership, isolated workspaces, canonical tracker, required checks, independent review/verification where appropriate.

Do not create process merely to demonstrate process.

## 6. GitHub-first lifecycle
For substantial GitHub-backed changes, prefer:

`Issue → branch → isolated worktree when needed → implementation/tests → PR → required review/checks → merge → release verification when applicable`

Treat `main`/default branch as the integration line, not a shared scratch workspace.

Research:
- raw exploration / Scout reports → Issue comments;
- Coordinator synthesis / accepted decision → Issue comment or decision record;
- accepted durable architecture/knowledge → repo docs/ADR through a PR.

## 7. Multi-agent cloud queue
When several agents can execute independent bounded tasks, publish them to the canonical tracker and let agents claim them rather than making the user relay prompts/results manually.

Roles may include `Coordinator`, `Scout`, `Implementer`, `Reviewer`, and `Verifier`.
Use [references/cloud-queue.md](references/cloud-queue.md).

## 8. Branch/worktree isolation
For concurrent writable tasks:
- one independently writable task → one branch;
- concurrent agents or a protected canonical worktree → one branch + one dedicated worktree per task;
- different agents must not share the same writable worktree;
- reviewer/verifier remains candidate-read-only during an independent review round.

Host-native worktree commands belong in host global guidance, not here.
Read [references/git-worktrees.md](references/git-worktrees.md).

## 9. Respect authority and acceptance
Use this evidence order when facts conflict:
1. Current explicit user intent/authorization.
2. Independently verified Accepted Project State.
3. Current repository/files/live reproducible evidence.
4. Worker claim/executor report.
5. Agent summary/inference.
6. Historical memory clue/index.

`Worker COMPLETE != PR merged != Accepted != Released`

A timeout, permission denial, partial test, or worker statement is never PASS.

## 10. Execute continuously when the path is clear
When Objective, scope, authorization, and Next Action are established:

`inspect → edit → test → repair → retest → package/PR/update → verify`

Pause only for missing required input, new/broader authorization, ownership ambiguity, an unapproved irreversible/high-risk action, or a real blocker with no safe fallback.

## 11. Update only high-signal continuity
At a meaningful gate:
- update active Issue/PR evidence;
- update compact Handoff only when objective, active item, gate, blocker, invariant, or Next Action materially changes;
- link canonical tracker identifiers instead of duplicating bodies;
- write Closure Memory only after actual acceptance.

Do not persist raw prompts, giant logs, full diffs, secrets, or duplicated GitHub discussions.
