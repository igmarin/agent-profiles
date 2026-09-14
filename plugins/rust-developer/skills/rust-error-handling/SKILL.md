---
name: rust-error-handling
description: 'Result over panic. thiserror in libs, anyhow in bins. ? propagation,
  no unwrap on recoverable errors. Trigger: thiserror, anyhow, unwrap, expect, ?,
  error chain, eyre.'
license: MIT
metadata:
  source-id: igmarin/rust-core-skills:error-handling
  source-commit: f105faa7b2a493bd8434ce7ee99ca3a424b1007a
  kind: atomic
  dependencies: '[]'
---

Resolve skill names through `../../skill-map.json`; use the source pack to disambiguate. Load only the workflow and resources needed for the authorized task.

# Error handling

Apply the [execution contract](../../resources/rust/docs/agent-contract.md) before this procedure.

## Goal

Recoverable failure is `Result`. Panics are bugs, not control flow.

## Inputs / outputs

- In: a fallible operation
- Out: `Result<T, E>` with a useful `E`, or a typed panic only for invariants

## Reads / writes

- Read: the fallible fn and its callers
- Write: none unless a playbook opened the task

## Approval

Adding `thiserror` / `anyhow` if they are not already in `Cargo.toml`.

## RULES — no exceptions

1. Library crates: preserve the existing typed error API; use a small handwritten `enum` or existing `thiserror` dependency implementing `Error` and needed conversions
2. Binary / app crates: use the existing error convention; `anyhow` with `.context()` is an option when already installed, not a required dependency
3. `?` to propagate; `From` impls make `?` work
4. No `.unwrap()` on user/IO/parse paths
5. `.expect("…")` only for proven invariants (a bug if it fires)
6. Messages: lowercase, no trailing punctuation
7. Preserve `source` (`#[source]` / `.context()`)
8. Document `# Errors` on public fallible fns

## Example

```rust
use std::num::NonZeroU16;

// ❌
let n: u16 = s.parse().unwrap();

// ✅ lib
#[derive(Debug, thiserror::Error)]
enum ParsePortError {
    #[error("not a number")]
    Num(#[from] std::num::ParseIntError),
    #[error("port must be non-zero")]
    Zero,
}

fn parse_port(s: &str) -> Result<NonZeroU16, ParsePortError> {
    let n: u16 = s.parse()?;
    NonZeroU16::new(n).ok_or(ParsePortError::Zero)
}
```

## Steps

1. Classify: recoverable vs invariant
2. Recoverable → `Result` + `?`
3. If the crate is a lib, keep `E` typed; if a bin, `anyhow` is enough

## Validation

No new `unwrap`/`expect` on IO/parse. `cargo test` covers the error variant.

## Pitfalls

| ❌ | ✅ |
|----|----|
| `unwrap` in a lib | `?` |
| `expect("failed")` on a missing file | `Err` + context |
| Swallow with `let _ =` | return or log once at the edge |

## Integration

Predecessor: `rust-essentials`. Successor: none.
