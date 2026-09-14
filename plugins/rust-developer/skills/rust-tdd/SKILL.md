---
name: rust-tdd
description: 'Cargo TDD with approval-aware execution: failing test for the right
  reason, authorized implementation, green, refactor, fmt/clippy. Trigger: tdd, red-green-refactor,
  test first, cargo test.'
license: MIT
metadata:
  source-id: igmarin/rust-core-skills:tdd
  source-commit: f105faa7b2a493bd8434ce7ee99ca3a424b1007a
  kind: workflow
  dependencies: '["igmarin/rust-core-skills:load-context", "igmarin/rust-core-skills:rust-essentials"]'
---

Resolve skill names through `../../skill-map.json`; use the source pack to disambiguate. Load only the workflow and resources needed for the authorized task.

# TDD playbook

Apply the [execution contract](../../resources/rust/docs/agent-contract.md) before this procedure.

## HARD-GATE

- No implementation until a test exists, was run, and failed because behaviour is missing (not because of compile noise you have not fixed in the test).
- Implementation waits for explicit user approval unless the task already granted implementation authority; after RED, continue only within that accepted scope.
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
2. **HITL + GREEN** — show the actual test + failure. Wait for explicit approval unless implementation was already authorized. Implement only within the accepted scope. Re-run until green.
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
| Still red after impl | smallest fix; re-approve if the approach or scope changes |
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
