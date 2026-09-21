# Project Workbench v2 candidate

Version: **2.0.0-rc.1**. This is a complete candidate Skill bundle, not a live installation or release acceptance claim.

The update turns direction-based collaboration into small, continuously integrated deliveries. It preserves proportional governance, direct connector routing, current-state verification, existing ownership safeguards, EverOS-derived-only boundaries and explicit production authorization.

## What changed

- Separate authorization, current observations and version-bound acceptance rather than treating them as one priority stack.
- Keep directions long-lived, tasks/branches short-lived and execution identity replaceable. Do not duplicate GitHub tasks into compulsory Work Nodes.
- Check code, runtime and production-resource isolation independently.
- Prefer interface contracts and early integration over a late departmental merge.
- Bind reviews, integration checks and deployment receipts to exact candidates and environments.
- Make partial bookkeeping explicit and retryable; use a stable project entry or a timestamped projection instead of a second manually maintained current-state database.
- Add a read-only, standard-library local checker with `resume`, `preflight`, `deliver`, and `integrate` commands. It only checks supplied snapshots and never contacts GitHub, merges, deploys, grants authority or auto-accepts.

## Contents

`SKILL.md` is the entrypoint. Existing connector/history reference paths and the original icon are retained. Read specialized references only when needed. The Chinese personalization texts live in `assets/`; the adapter example for explicit-only Codex lives in `assets/adapters/`.

## Usage and verification

Use the existing host installation mechanism for the complete `skill.zip`. Keep the previous installation until the intended receiver pilot succeeds. Do not silently change activation policy or global instructions. See [rollout](references/rollout.md).

The current ChatGPT adapter retains narrow implicit invocation. A Codex installation with an accepted explicit-only policy must use the provided explicit-only adapter, not the ChatGPT setting. Other host-specific policies must be rechecked before installation.

Run optional local tests with Python 3.10+ and Git installed:

```sh
PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -v
python scripts/workbench.py resume assets/examples/packet.json
python scripts/workbench.py preflight assets/examples/packet.json --peers assets/examples/peers.json
```

Examples contain synthetic references, not observed user-project state. The example task is intentionally unfinished; `deliver` must report attention until evidence is supplied. The test suite includes temporary Git worktree integration, but not a live GitHub workflow, real AI receiver evaluation or router deployment.

Use [local-checks](references/local-checks.md) for the exact packet contract and tool limits, [scenarios](evals/scenarios.md) for receiver acceptance, and [sources](references/sources.md) for checked upstream behavior.

## Local validation result

See [validation report](evals/validation-report.md): 47 local tests passed, including one synthetic Git worktree integration pilot. Four CLI smoke checks returned the expected outcomes. No real AI receiver, GitHub-hosted workflow, router deployment or installed-skill activation was performed.

## Scope boundaries

Do not add a daemon, heartbeat, auto-takeover, universal lock server, public tunnel, auto-merge or background agent dispatcher just to use this Skill. Prefer existing runtime and GitHub capabilities. Do not require a packet or Python for simple work.

The candidate keeps one entrypoint. Installation, fresh-receiver acceptance, account settings and GitHub publication are separately observable steps; packaging alone establishes none of them.
