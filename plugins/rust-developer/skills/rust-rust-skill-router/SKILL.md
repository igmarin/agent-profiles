---
name: rust-rust-skill-router
description: 'Routes a Rust task to the required playbook or atomics and continues
  authorized work. First response line MUST be "Next skill: skills/<name>". Trigger:
  where do I start, rust help, which skill, rust-core-skills.'
license: MIT
metadata:
  source-id: igmarin/rust-core-skills:rust-skill-router
  source-commit: d27b83055ce5a78253adb550b49380ab67190d9b
  kind: router
  dependencies: '[]'
---

Resolve skill names through `../../skill-map.json`; use the source pack to disambiguate. Load only the workflow and resources needed for the authorized task.

# Rust skill router

Apply the [execution contract](../../resources/rust/docs/agent-contract.md) before this procedure.

## Goal

Select the next procedure, load it, and continue the requested work within its gates.

## Inputs / outputs

- In: the user request
- Out: the first skill path and an ordered chain when several procedures are needed

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

For existing crates, load `load-context` first. For behavior changes, continue with `tdd`; for review or explanations, load only the relevant atomics. Load `rust-essentials` before any `.rs` write. Planning-only work uses the named planning pack and does not open an implementation loop.

## Steps

1. Classify with the table
2. First line: `Next skill: skills/<name>`
3. Load the selected skill and continue if execution was requested; for routing-only requests, return the chain.

## Validation

Every selected skill exists in the catalog; changed Rust follows the observed RED/GREEN and quality gates.

## Integration

Human catalog: `README.md`. Registry: `directory.json`. Browse: `docs/reference/skill-catalog.md`.
