# Skill Catalog

7 written skills. `directory.json` is the registry. Planned names: [topic-inventory.md](../topic-inventory.md).

## Rust core

| Skill | Path | Use when |
|-------|------|----------|
| **rust-essentials** | `skills/rust-essentials/SKILL.md` | Any `.rs` write. FCIS, ponytail ladder, parse-at-boundary. |
| **ownership-borrowing** | `skills/ownership-borrowing/SKILL.md` | Clone, lifetimes, Arc/Rc, interior mutability. |
| **type-driven-design** | `skills/type-driven-design/SKILL.md` | Newtypes, enum state, typestate, `TryFrom` at the boundary. |
| **error-handling** | `skills/error-handling/SKILL.md` | `Result`, `?`, thiserror/anyhow, unwrap on recoverable errors. |

## Project

| Skill | Path | Use when |
|-------|------|----------|
| **load-context** | `skills/load-context/SKILL.md` | Existing crate. Read `Cargo.toml`, toolchain, one neighbor + its test. |

## Playbooks

| Skill | Path | Use when |
|-------|------|----------|
| **tdd** | `skills/tdd/SKILL.md` | New or changed behaviour. RED → HITL approve → GREEN → quality gate. |

## Orchestration

| Skill | Path | Use when |
|-------|------|----------|
| **rust-skill-router** | `skills/rust-skill-router/SKILL.md` | Unclear next skill. Does not implement. |

## Typical chain

```text
rust-skill-router → load-context → tdd → rust-essentials → PR
```

PRDs and tickets: [`agnostic-planning-skills`](https://github.com/igmarin/agnostic-planning-skills).
