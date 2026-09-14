---
name: tdd
type: playbook
tags: [playbooks]
license: MIT
description: >
  Cargo TDD: observed failure for missing behavior, authorized implementation, green,
  refactor, fmt/clippy. Trigger: tdd, red-green-refactor, test first, cargo test.
metadata:
  version: "1.0.0"
  user-invocable: "true"
  entry_point: true
  phases: "Phase 1: Context and RED, Phase 2: Scope check and GREEN, Phase 3: Refactor, Phase 4: Quality"
  hard_gates: "Test fails for missing behaviour, Authorized scope, Quality gate green"
  dependencies:
    - source: self
      skills: [load-context, rust-essentials]
---

# TDD playbook

Apply the [execution contract](../../docs/agent-contract.md) before this procedure.

## HARD-GATE

- No implementation until a test exists, was run, and failed because behaviour is missing (not because of compile noise you have not fixed in the test).
- Continue implementation already authorized by the user after RED is observed.
- Quality gate before you call it done — same commands as `docs/skill-authoring.md`: `cargo fmt --check`, `cargo clippy --all-targets -- -D warnings`, `cargo test`.

## When to use

New or changed behaviour in a Rust crate. Prefer unit tests next to the module; `tests/` only for public-API contracts.

## Loads

| Skill | Role |
|-------|------|
| `load-context` | existing crates |
| `rust-essentials` | apply `docs/fcis-rust.md` |

## Phases

1. **Context + RED** — `load-context` if the crate exists. Write the smallest failing test. Run `cargo test <test_name> -- --exact`.
2. **Authorized GREEN** — show the actual test + failure. Implement within the accepted scope. Re-run until green.
3. **Refactor** — behaviour unchanged; re-run after each step.
4. **Quality** — fmt, clippy `-D warnings`, `cargo test` for the crate.

## Validation

- RED: failure is missing behaviour
- User said to implement
- GREEN on the target test
- fmt/clippy/test exit 0

## Error recovery

| Problem | Action |
|---------|--------|
| Test does not compile | fix the test; stay in RED |
| Still red after impl | smallest fix; ask only if scope or authority must change |
| Refactor red | revert last step |
| Clippy red | fix; do not `#[allow]` to skip the gate |

## Output

```text
## TDD Report
**Behaviour:** …
**Test:** `path` / `test_name`
**RED:** command + reason
**Approval:** yes/no
**GREEN:** command
**Quality:** fmt / clippy / test
**Skipped (ponytail):** …
```

## Integration

Atomics during GREEN: `type-driven-design`, `error-handling`, `ownership-borrowing` as needed. Do not skip `rust-essentials`.
