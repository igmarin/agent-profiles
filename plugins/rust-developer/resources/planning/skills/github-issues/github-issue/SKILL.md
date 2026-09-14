---
name: github-issue
type: atomic
license: MIT
description: >
  Use when creating, updating, or closing GitHub issues, or moving
  them on a project board when explicitly requested.
  Trigger words: github issue, create issue, track issue, project
  board, milestone.
---

# GitHub Issue Management

## HARD-GATE

```text
Create, update, close, or move issues only when that action is explicitly authorized. A direct request satisfies this gate; a draft-only planning request does not.
DO NOT assume tracker credentials, project fields, or sprint IDs.
```

## Prerequisites
- `gh` CLI installed and authenticated.
- Working in a git repository with a GitHub remote.

## Label Conventions
**Type** (required, one): `bug`, `new-feature`, `improvement`, `refactor`, `security`
**Stage**: `todo`, `in-progress`, `in-review`, `done`
**Phase** (optional): `phase-1`, etc.
**Priority** (optional): `priority:high`, `priority:medium`, `priority:low`
All labels use kebab-case. New issues start with `todo`.

## Stage Lifecycle
```
todo → in-progress → in-review → done (closed)
```
Any stage can revert to `todo` if blocked.

## Creating an Issue

1. Gather context: what's the problem/feature, why, what "done" means, any examples.
2. Detect repo setup: owner/repo, issue templates, Projects V2, Classic projects, milestones (see reference for exact command queries).
3. Draft the issue using a standard template (Problem, Expected Outcome, Proposed Solution, Examples, Acceptance Criteria). If templates exist, adapt.
4. Validate the draft against the request and repository template. Resolve any material ambiguity; reuse explicit authorization already provided.
5. Create the issue via `gh issue create`, add to project board (V2 or Classic using GraphQL), and associate milestone as appropriate.
6. Confirm creation with issue number, labels, and links.

## Updating an Issue

1. Find the issue by number or search.
2. Detect stage change (explicit or inferred).
3. Update labels and stage, close when `done`.
4. Move on project board (V2/Classic) using GraphQL mutations.
5. Confirm update.

For exact GraphQL queries and project board integration details, see [references/gh-commands.md](references/gh-commands.md) (loaded on demand).

## Integration

| Skill | When to chain |
|-------|---------------|
| `plan-tickets` | Draft tickets before creating issues |
| `plan-sprint` | After issues exist, select a sprint |

