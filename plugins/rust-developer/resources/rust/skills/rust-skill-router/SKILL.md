---
name: rust-skill-router
type: orchestrator
tags: [orchestration]
license: MIT
description: >
  Routes a Rust task to one playbook or atomic. Does not implement.
  First response line MUST be "Next skill: skills/<name>".
  Trigger: where do I start, rust help, which skill, rust-core-skills.
metadata:
  version: "1.0.0"
  user-invocable: "true"
---

# Rust skill router

Apply the [execution contract](../../docs/agent-contract.md) before this procedure.

## Goal

Select the next procedure, load it, and continue the requested work within its gates.

## Inputs / outputs

- In: the user request
- Out: the skill path to load, and nothing else

## Reads / writes

- Read: this file, `directory.json`, `README.md`
- Write: none

## Approval

None.

## Route

Load only paths that exist in `directory.json`. No skill yet → `Next skill: skills/rust-essentials` (and `skills/tdd` if behaviour changes).

| If the request is… | Next skill |
|--------------------|------------|
| PRD / tickets / sprint | **stop** — `agnostic-planning-skills` |
| Existing crate, first action | `skills/load-context` |
| New or changed behaviour / TDD / bug | `skills/tdd` |
| Clone / lifetime / Arc | `skills/ownership-borrowing` |
| Newtype / enum state | `skills/type-driven-design` |
| unwrap / thiserror | `skills/error-handling` |
| Anything `.rs`, including clap/tokio/unsafe/clippy until those skills exist | `skills/rust-essentials` |

For existing crates, load `load-context` first. For behavior changes, route to `tdd`; for review or explanations, load only the relevant atomics. Load `rust-essentials` before any `.rs` write. Planning-only work routes to `agnostic-planning-skills` and does not open an implementation loop.

## Steps

1. Classify with the table
2. First line: `Next skill: skills/<name>`
3. Stop — do not write crate code.

## Validation

No `.rs` in the crate was written in this turn.

## Integration

Human catalog: `README.md`. Registry: `directory.json`. Browse: `docs/reference/skill-catalog.md`.
