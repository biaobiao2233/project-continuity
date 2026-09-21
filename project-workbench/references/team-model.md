# Directions, tasks, and execution

## Keep three concepts, not five mandatory layers

Use a stable **direction/Lane** only where work recurs: UI, runtime, infrastructure, research. Use the canonical **task** as the delivery unit. Treat a **conversation/execution** as a temporary assignee. A milestone is optional grouping, not another contract to maintain.

For a GitHub project, link an Issue/PR rather than duplicating its objective and acceptance criteria into a mandatory Work Node. Retain existing Work Nodes where they add execution context or where the project is local-only. Do not rename old records or erase accepted history to adopt this model.

## Task boundaries

Choose a deliverable that can be validated and integrated independently. Record only fields not already available from its canonical source: direction, current executor, isolated workspace, candidate identity, resource claims, blockers and next action. A direction owns capabilities over time; it does not own one never-ending feature branch.

Use short task branches/worktrees from the current integration baseline. Rebase/reconcile through the repository's policy, not by force-pushing somebody else's work. Research may deliver a decision, experiment or contract without a production-code PR.

## Contracts before parallel implementation

Agree on a minimal versioned API/schema or file format and an owner. Consumers pin the contract revision and use shared fixtures. Providers run the same compatibility checks. Freeze only what is needed for the next delivery; do not demand a complete speculative architecture.

When a contract changes, create/link the dependency in the canonical tracker and identify affected consumers. A consumer may continue isolated work with a mock, but cannot claim integration complete until validated against the provider.

## Roles without ceremony

Let a coordinator also integrate routine changes. Let executors work continuously inside their bounded direction. Assign an independent reviewer only when required by risk/repository/task policy; do not silently remove a required independent gate.

Do not let an integrator silently implement substantial product changes to resolve semantic conflicts. Return the defect to its owning task or explicitly revise the scope. Minor merge resolutions still produce a new candidate that needs affected checks.

## Dispatch and work in progress

Before opening another task, look for a blocked consumer that can be unblocked, a PR awaiting review, or a ready integration. Set the concurrency limit from actual available executors, memory, test resources and deployment targets. Do not assume more agents means more throughput.

A coordinator that becomes unavailable does not grant its privileges to every worker. Workers may finish already-owned isolated tasks and report results; central writes and deployment ownership still require a valid grant.

## Athena-style example (illustrative, not live state)

A DNS task and a routing-UI task can build in separate directories with different test ports. Both bind to the same route-status API fixture. Their changes can be reviewed and integrated incrementally. If both need to alter the same router, declare the same canonical production resource (for example `device/athena/network`) and serialize those mutations even when their source files differ.

Do not infer that any Athena deployment or receiver evaluation has run from this example.
