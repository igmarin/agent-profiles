---
name: create-retrospective
type: atomic
license: MIT
description: >
  Use when writing a sprint retrospective from team feedback and
  metrics.
  Trigger words: retrospective, retro, sprint review, what went well,
  what didn't, lessons learned, improvement items.
metadata:
  version: 1.0.0
  user-invocable: "true"
---
# Creating a Sprint Retrospective

Generate a structured retrospective focused on learning and actionable improvements.

## Quick Reference

- **Input:** Sprint data (goal, completed/not completed), team feedback, metrics.
- **Output:** Retrospective document with action items.
- **Sections:** What Went Well, What Didn't, Action Items, Metrics, Kudos.
- **Rule:** Every "what didn't" needs an action item with an owner.

## HARD-GATE

```text
DO NOT fabricate feedback — only include input the team actually provided.
DO NOT skip action items — every "what didn't" must have at least one action.
DO assign an owner and timeline to every action item.
```

## Core Process

1. **Gather** — sprint data (goal met? completed/not completed tickets), team feedback, relevant metrics.
2. **Categorize**:
   - **What Went Well** — wins, effective practices, things to continue.
   - **What Didn't** — blockers, bottlenecks, process issues, surprises.
   - **Kudos** — shout-outs and recognition.
3. **Identify themes** — group related feedback into themes rather than listing raw comments.
4. **Draft action items** — specific, owned, time-bound. Use the template in [RETROSPECTIVE_TEMPLATE.md](RETROSPECTIVE_TEMPLATE.md) if available; otherwise use the minimal template below.
5. **Review** — verify every "what didn't" maps to an action item.

## Output Style

Use **[RETROSPECTIVE_TEMPLATE.md](RETROSPECTIVE_TEMPLATE.md)** when bundled.

Section order: header → What Went Well → What Didn't → Action Items → Metrics → Kudos. Use English unless the user requests otherwise. Every "what didn't" maps to an action item with Owner, Timeline, and Linked Issue.

## Integration

| Skill | When to chain |
|-------|---------------|
| **plan-sprint** | Review the sprint plan vs what was actually delivered |
| **generate-status-report** | Include retrospective insights in the next status report |
| **project-manager** | Feed action items into the execution tracking pipeline |
