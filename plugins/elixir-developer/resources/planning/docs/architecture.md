# Skill Architecture — Agnostic Planning Skills

Conventions and structure for every `SKILL.md` in this library.

- **Overview and catalog:** [README](../README.md)
- **Persona chains:** [persona-guide.md](persona-guide.md)
- **Docs index:** [index.md](index.md)

## Directory Structure

```text
agnostic-planning-skills/
├── docs/
│   ├── architecture.md
│   ├── persona-guide.md
│   ├── calling-skills.md
│   └── reference/
│       ├── skill-catalog.md
│       ├── integration-matrix.md
│       └── gaps.md
├── skills/<name>/SKILL.md   # Flat layout (catalog, atomics, personas)
├── scripts/                 # validate-skills.sh, rs-guard helpers
├── bin/                     # Pre-built rs-guard binaries
├── hooks/
├── directory.json           # Canonical skill registry
├── skills.sh.json
├── AGENTS.md                # Host-context source
├── CLAUDE.md                # Thin stub → AGENTS.md
└── README.md
```

The catalog entry is `skills/agnostic-planning-skills/SKILL.md` (no root `SKILL.md`). Display groups: `skills.sh.json`.

## SKILL.md Structure

Every skill follows this structure:

### 1. YAML Frontmatter (Required)

```yaml
---
name: skill-name
type: atomic          # atomic | persona | catalog
license: MIT
description: >
  Use when [concrete trigger]. [One gate only if skipping the body is dangerous].
  Trigger words: [nouns, verbs, symptoms].
---
```

**Rules:**

- `name`: kebab-case, **must equal** the directory name
- `type`: `atomic`, `persona`, or `catalog` only
- `description`: **when to use + trigger words**. First sentence = when. Body = how.
- Target ≤ 600 characters (folded). Hard fail at 1024 (Agent Skills spec).
- Do **not** summarize the workflow, hard-gate list, output shape, or taxonomy in YAML
- One gate in YAML only if skipping the body would be dangerous (draft-only, no implementation)
- HITL / HARD-GATE stay in the body
- Frontmatter as a whole is not a 1024-character budget — only `description` is

### 2. Title and Core Principle

```markdown
# Skill Title

Use this skill when [brief trigger].

**Core principle:** [One sentence philosophy]
```

### 3. Quick Reference (High Priority)

A scannable table at the top for fast lookup:

```markdown
## Quick Reference

| Aspect | Rule |
|--------|------|
| ... | ... |
```

### 4. HARD-GATE (Where Applicable)

Non-negotiable blockers in a code block:

```markdown
## HARD-GATE

\```
DO NOT [forbidden action].
ALWAYS [required action].
\```
```

### 5. Core Rules / Process

The main instructions. Use numbered steps for processes, bullet lists for rules.

### 6. Common Mistakes (High Priority)

Table format with "Mistake" and "Reality" columns:

```markdown
## Common Mistakes

| Mistake | Reality |
|---------|---------|
| "Excuse or bad practice" | Why it's wrong and what to do instead |
```

### 7. Red Flags (High Priority)

Bullet list of signals that the skill is being violated:

```markdown
## Red Flags

- Signal that something is wrong
- Another signal
```

### 8. Integration (Medium Priority)

Table of related skills and when to chain them:

```markdown
## Integration

| Skill | When to chain |
|-------|---------------|
| **other-skill** | When [condition] |
```

## Frontmatter Optimization (CSO)

How the description helps agents find the right skill:

1. Start with "Use when..." (activation trigger)
2. Include concrete nouns and action verbs
3. End with `Trigger words:` for discovery
4. Do NOT summarize the workflow (the model will skip the body)
5. Target ≤ 600 characters; hard fail at 1024

**Good:**

```yaml
description: >
  Use when generating a Product Requirements Document, defining feature scope,
  or writing a product spec.
  Trigger words: PRD, product requirements, plan a feature, write a spec.
```

**Bad:**

```yaml
description: >
  This skill creates PRDs by first writing the introduction, then goals, then
  user stories, then requirements, then non-goals, then success metrics.
```

## Skill Types

### Atomic Skills (`type: atomic`)

Single-purpose capabilities. Do one thing well.

- `create-prd` — Product Requirements Documents
- `generate-tasks` — TDD task checklists from PRDs
- `plan-tickets` — Tracker-ready ticket drafts
- `requirements-clarifier` — Transform vague requests into specifications

### Personas (`type: persona`)

Role-based orchestrators that sequence atomic skills with scope and evidence gates. Legacy `type: persona` and catalog paths remain stable; in composed roles, product-owner, project-manager, and tech-lead own outcomes while delivery-lead coordinates the delivery workflow.

- `product-owner` — Full planning lifecycle: Discovery → PRD → Tasks → Tickets → Sprint
- `delivery-lead` — End-to-end pipeline: Scope → Plan → Prioritize → Sprint → Execute → Retrospect

## Skill Reference Formats

Skills are referenced by three conventions depending on context:

| Context | Format | Example |
|---------|--------|---------|
| `directory.json` | Full path: `skills/<name>/SKILL.md` | `skills/create-prd/SKILL.md` |
| Persona body (activate calls) | Skill name | `create-prd` |
| Integration tables | Short name only | `create-prd` |

Layout is flat. Integration tables use bare names; `directory.json` is the path source of truth.

## Approval Gates

Planning skills use **hard gates** for scope, evidence, and external authorization. The current request or a prior decision satisfies approval when it covers the action; repeat a question only when scope materially changes.

### PRD Approval Gate

Defined in: `create-prd`, `product-owner` persona.

Purpose: Resolve new product scope before implementation. An approved PRD or concrete authorized brief is sufficient; a small bug routes directly to the implementation pack. Draft tasks within the requested planning scope.

### Ticket Approval Gate

Defined in: `plan-tickets`, `product-owner` persona.

Purpose: Tracker publication needs an explicit request; existing authorization is sufficient. Default planning output remains draft-only.

### Sprint Confirmation Gate

Defined in: `product-owner` persona.

Purpose: Sprint placement must be confirmed by the user. The persona does not assume sprint IDs, capacity, or team availability.

## Platform Compatibility

All skills use standard Markdown and YAML frontmatter, compatible across major AI coding assistants that support skill/plugin loading.
