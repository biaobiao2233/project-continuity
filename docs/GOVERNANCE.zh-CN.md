# Lightweight GitHub-style Governance

Project Continuity 借用 GitHub 成熟协作模型，但不复制整套产品 UI。

推荐生命周期：

```text
Observation / Problem
→ Issue
→ Triage
→ Milestone / Target (optional)
→ Work Node
→ Branch / Worktree (optional)
→ Implementation
→ Candidate Change Packet
→ Required Checks / Independent Review (when required)
→ PASS / REPAIR_FIRST / FAIL
→ Source Merge
→ Staging / Release Gate
→ Release / Promotion
→ Closure Memory
```

## Issue

**Issue records a problem, not a decision.**

Issue 可以记录 symptom / evidence / impact / reproduction，但：

- Issue severity != execution authorization；
- suspected cause != accepted cause；
- Issue != Requirement；
- Issue != Work Node；
- Issue != Accepted Memory。

## Milestone

Milestone 只是 planning view，不建立第三套状态机。

真实 Issue 状态留在 Issue；真实 Work Node 状态留在 Work Node。

## Candidate Change Packet

正式 Review 的候选变更建议记录：

```text
Candidate revision:
Worker / executor:
Linked Issues:
Objective / why:
Owned scope:
Changed files / artifacts:
What changed:
Acceptance criteria addressed:
Automated checks:
Results:
Known risks:
Breaking changes:
Rollback:
Independent review status:
Merge readiness:
Release readiness:
```

Candidate Packet 是 review surface / Worker Claim，不是 PASS。

## Required Review Gate

高风险 Node 可要求：

- focused tests；
- regression tests；
- lint / build；
- security / adversarial review；
- scope / diff check；
- live-state / staging verification；
- independent reviewer；
- rollback / cleanup verification；
- Primary acceptance。

缺 required check 不得 PASS。

但普通低风险任务不机械要求 independent review。

## Merge / Release

始终区分：

```text
Accepted/Merged Source
!= Staging Accepted
!= Production Released
```

一个 commit 被 merge 不证明线上已经发布。

## Branch / worktree / fork

- 自有 repo 的多 Agent 并行优先 branch/worktree；
- scope 本来就不重叠时不机械新建 worktree；
- fork 更适合外部 upstream 或长期分叉实验；
- Git 隔离不替代 Project Continuity ownership / acceptance。

## Deferred by default

除非真实使用证明需要，不默认增加：

- Project Board / Kanban；
- 大量 labels / priority matrix；
- Bot / webhook；
- 自动 Issue/PR 双向同步；
- CODEOWNERS automation；
- 自动 release。

