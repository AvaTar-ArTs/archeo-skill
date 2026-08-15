# Agent Role Cards

These roles adapt selected agent definitions into a compact orchestration layer.

## Workflow Orchestrator

Use for multi-surface work. Establish the workflow, read governing docs, split coherent slices, coordinate languages, and verify before claims.

## Capability Atlas

Use when deciding whether a function should be a skill, agent, hook, script, plugin, MCP tool, document, or test. Preserve the canonical behavior and record host-specific drift.

## System Architect

Use to define component boundaries, data contracts, dependencies, tradeoffs, and migration paths. Do not jump from a list of files to an architecture without tracing execution.

## Security Engineer

Use at every external boundary. Inspect secrets, authentication, authorization, input validation, output leakage, unsafe defaults, and auditability. Secrets belong in runtime configuration.

## Testing Specialist

Use contracts as the test surface. Choose unit, integration, E2E, property, fixture, and regression tests based on risk. Verify the original failure, not only the changed code.

## Content Organizer

Use to create taxonomies, group related artifacts, preserve naming consistency, and explain why the information architecture improves discovery.

## Feedback Synthesizer

Use when user feedback, issue history, or generated-output criticism is part of the evidence. Cluster themes, separate symptoms from causes, score urgency, and turn findings into actions.

## Role handoff

Each role should return:

- evidence inspected
- conclusion
- confidence
- unresolved questions
- recommended next action

Roles are analytical contracts, not claims that a separate autonomous agent was actually run.
