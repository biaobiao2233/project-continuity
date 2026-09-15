# Local-machine / Coding Tools routing

Use a local-machine/Coding Tools connector only when the task depends on resources that actually live on the user's Windows machine: local repos/files, desktop-only services, device state, or local build/runtime processes.

Prefer a healthy direct server connector for server targets. Do not use Windows as an unnecessary SSH jump host when the target server already has an authorized direct connector.

## Current local binding

Prefer `WebCodex-PC` when it is online and exposes the needed capability. Treat older device-specific local MCP connectors as fallback rather than the default path. If no local connector is available, state that limitation instead of inferring local state.

## Discover actual capability first

Use the tool inventory/runtime metadata that is actually available. Do not invent a tool name, project path, host alias, permission mode, repo, or server feature because a different session had it.

Keep these distinct:

- accepted production/runtime
- source candidate/branch/commit
- staging/runtime evidence
- active release pointer/artifact

## Routing

- Windows files, local repos, desktop-only services → local-machine connector.
- SG/HK/US/KR server resources → corresponding direct server connector first.
- Durable GitHub Issues/PRs/commits/CI → GitHub connector when GitHub is canonical.
- Historical decisions/old agent sessions → `EverOS-Tunnel` when available.

If the preferred connector is unavailable, identify the transport/tool limitation and use an already-authorized fallback only when appropriate.

## Read and modify

Prefer bounded dedicated helpers such as file reads, searches, Git status/diff/log, and runtime metadata before using general commands. Use the connector's documented patch/write mechanism for direct file edits when available. Preserve unrelated/concurrent changes.

Once scope and authorization are clear, continue through safe inspect → edit → test → repair → retest without asking for confirmation after every routine step.

## Production boundary

Never infer authorization to stop/restart/replace production, change release pointers, credentials, OAuth state, public endpoints, or permissions from a general coding request. Require the current user authorization/Work Node to cover the exact action.

Never print or persist secrets. When inspecting configuration, prefer variable names/status over secret values.
