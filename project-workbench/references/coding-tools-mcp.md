# Coding Tools MCP / Local-Machine MCP

Use the available local-machine/Coding Tools MCP when the task depends on the user's Windows machine, local repos, services, staging/production, host roots, or machine-side files.

Prefer direct server connectors when the target server already has an authorized WebCodex/Tunnel connector. Use local-machine MCP only for resources that actually live on the user's device.

## Discover actual capability first

Use the tool list/runtime metadata that is actually available. Do not invent a tool name, host alias, project path, permission mode, or server feature because a different account/server had it.

When relevant, inspect server/runtime metadata such as `server_info`, execution environment, host roots, workspace/project context, permission mode, version, and tool inventory. Do not assume a source version is the live production version.

Keep separate:

- Accepted production/runtime
- Source candidate/branch/commit
- Staging runtime/evidence
- Active release pointer/artifact

## Routing

- Windows files, local repositories, desktop-only services → local-machine MCP.
- SG/HK/US/KR server work when the corresponding WebCodex connector exists → that server connector first.
- Historical decisions and old conversations → EverOS connector.
- If a preferred connector is unavailable, state the limitation and use an authorized fallback.

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

Use bounded command tools for tests or validation. Do not interpret a tool limitation as evidence about the code.

## Modification rule

Use the MCP's documented direct patch/write mechanism. Preserve unrelated and concurrent changes. Inspect final status/diff.

## Production boundary

Never infer authorization to stop/restart/replace production, change active-release, alter OAuth/credential state, public endpoints, or promotion state from a general coding request. Require the current Work Node/user authorization to cover the exact action.

Never print or persist secrets. When checking environment/configuration, prefer variable names/status over secret values.
