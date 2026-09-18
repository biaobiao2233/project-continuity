# Project Continuity Design Principles

## Purpose

Project Continuity is a lightweight framework for long-running AI-assisted projects. It focuses on preserving context, controlling scope, and separating claims from verified states.

## Core Principles

### 1. Goal before workflow

Tools, MCP servers, skills, and governance processes are means to achieve an objective. The workflow should serve the acceptance criteria, not become the objective itself.

### 2. Proportional governance

Governance should match risk:

- L0: normal questions and explanations
- L1: small one-off changes
- L2: continuous projects with handoff needs
- L3: production, security, migration, architecture, or multi-agent work

Do not introduce heavyweight ceremony for low-risk work.

### 3. Current evidence over assumptions

Agents should verify repository state, files, tests, runtime state, and handoff information before making claims about completion.

### 4. Separate completion states

A worker claim is not automatically acceptance.

```
Implementation complete
        !=
Verified
        !=
Accepted
        !=
Production released
```

### 5. Scope discipline

Every substantial task should make clear:

- Objective
- Owned Scope
- Out of Scope
- Acceptance Criteria
- Protected Invariants
- Blockers
- Next Action

## Integration Philosophy

Project Continuity does not require a specific vendor or runtime. Memory providers, execution environments, repository providers, and external connectors should be replaceable while preserving the same continuity model.
