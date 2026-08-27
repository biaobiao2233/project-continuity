# SG MCP Usage

Use SG MCP only when its coding workspace/tools are actually available and the target lies inside that configured workspace. If the target is outside it or the task is machine/service administration, use an appropriate local-machine/Coding Tools MCP instead.

## Before changing code

1. Read applicable project instructions such as nearest `AGENTS.md`, `GEMINI.md`, task/Work Node, and `DESIGN.md` when relevant.
2. Inspect current repository state with available Git read tools such as `git_status`, `git_diff`, `git_log`/`git_show` as needed.
3. Confirm the requested Objective, Owned Scope, protected invariants, and observable completion checks.
4. Preserve unrelated or concurrent changes.

## Read and search

Use SG read/search/Git tools to establish the current implementation before proposing edits. Do not guess file contents or implementation state.

## Modify

Use `apply_patch` as the direct file-modification mechanism when that is the SG server contract. Do not modify files through command-shell redirection or editing scripts.

Prefer the smallest coherent patch. Do not perform unrelated cleanup, dependency upgrades, formatting churn, architecture rewrites, authentication/policy changes, or production work unless explicitly owned by the task.

## Execute and verify

Use the bounded command tool for tests, builds, linters, compilers, and developer commands. Poll a long-running command through the server's session interaction tool instead of launching duplicates. A timeout or still-running job is not PASS.

After implementation:

- run focused checks required by the task
- run the smallest useful regression/integration gate
- inspect final `git_diff`
- inspect final `git_status`
- report exact changed files and material verification results

## Review mode

For read-only review, do not use `apply_patch`. Inspect the current diff and run only non-mutating checks. Return findings with reproducible evidence and do not self-integrate repairs unless the task explicitly changes from review to implementation.

If SG tools are unavailable in another account/session, say so and use another authorized coding path when one exists; never fabricate SG results.
