# Reusable Project Workflows

## Fast continuation
Handoff/Fast Resume → active Issue/PR → latest relevant evidence → minimal invalidating checks → execute Next Action → update gate if changed.

## Deep Recovery
Use only when Fast Resume is insufficient: explicit task → handoff/spine → active Work Node → canonical tracker → repo/live state → relevant accepted predecessor → history only if still needed.

## Continuous execution
When Objective, scope, authorization, and Next Action are clear:
`inspect → edit → test → repair → retest → package/PR/update → verify`

## Publish multi-agent work
Split only independent scopes; create bounded canonical Issues; avoid overlapping writes; agents claim via `cloud-queue.md`; Coordinator reads GitHub results and advances the gate.

## Substantial Git implementation
Issue → inspect branch/worktree → dedicated branch/worktree → smallest coherent change → focused checks → repair/retest → regression/scope checks → final diff/status → PR/tracker update → required review/verification.

## Independent review
Start from actual candidate, inspect diff/artifact, reproduce checks, verify scope/invariants/revision, return evidence-backed verdict, do not edit candidate.

## Pause / handoff
Update active tracker evidence; update Handoff only if objective/gate/active item/blocker/Next Action changed; preserve links/invariants/evidence; do not copy raw logs/prompts.
