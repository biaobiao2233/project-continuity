# Coding Tools MCP / Local-Machine MCP

Use the available local-machine/Coding Tools MCP when the task depends on the user's Windows machine, local repos, services, staging/production, host roots, or machine-side files. A deployment may expose this under a device-specific name; do not assume another account/session has the same name or capabilities.

## Discover actual capability first

Use the tool list/runtime metadata that is actually available. Do not invent a tool name, host alias, project path, permission mode, or server feature because a different account/server had it.

When relevant, inspect server/runtime metadata such as `server_info`, execution environment, host roots, workspace/project context, permission mode, version, and tool inventory. Do not assume a source version is the live production version.

Keep separate:

- Accepted production/runtime
- Source candidate/branch/commit
- Staging runtime/evidence
- Active release pointer/artifact

Before and after a risky staging/release operation, recheck the protected production endpoint/process/pointer when the Work Node requires it.

## Read-first workflow

Prefer bounded read tools offered by the current MCP, commonly:

- `read_file` / `host_read_file`
- `list_files` / `host_list_dir`
- `search_text`
- `git_status`
- `git_diff`
- `git_log`
- `git_show`
- `server_info`

Use a bounded command tool for tests or a read-only Git fallback when a dedicated helper cannot resolve the repo. Do not interpret a tool limitation as evidence about the code.

## Modification rule

Use the MCP's documented direct patch/write mechanism (for example `apply_patch` / `host_apply_patch`) for direct file modifications. Do not edit files through shell redirection, ad-hoc editing scripts, `sed -i`, PowerShell content replacement, or similar command side effects when the MCP contract designates patching as the direct modification path.

Preserve unrelated and concurrent changes. Inspect final status/diff.

## Review mode

When asked for an independent/read-only review:

- Re-read the current Project Spine/Work Node and actual current diff/artifact.
- Do not assume prior findings were fixed correctly.
- Do not modify source, Project Continuity, production, or external state.
- Run read-only/focused checks only when authorized by the review contract.
- Return evidence by severity and the contract's verdict vocabulary (for example `PASS_FOR_<NODE>` or `REPAIR_FIRST`).
- Reviewer verdict remains Reviewer Evidence until Primary independently accepts it.

## Machine/GUI boundary

Prefer file/repo/command tools over GUI. Do not use desktop control unless the user explicitly asks for GUI operation. If GUI is user-operated, do not compete for the desktop.

## Production boundary

Never infer authorization to stop/restart/replace production, change active-release, alter OAuth/credential state, public endpoints, or promotion state from a general coding request. Require the current Work Node/user authorization to cover the exact action.

Never print or persist secrets. When checking environment/configuration, prefer variable names/status over secret values.
