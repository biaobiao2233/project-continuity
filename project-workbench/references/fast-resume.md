# Fast Resume and Cold-Start Recovery

## Default sequence
1. Identify the canonical repo.
2. Find the single current coordinator/project handoff if one exists.
3. Read the `Fast Resume` header first.
4. Read the active Issue/PR named there and only its latest relevant evidence.
5. Verify only facts that could invalidate the stated Next Action.
6. Execute through the next real gate.
7. Update the handoff after the gate changes.

Do not begin by listing every Issue, PR, branch, historical closure, or prior conversation.

## Recommended GitHub handoff
```markdown
## Fast Resume
Role: Coordinator
Project: <name>
Canonical Repo: owner/repo
Active Issue: #123 | none
Active PR: #456 | none
Current Gate: <short machine-readable state>
Next Action: <one concrete next action>

Read First:
- #123 latest relevant comment
- PR #456 checks, if active

Read If Needed:
- #98 accepted decision

Do Not Read By Default:
- historical closed Issues
- old chat summaries
- unrelated PRs
```

Then keep compact sections: Current Objective, Accepted / Verified State, Active Work, Protected Invariants, Blockers, Do Not Assume.

The handoff is an index into canonical evidence, not a second ledger.

## Deep Recovery
Escalate only when the handoff is absent/ambiguous/conflicting/stale, ownership or authorization is uncertain, high-impact risk requires wider verification, or the user asks for comprehensive reconstruction.

Order:
`current explicit task → handoff/spine → active Work Node → canonical Issue/PR → current repo/live evidence → relevant accepted predecessor → historical memory only if still needed`

A fresh physical conversation is a fresh claimant unless continuity is independently established. Durable handoff transfers project knowledge; it does not prove session ownership.
