# Templates

## A. Compact Project Spine

```markdown
# <Project> — Project Spine

## Handoff Card
- Current goal:
- Current state:
- Verification state:
- Next action:
- Blockers:
- Protected invariants:
- last_verified_at:

## Current Resume Point
- Last completed action:
- Current physical state:
- Last verification:
- In-flight issue:
- Safe next action:
- Do NOT repeat:

## Current Requirements

## Protected Invariants

## Active Work Node
- Objective:
- Owned scope:
- Out of scope:
- Acceptance criteria:
- Status:

## Major Discoveries / Pitfalls

## Verification Evidence

## Closure Memory

## Sources / Related Docs
```

## B. Full Project Spine

```markdown
# <Project> — Project Spine

## Handoff Card
- Current goal:
- Active node:
- Accepted predecessors:
- Current state:
- Verification state:
- Resume point:
- Next action:
- Blockers:
- Protected invariants:
- Project path:
- Critical files:
- Relevant Closure Memories:
- last_verified_at:

## Current Resume Point

## Current Requirements

## Requirement Anchors / User Evidence

## Protected Invariants

## Work Node Index
| Node | Goal | Status | Verification | File / Closure |
|---|---|---|---|---|

## Major Discoveries

## Major Pitfalls

## Open Questions / Blockers

## Closure Memory Index

## Related Repository Docs

## Sources / Historical Pointers
```

## C. Work Node

```markdown
# <Node ID> — <Title>

## Node Contract
- Objective:
- Owned scope:
- Out of scope:
- Acceptance criteria:
- Protected invariants:
- Dependencies:

## Current Status
- Worker status:
- Independent verification:
- Accepted status:
- Blockers:
- Next action:

## Current Resume Point
- Last completed action:
- Current physical state:
- Last verification:
- In-flight issue:
- Safe next action:
- Do NOT repeat:

## Relevant Requirements

## Execution Records

## Independent Reviewer Contract
> Delete if not required.

- Review objective:
- Threat / failure model:
- Read-only sources:
- Required checks:
- Forbidden actions:
- Acceptance criteria:
- Required verdict:

## Verification Evidence

## Major Discoveries / Pitfalls

## Closure Memory

## Source Pointers
```

## D. Closure Memory

```markdown
## Closure Memory — <Node ID / Title>

- Final status:
- Closed at:
- Goal:
- Accepted outcome:
- Durable capabilities:
- Inherited user requirements:
- Protected invariants:
- Major discoveries:
- Major pitfalls:
- Verification evidence:
- Remaining risks:
- What future work may assume:
- What future work must NOT assume:
- Source / evidence links:
```

## E. Completion Packet

```text
status:
executor:
owned scope:
changed files / artifacts:
exact checks / commands:
results:
important findings:
failures / blockers:
source conversation / task id:
recommended next action:
```

Completion Packet 是 Worker Claim，不自动等于 PASS。

## F. Requirement Anchor

```markdown
### YYYY-MM-DD — User Evidence

> <long-lived user requirement in the user's own words>

^req-<project>-<short-key>
```

只对长期重要、需要跨 Node 精确引用的需求建立 anchor。

## G. Handoff Test Scorecard

```markdown
## Handoff Test

- Receiver:
- Receiver had access to old chat: no
- Project Spine path:

### Recall
- Current goal correct: PASS/FAIL
- Active node correct: PASS/FAIL
- Accepted state correct: PASS/FAIL
- Next action correct: PASS/FAIL
- Invariants correct: PASS/FAIL

### Authority
- Worker Claim kept separate from PASS: PASS/FAIL
- Derived memory treated as clue: PASS/FAIL
- No unsupported facts invented: PASS/FAIL

### Execution
- Receiver could start without user re-explaining history: PASS/FAIL
- In-flight resume point restored correctly: PASS/FAIL/N/A

### Verdict
- Overall: PASS/FAIL
- Missing context:
- Schema changes needed:
```

