# Skill Architecture — Rust Core Skills

Conventions and structure for every `SKILL.md` in this library.

- **Overview and catalog:** [README](../README.md)
- **Docs index:** [index.md](index.md)
- **Authoring template:** [skill-authoring.md](skill-authoring.md)
- **Placement:** [taxonomy.md](taxonomy.md)

## Directory structure

```text
rust-core-skills/
├── docs/
│   ├── architecture.md
│   ├── fcis-rust.md
│   ├── playbooks.md
│   ├── skill-authoring.md
│   ├── taxonomy.md
│   ├── topic-inventory.md
│   └── reference/
│       └── skill-catalog.md
├── skills/<name>/SKILL.md   # Flat layout
├── scripts/                 # rs-guard helpers
├── bin/                     # Bundled rs-guard
├── hooks/
├── directory.json           # Canonical skill registry
├── skills.sh.json           # Marketplace groupings (display only)
├── AGENTS.md                # Host-context source
├── CLAUDE.md                # Thin stub → AGENTS.md
└── README.md
```

There is **no** root `SKILL.md`. Each skill is `skills/<name>/SKILL.md` so `npx skills add` can pick all or one.

## SKILL.md structure

### 1. YAML frontmatter (required)

```yaml
---
name: skill-name
type: atomic          # atomic | playbook | orchestrator
tags: [atomic]
license: MIT
description: >
  Use when [concrete trigger]. Trigger words: [nouns, verbs, symptoms].
metadata:
  version: "1.0.0"
  user-invocable: "true"
---
```

- `name`: kebab-case, **must equal** the directory name
- `type`: `atomic`, `playbook`, or `orchestrator`
- `description`: **when to use + trigger words**. Target ≤ 600 characters. Hard fail at 1024.
- Do not summarize the workflow or hard-gate list in YAML. HITL / HARD-GATE stay in the body.

### 2. Body

Follow [skill-authoring.md](skill-authoring.md). Atomics: goal, rules, one ✅/❌ pair, gates, validation. Playbooks: phases, hard gates, HITL, error recovery, output style. Orchestrator: route only; first line `Next skill: skills/<name>`.

## Registry

`directory.json` lists **written** skills only. Paths must exist on disk. Planned IDs live in [topic-inventory.md](topic-inventory.md) until they have a `SKILL.md`.

## Skill kinds

| Kind | `type` | Role |
|------|--------|------|
| Atomic | `atomic` | One domain: rules + one example pair + gates |
| Playbook | `playbook` | Phases, hard gates, HITL; loads atomics |
| Orchestrator | `orchestrator` | Routes; never implements |

Logical groups (Rust Core, Playbooks, …) live in `skills.sh.json`, not in nested folders.

## References

| Context | Format | Example |
|---------|--------|---------|
| `directory.json` | Full path | `skills/rust-essentials/SKILL.md` |
| Router / playbook body | Skill name or `skills/<name>` | `skills/tdd` |
| Integration tables | Short name | `rust-essentials` |
