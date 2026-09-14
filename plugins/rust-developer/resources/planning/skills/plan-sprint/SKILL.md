---
name: plan-sprint
type: atomic
license: MIT
description: >
  Use when selecting tickets for a sprint from a prioritized backlog,
  setting a sprint goal, or allocating capacity.
  Trigger words: plan sprint, sprint planning, sprint goal, sprint
  capacity, sprint backlog, what should we work on this sprint.
metadata:
  version: 1.0.0
  user-invocable: "true"
---
# Planning a Sprint

Select tickets, define a goal, and commit to a sprint scope.

## Quick Reference

- **Input:** Prioritized backlog, team capacity, sprint duration.
- **Output:** Sprint plan with selected tickets, sprint goal, capacity allocation.
- **Rule:** Don't overcommit — plan for ≤80% of theoretical capacity.

## HARD-GATE

```text
DO NOT commit more than the team's historical velocity.
DO NOT select tickets with unresolved dependencies or unclear acceptance criteria.
DO set a single, clear sprint goal that every selected ticket supports.
```

## Core Process

1. **Gather inputs** — prioritized backlog (from `prioritize-backlog`), team capacity, sprint dates, historical velocity.
2. **Define sprint goal** — every selected ticket must support this goal.
3. **Select tickets** — start from the top of the backlog, stop when total estimate reaches ≤80% of capacity (see [Capacity Heuristics](#capacity-heuristics) below).
4. **Validate** — check no ticket has unresolved dependencies, unclear acceptance criteria, or missing estimates. Use the [Common Anti-Patterns](#common-anti-patterns) table as a checklist.
5. **Flag** — tickets that almost made the cut (next sprint), dependency risks, stretch goals.
6. **Output** — sprint plan using the format in [Output Style](#output-style).

## Capacity Heuristics

### Theoretical Capacity
- **Per person per day:** 6 productive hours.
- **Sprint capacity:** `team_size × sprint_days × 6h × utilisation_factor`
- **Utilisation factor:** 0.8 for stable teams; 0.6–0.7 for new or high-uncertainty teams.

### Velocity
- **Rolling average:** Mean completed points across last 3–5 sprints; exclude disrupted sprints.
- **No history:** Use `theoretical_capacity × 0.6` as a conservative baseline.
- **Declining trend:** Use the most recent sprint's figure rather than the average.

### Common Anti-Patterns

| Anti-Pattern | Mitigation |
|---|---|
| Planning to 100% capacity | Cap at 80% |
| Including unestimated tickets | Estimate before committing |
| Multiple sprint goals | One goal per sprint |
| Ignoring dependencies | Resolve or defer dependents |
| Carry-over without re-estimation | Re-estimate carry-over tickets |

## Output Style

1. **Sprint header** — name, dates, duration, team capacity.
2. **Sprint goal** — single sentence.
3. **Selected tickets** — `| Rank | Ticket | Estimate | Confidence | Notes |`
4. **Capacity allocation** — total committed, buffer (%), stretch goals.
5. **Deferred** — top 3 items that didn't fit, for next sprint visibility.
6. **English only** unless user requests otherwise.

Worked example: [assets/example-sprint-plan.md](assets/example-sprint-plan.md).

## Integration

| Skill | When to chain |
|---|---|
| **prioritize-backlog** | Use ordered backlog as input to ticket selection |
| **estimate-tasks** | Reference estimates for capacity-based selection |
| **identify-risks** | Scan sprint plan for dependency and capacity risks |
