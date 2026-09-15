# GitHub-backed project governance

Use GitHub as the durable development record when a project has a suitable writable repository.

## Source of truth

GitHub owns:

- durable feature requests and bugs (Issues)
- branches
- pull requests
- commits
- code review discussions
- CI status
- merge history

Project Continuity owns coordination state that GitHub does not model well:

- Work Node
- Session Pin
- write ownership
- protected invariants
- live runtime/deployment evidence
- current next action

## Lifecycle

Typical substantial change:

`GitHub Issue → branch/worktree → implementation → Pull Request → checks/review → merge → close Issue`

Do not create a parallel local copy of the Issue body. Link the GitHub identifier from the Work Node.

## Small changes

Do not force Issue/PR ceremony for trivial low-risk edits. Follow repository policy and user intent.

## Local fallback

Use local tracking only when:

- no suitable GitHub repository exists
- the project is intentionally private/local
- the item is an execution note or temporary coordination record
- the user explicitly requests local tracking

## Boundaries

GitHub Issue/PR state does not prove:

- production deployment
- live runtime state
- current ownership of a ChatGPT session
- final acceptance without required evidence

Combine GitHub records with current repo/live evidence and Project Continuity state.
