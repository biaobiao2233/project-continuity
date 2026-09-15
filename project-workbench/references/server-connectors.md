# Server WebCodex connector routing

Use direct server connectors when the target server already exposes an authorized WebCodex/Tunnel connector.

## Routing

- SG WebCodex → Singapore server tasks.
- HK WebCodex → Hong Kong server tasks.
- US WebCodex → US server tasks.
- KR WebCodex → Korea server tasks.
- Local-machine MCP → Windows/local-only resources.

Do not route a server task through Windows, SSH tunnels, or old proxy paths when a healthy direct server connector exists.

## Verification

Before changes:

- confirm the actual connector and target
- inspect runtime/repo state
- confirm scope and protected invariants

After changes:

- run focused checks
- verify relevant live state
- report evidence separately from claims

## Safety

Never assume a server connector exists because another session had it. Discover current capabilities first.
Never expose credentials or secret environment values.
