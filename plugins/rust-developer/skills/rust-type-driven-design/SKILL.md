---
name: rust-type-driven-design
description: 'Make illegal states unrepresentable: newtypes, enums, typestate, TryFrom
  at the boundary. Trigger: newtype, parse don''t validate, enum state, NonZero, typestate,
  validated type.'
license: MIT
metadata:
  source-id: igmarin/rust-core-skills:type-driven-design
  source-commit: d27b83055ce5a78253adb550b49380ab67190d9b
  kind: atomic
  dependencies: '[]'
---

Resolve skill names through `../../skill-map.json`; use the source pack to disambiguate. Load only the workflow and resources needed for the authorized task.

# Type-driven design

Apply the [execution contract](../../resources/rust/docs/agent-contract.md) before this procedure.

## Goal

Invalid data cannot be constructed past the crate boundary.

## Inputs / outputs

- In: raw input (CLI, config, JSON, `u16`, `&str`)
- Out: a type whose constructor is the validation

## Reads / writes

- Read: call sites of the untyped value
- Write: none unless a playbook opened the task

## Approval

Public API type changes (semver).

## RULES — no exceptions

1. Parse into a validated type at the edge; inner code takes that type
2. Newtype IDs (`UserId(u64)`), not raw integers mixed with other IDs
3. Enums for mutually exclusive states; never `is_ready: bool` + `result: Option<T>` for the same machine
4. `Option` = absence; `Result` = failure — do not mix
5. `TryFrom` / `FromStr` for fallible parse; `From` for infallible
6. `NonZero*` when zero is illegal
7. Typestate only when the compiler must block a call; otherwise an enum is enough
8. No stringly APIs (`"admin"` vs `Role::Admin`)

## Example

```rust
use std::num::NonZeroU16;

struct ServicePort(NonZeroU16);
enum PortError { Zero }

// ❌
fn listen(_port: u16) {}

// ✅
fn listen(_port: ServicePort) {}

impl TryFrom<u16> for ServicePort {
    type Error = PortError;
    fn try_from(n: u16) -> Result<Self, Self::Error> {
        NonZeroU16::new(n).map(Self).ok_or(PortError::Zero)
    }
}
```

## Steps

1. Name the invariant (non-zero, one of N roles, not both loading and loaded)
2. Put it in a type
3. Change the function signature; delete scattered `if invalid`

## Validation

Callers no longer compile if they pass raw unparsed input. Run `cargo test` covering `TryFrom`/`FromStr` error cases (`Ok` for valid, `Err` for zero/empty/invalid).

## Pitfalls

| ❌ | ✅ |
|----|----|
| `Port(0)` via `Option` later | `NonZeroU16` |
| Validate in every fn | parse once |
| Typestate for two states | `enum` |

## Integration

Predecessor: `rust-essentials`. Successor: `error-handling`.
