# Direct server connector routing

Prefer an authorized direct server WebCodex/Tunnel connector whenever the target actually lives on that server. Discover the current tool inventory first; connector names below are deployment bindings, not assumptions that every session has them.

## Current deployment bindings

When available:

- `WebCodex-SG` → Singapore server.
- `WebCodex-HK` → Hong Kong server.
- `WebCodex-US` → US server.
- `WebCodex-KR` → Korea server.
- `WebCodex-PC` → user's Windows machine; use only for local-machine targets.

Do not route SG/HK/US/KR work through Windows SSH, legacy Cloudflare paths, or another server merely because those paths existed historically when a healthy direct connector to the target is available.

## Before changing anything

1. Confirm the connector resolves to the intended host/project/runner.
2. Inspect current repo/runtime/service state needed for the task.
3. Re-read applicable project instructions and protected invariants.
4. Confirm the requested action is inside existing authorization; root capability does not expand scope.

## Execute and verify

- Prefer bounded native read/patch/process tools exposed by the connector.
- Preserve unrelated/concurrent changes.
- Continue through safe inspect → modify → test → repair → retest steps without asking between routine operations.
- After mutation, inspect the relevant diff/status and live state rather than trusting command success alone.
- Keep source acceptance, staging acceptance, and production release distinct.

## Fallback

If the preferred direct connector is unavailable, identify the exact transport/tool failure and use another already-authorized path only when it preserves scope and safety. Do not report a connector outage as a target-host/product failure.

Never expose credentials, secret environment values, private keys, or tunnel runtime keys.
