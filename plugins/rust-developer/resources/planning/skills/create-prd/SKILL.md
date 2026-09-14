---
name: create-prd
type: atomic
license: MIT
description: >
  Use when the user wants a PRD, product requirements, a feature spec,
  or a written scope. No implementation code.
  Trigger words: PRD, product requirements, plan a feature, write a spec,
  requirements document.
metadata:
  version: 1.0.0
  user-invocable: "true"
---
# Generating a PRD

**Goal:** Draft a PRD focusing on *what* and *why*, not *how*. No code.

## HARD-GATE
- No code, pseudo-code, SQL, class names, or method signatures.
- Resolve newly introduced product scope before implementation. Existing approval or a concrete user-authorized brief remains valid; this skill produces a PRD, not implementation code.

## Core Process
1. Receive feature description.
2. Clarify only if ambiguous — use up to 5 questions from [assets/prd_questions.md](assets/prd_questions.md).
3. Draft using [PRD_TEMPLATE.md](PRD_TEMPLATE.md) section by section.
4. Validate — present the PRD; request a decision on unresolved product scope before implementation.

## Output
- Save to `/tasks/prd-<slug>.md` (kebab-case).
- Write requirements in natural language — no code.
- Reuse prior approval when scope is unchanged; otherwise request the specific scope decision; include next steps (e.g., "Run `generate-tasks` once approved").

## Integration
| Skill | When |
|-------|------|
| **generate-tasks** | After PRD approved |
| **plan-tickets** | When tracker tickets are needed from approved scope |
