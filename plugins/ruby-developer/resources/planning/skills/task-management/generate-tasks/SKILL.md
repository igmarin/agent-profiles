---
name: generate-tasks
type: atomic
license: MIT
description: >
  Use when breaking a feature or approved PRD into an implementation
  task list.
  Trigger words: task list, implementation plan, feature breakdown,
  generate tasks, TDD tasks, break down this PRD.
metadata:
  version: 1.0.0
  user-invocable: "true"
---
# Generating a Task List from Requirements

## HARD-GATE

```text
Task 0.0 records or creates an isolated feature branch according to project policy.
DO NOT combine TDD sub-tasks into a single task.
Generate tasks from an approved PRD or concrete user-authorized brief. Mark unresolved scope decisions; small bug fixes do not require a PRD.
```

## Quick Reference
- Task 0.0: create feature branch.
- Output: `/tasks/tasks-[feature-name].md`.
- Auto-detect test command, source dir, test dir, doc tool.
- Validate test command before full generation.

## Workflow

### 1. Project Detection
Detect conventions using config files (see [TEST_COMMANDS.md](TEST_COMMANDS.md)). Identify source and test directories.

### 2. Validation
Run the detected test command when available; record baseline failures and distinguish environment failures from assertion failures. Continue planning with explicit constraints; ask only for a material decision.

### 3. Requirements Analysis
Break down the feature/PRD:
- Identify user-visible behaviors.
- Choose a smallest slice (first-slice heuristics) for TDD.
- Group behaviors into parent task groups.

### 4. Generate Task List
Create `/tasks/tasks-[feature-name].md` using the template in [TASK_TEMPLATES.md](TASK_TEMPLATES.md). Each parent group follows TDD quadruplet (write failing test, confirm fail, implement, confirm pass).

### 5. Final Validation
Review tasks for coverage, correctness, and file paths.

## Integration
| Skill | When |
|-------|------|
| **create-prd** | Feeds requirements |
| **estimate-tasks** | After tasks generated |
