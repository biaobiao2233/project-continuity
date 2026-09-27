# Git Branch and Worktree Isolation

Keep default branch as the integration line. Do not let concurrent agents share one writable workspace.

Use a dedicated branch for substantial durable changes. Typical names: `feat/<issue>-<slug>`, `fix/<issue>-<slug>`, `docs/<issue>-<slug>`, `test/<issue>-<slug>`.

Use a dedicated worktree when multiple writable tasks/agents are concurrent, the canonical worktree must stay clean, a reviewer needs a stable candidate, or branch switching risks unrelated state.

Before creating one: inspect status/branches/worktrees/remotes; confirm base revision and Issue; check claimant collision; create from intended base; verify clean expected branch.

Representative shape:
```bash
git fetch origin
git worktree add ../repo-wt-42 -b feat/42-semantic-export origin/main
```
Do not copy blindly when repo policy differs.

One writable task owns one branch/worktree. Different agents must not edit the same worktree. Worktrees prevent filesystem collisions, not semantic conflicts.

Independent Reviewer/Verifier stays candidate-read-only. Editing candidate ends that independent review round.

Host-native worktree commands belong in host global guidance, not in this cross-agent Skill.

Remove a worktree only after changes are preserved/discard authorized, no claimant owns it, and the branch/PR lifecycle no longer needs it.
