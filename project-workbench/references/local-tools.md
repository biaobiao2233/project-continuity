# Local / Repository Tooling

Use the local-machine or coding tools actually exposed by the current client.

## Discover capability first

Do not invent tool names, host aliases, workspace paths, permission modes or server features because another machine/account had them.

When relevant, inspect current tool/runtime metadata and keep separate:

- accepted production/runtime;
- source candidate/branch/commit;
- staging runtime/evidence;
- active release pointer/artifact.

## Read first

Prefer bounded file/search/git tools before shell fallbacks. Establish the actual current implementation before proposing edits.

## Modify safely

Use the platform's documented patch/write mechanism when available. Preserve unrelated/concurrent changes. Inspect final diff/status.

## Review mode

When asked for read-only review:

- re-read current Project Spine/Work Node and actual candidate;
- do not assume previous findings were fixed;
- do not modify source or accepted state;
- return evidence using the task contract's verdict vocabulary.

## Production boundary

Never infer permission to stop/restart/replace production, change credentials, release pointers or deployment state from a generic coding request. Require current explicit authorization for the exact action.

Never print/persist secrets.

