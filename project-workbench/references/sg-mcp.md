# Server WebCodex / SG MCP Usage

Use a server WebCodex connector only when that server's tools are actually available in the current account/session and the target belongs to that server.

Prefer the direct server connector over routing through Windows or old SSH/Cloudflare paths.

## Server routing

- SG WebCodex: primary for Singapore server services and workspaces.
- HK WebCodex: primary for Hong Kong server tasks.
- US WebCodex: primary for US server tasks.
- KR WebCodex: primary for Korea server tasks.
- Use local-machine MCP only when the target is the Windows machine.

## Before changing code

1. Read applicable project instructions such as nearest `AGENTS.md`, `GEMINI.md`, task/Work Node, and `DESIGN.md` when relevant.
2. Inspect current repository state with available Git read tools.
3. Confirm Objective, Owned Scope, protected invariants, and observable completion checks.
4. Preserve unrelated or concurrent changes.

## Read and modify

Establish current implementation before proposing edits. Use the server MCP's documented patch/write mechanism. Prefer smallest coherent patches.

Do not perform unrelated cleanup, dependency upgrades, formatting churn, architecture rewrites, authentication/policy changes, or production work unless explicitly owned.

## Execute and verify

Use bounded command tools for tests, builds, and validation. A timeout or still-running job is not PASS.

After implementation:

- run focused checks
- inspect final diff/status
- report exact changed files and material verification results

## Review mode

For read-only review, do not modify candidate state. Inspect actual evidence and return findings separately from acceptance.

If server tools are unavailable, say so and use another authorized path; never fabricate server results.
