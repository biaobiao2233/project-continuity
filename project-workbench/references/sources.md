# Sources and compatibility notes

Checked on 2026-09-21. The operating choices are this candidate's design; the sources below support platform facts, not a claim that those features are enabled for a particular user/repository. Recheck capabilities at execution time.

- Git worktree: https://git-scm.com/docs/git-worktree — worktrees share repository objects/refs and do not isolate external runtime resources.
- GitHub issue dependencies: https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-issue-dependencies — native blocked-by/blocking relationships are available; permissions must still be checked.
- GitHub merge queue: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue — eligibility is repository/organization dependent; Actions checks need `merge_group` when a queue is required.
- GitHub PR review: https://docs.github.com/en/pull-requests/how-tos/review-pull-requests/reviewing-proposed-changes-in-a-pull-request — authors cannot approve their own PRs; configured stale approvals can be dismissed after changes.
- GitHub deployments: https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/control-deployments — environments/concurrency govern the configured workflows, not arbitrary external SSH operations.
- ChatGPT custom instructions: https://help.openai.com/en/articles/8096356-custom-instructions-for-chatgpt — current documentation lists 1,500 characters for Free/Go and 5,000 for Plus/Pro/Enterprise/Business/Education. This bundle provides full and compact texts; inspect the actual target UI before applying.

Source Skill: the complete currently exposed `project-workbench` bundle was copied before edits; existing connector reference files and icon were retained. This is an update of that bundle, not a rewrite of historical accepted PC-01..PC-09 records or an assertion of parity with a freshly inspected public GitHub release.
