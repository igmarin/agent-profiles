---
name: rust-tdd
description: 'Cargo TDD: observed failure for missing behavior, authorized implementation,
  green, refactor, fmt/clippy. Trigger: tdd, red-green-refactor, test first, cargo
  test.'
license: MIT
metadata:
  source-id: igmarin/rust-core-skills:tdd
  source-commit: d27b83055ce5a78253adb550b49380ab67190d9b
  kind: workflow
  dependencies: '["igmarin/rust-core-skills:load-context", "igmarin/rust-core-skills:rust-essentials"]'
---

Resolve skill names through `../../skill-map.json`; use the source pack to disambiguate. Load only the workflow and resources needed for the authorized task.

# TDD playbook

Apply the [execution contract](../../resources/rust/docs/agent-contract.md) before this procedure.

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
