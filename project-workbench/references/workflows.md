# Four operating workflows

Use these flows in the existing connector/runtime. Do not create a second runner or assume the optional local helper performs remote actions.

## Recover

Read the stable project entry, canonical task/PR and existing execution handoff. Confirm source/workspace and only the required environment. Choose current explicit task over project focus; preserve an established continuing pin unless explicitly switched. Use a fresh execution ID for a fresh conversation.

If an older owner has not released shared scope, continue read-only or in a truly isolated, authorized sandbox. Do not block unrelated safe investigation just to manufacture a registry row. End recovery once the next action and its authority are established.

Optional helper: `python scripts/workbench.py resume packet.json` produces a compact projection of an already collected snapshot. It does not find the project or contact connectors.

## Preflight

Recover Objective/scope/acceptance/invariants from the existing task. Establish current authorization and required review policy. Inspect code workspace and shared runtime/live resource ownership; batch independent reads. Bind the current source ref and needed contract.

For parallel work, verify actual branch/worktree isolation and shared resource inventory. Start only the bounded next step; avoid repeatedly rereading every completed historical task.

Optional helper: `python scripts/workbench.py preflight packet.json --peers peers.json` flags declared resource overlap, missing evidence pointers and uncertain execution ownership. A clear result does not grant write authority or establish a live lock.

## Deliver

Implement → focused checks → repair in scope → affected regression → final diff/readback. Keep executing until required human/independent/platform/production gate, a real blocker, or task completion. Do not ask for “continue” after predictable substeps.

Update the canonical candidate and current handoff entry using read-before-write. Record accurate check coverage and candidate refs. If a task promises a package, supply the complete usable artifact, not just a patch summary.

Keep engineering result and synchronization result separate. Retry pending record updates after re-reading their destinations; never repeat an already confirmed deployment merely to clear a sync flag.

Optional helper: `python scripts/workbench.py deliver packet.json` detects missing required check results, changed candidate refs, invalid declared review independence, source/deployment mismatch and unconfirmed synchronization. It emits `ATTENTION_NEEDED` or `CHECKS_CLEAR`, never project PASS.

## Integrate

Read current target and candidate heads plus dependencies. Verify contract compatibility and required review/platform rules. Test the exact combination, then merge/deploy only through authorized routes. Inspect automation before merging. Read back the result and preserve one resumable next action.

Optional helper: `python scripts/workbench.py integrate packet.json` additionally compares supplied tested/current integration refs and dependency evidence. It does not perform a merge, decide product acceptance, or claim that GitHub CI ran.

## Classify friction

Keep an in-scope finding in this task. Keep a temporary outage/wait as a blocker. Put an independent durable requirement in the canonical tracker. Do not make an external outage a project defect without evidence, and do not broaden the task simply because an adjacent issue is visible.

## Handoff and closure

Release/transfer only owned scope and record any unknown side effects. A receiver re-reads actual state before accepting. Write a compact outcome/evidence/next-action record; archive completed detail outside the default recovery path.

When the required gate is reached, stop. A worker claim, helper result, package validation, technical review, Primary acceptance, merge and deployment remain different statements.
