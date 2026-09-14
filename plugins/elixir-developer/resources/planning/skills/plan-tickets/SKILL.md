---
name: plan-tickets
type: atomic
license: MIT
description: >
  Use when breaking a plan into tracker tickets or classifying work
  items. Draft-only unless the user explicitly asks to create issues.
  Trigger words: create tickets, Jira, Linear, GitHub Issues, classify
  work items, ticket drafts.
metadata:
  version: 1.0.0
  user-invocable: "true"
---
# Plan Tickets

Normalize inputs, classify each work item, draft tickets in a standard structure. Default mode: draft-only.

## HARD-GATE
- Do not create tracker issues unless explicitly asked.
- Do not assume tracker credentials, project fields, sprint IDs, or status behavior.
- If only tickets are requested, return Markdown drafts.

## Core Process
1. Normalize initiative: theme, project, draft vs. create mode, default bucket, constraints.
2. Classify each ticket: type, area, execution order, dependency level, target bucket using the classification rules below.
3. Apply sprint placement: foundation/api before client, exclude external confirmations, place follow-up tickets in ready-to-refine.
4. Apply title prefixes: `BE | ` (backend), `FE | ` (frontend), `Mobile | ` (mobile).
5. Draft each ticket with five sections: Summary, Background, Acceptance Criteria, Dependencies, Technical Notes.
6. Output:

   **Draft-only (default):** Markdown tickets with classification line and five-section structure plus a readiness checklist.

   **Create-in-tracker:** After explicit approval, create issues using the tracker API. Validate required fields; do not set status on create. Confirm with one issue before bulk creation.

## Classification Rules
`[type: Story|Task] [area: backend|web|mobile|cross-platform|external] [execution_order: foundation|api|client|follow-up] [dependency_level: unblocked|blocked] [target_bucket: ready-to-refine|next-dev-sprint|later]`

Optional: `coordination_need`, `external_dependency`, `urgency`.

## Extended Resources
- [EXAMPLES.md](EXAMPLES.md) — full plan-to-ticket example
- [assets/ticket-samples/sample_issue.md](assets/ticket-samples/sample_issue.md) — sample issue format

## Integration
| Skill | When |
|-------|------|
| **generate-tasks** | After tasks exist |
| **create-prd** | Align tickets with PRD scope |
