# Candidate rollout and paired instructions

## This package

Treat version 2.0.0-rc.3 as a candidate update of Project Workbench, not as proof that any installed copy, personalization setting, repository release or live workflow has changed. The creation task is code/document/package validation; a real fresh-receiver pilot remains a separate gate.

Preserve the full existing resource structure and icon. Preserve ChatGPT's current narrow implicit invocation policy. The existing Codex deployment is explicit-only; use `assets/adapters/codex-openai.yaml` for that installation and do not silently enable implicit invocation. OpenCode uses its own global `~/.config/opencode/AGENTS.md` plus native Skill discovery; `~/.agents/skills/project-workbench` is already a supported global Skill source, so avoid a duplicate OpenCode copy unless an intentional same-name override is required. Use `assets/adapters/opencode.md` for the OpenCode-specific guidance layer. Do not alter unrelated host instructions incidentally.

Keep one skill entrypoint in the distributable zip. Choose the adapter for the target host; do not install both old and new variants under competing names without a clear invocation plan. Copying files is not proof that a host discovered or loaded them. Confirm discovery and a fresh isolated receiver before claiming activation.

## Personalization

`assets/personalization-v2.txt` is the full Chinese counterpart. `assets/personalization-v2-compact.txt` is a smaller fallback for limited fields. Replace an old prompt rather than appending contradictory versions. Do not insert release notes or validation reports into the personalization field.

The prompt contains stable preferences and boundaries; task instructions, host bindings, ownership grants and runtime versions still come from the current request/project. It does not turn every conversation into project work or authorize production changes.

## Pilot acceptance

Use an isolated repository and two bounded tasks with a shared contract. Demonstrate new-session recovery, independent worktrees, runtime conflict detection, early tested integration, stale-review rejection and interrupted-sync recovery. A deterministic unit test can test the checker; it cannot establish that a fresh AI receiver follows the prose.

Do not use the user's live router as the test fixture. Do not promote this candidate based only on its author's report. Keep existing accepted installation and historical closure records intact until the chosen receiver/review/activation gates pass.

## Reversibility

Keep the previous skill bundle and prompt as private rollback inputs. To revert an installation, restore the previous complete bundle and prior platform adapter, then verify loading. Do not roll back unrelated project code, production services or user preferences.

## Delivery status

Keep package-built, tests-passed, receiver-pilot-pending, installation-confirmed, settings-applied and GitHub-synced separately. A missing external connection may leave GitHub sync pending without blocking a usable local package.
