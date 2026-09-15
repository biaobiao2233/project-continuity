# EverOS Usage

Use EverOS only when its memory tools are actually available in the current account/session. Prefer the current direct EverOS connector (for example EverOS-Tunnel) when available. Treat it as read-mostly semantic/historical memory and index across agent sessions. It is useful for discovery; it is not the authoritative current project ledger.

## Correct evidence level

EverOS output is derived memory/index evidence. Never use it by itself to prove:

- current live machine/repo state
- exact current user authorization
- final acceptance/PASS
- exact wording when a source conversation/file is available
- current production version or deployment state

If EverOS conflicts with Project Continuity, current repo/files, or live evidence, return to the higher-authority source.

## Tool workflow

When the corresponding tools exist:

- Use `memory_status` only when health/availability matters.
- Use `memory_search` for semantic historical questions such as why a decision was made, which prior agent/session handled something, or what earlier experiments found.
- Use `memory_get` when an exact session ID is known and the bounded episode/profile/case is needed.
- Use `memory_list_sources` only to inventory configured source partitions when necessary.
- Use focused queries; prefer project/topic names, exact terms, and the missing decision/fact. Do not sweep unrelated user history.
- Treat `partial`, timeout, or stale/derived results as incomplete, not as absence of history.

## Write boundary

Do not call a memory write operation such as `memory_remember` merely because useful history was found. Writes require explicit user intent plus whatever server confirmation/approval path is configured. Project Continuity remains the normal place for accepted durable project state.

## Typical fallback sequence

`Project Spine / Active Work Node → relevant Closure/source pointers → EverOS semantic search if history is missing → exact source/session when needed → current repo/live verification`.

Use EverOS to reduce rediscovery, not to bypass verification.
