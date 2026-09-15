# EverOS historical memory routing

Use EverOS as read-mostly semantic/historical memory across prior agent sessions. Prefer the direct `EverOS-Tunnel` connector when it is available. Treat the older `everos` connector as fallback, not the default path.

EverOS is useful for discovery and source location; it is not the authoritative current project ledger or live-state monitor.

## Correct evidence level

EverOS output is derived memory/index evidence. Never use it by itself to prove:

- current live machine/repo state
- exact current user authorization
- final acceptance/PASS
- exact wording when a source conversation/file is available
- current production version/deployment state
- current Session Pin or write ownership

If EverOS conflicts with Project Continuity, GitHub canonical records, current repo/files, or live evidence, return to the higher-authority source.

## Tool workflow

When the tools exist:

- Use `memory_status` only when health/availability matters.
- Use `memory_search` for semantic historical questions: why a decision was made, which prior session handled something, or what an earlier experiment found.
- Use focused queries with project/topic names, exact terms, and the missing decision/fact; do not sweep unrelated user history.
- Use returned session/provenance identifiers to narrow the source.
- Use `memory_get` when an exact session ID is known and the bounded episode/case is needed.
- Use `memory_list_sources` only when source inventory is materially relevant.
- Treat `partial`, timeout, stale, or derived results as incomplete rather than evidence that history does not exist.

Do not perform redundant health/status calls before every search when the connector is already working in the current flow.

## Write boundary

Do not call `memory_remember` merely because useful history was found. Memory writes require explicit user intent plus the configured approval path. Project Continuity and the project's canonical tracker remain the normal locations for accepted durable project state.

## Typical recovery sequence

`Project Spine / Active Work Node → canonical Issue/PR/source pointers → relevant Closure → EverOS-Tunnel semantic search if history is missing → exact source/session when needed → current repo/live verification`.

Use EverOS to reduce rediscovery, not to bypass verification.
