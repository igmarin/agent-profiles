---
name: rust-rust-essentials
description: 'MANDATORY before any .rs write. FCIS, ponytail ladder, parse-at-boundary,
  Result + ?, iterators, match, naming. Trigger: rust, FCIS, idiomatic rust, ownership
  intro, Result, newtype, clippy.'
license: MIT
metadata:
  source-id: igmarin/rust-core-skills:rust-essentials
  source-commit: f105faa7b2a493bd8434ce7ee99ca3a424b1007a
  kind: atomic
  dependencies: '[]'
---

Resolve skill names through `../../skill-map.json`; use the source pack to disambiguate. Load only the workflow and resources needed for the authorized task.

# Rust essentials

Apply the [execution contract](../../resources/rust/docs/agent-contract.md) before this procedure.

Canonical: [`docs/fcis-rust.md`](../../resources/rust/docs/fcis-rust.md)

## Goal

Every `.rs` change follows FCIS and the ponytail ladder.

## Inputs / outputs

- In: current crate + the behaviour to change
- Out: Rust that compiles, no extra crates, illegal states unrepresentable

## Reads / writes

- Read: `Cargo.toml`, files the task already opened, `docs/fcis-rust.md` in this pack
- Write: none unless a playbook opened the task

## Approval

Adding a dependency, `unsafe`, or toolchain install.

## RULES — no exceptions

1. Apply [`docs/fcis-rust.md`](../../resources/rust/docs/fcis-rust.md) (ladder + six FCIS rules). Do not restate them here.
2. **Names:** types `UpperCamelCase`, fns `snake_case`, consts `SCREAMING_SNAKE`; acronyms as words (`HttpServer`)
3. **Never skip:** trust-boundary parse, `Result`, `// SAFETY:`, one failing test for non-trivial logic

## Example

```rust
// ❌
fn bind(port: u16) -> std::net::SocketAddr {
    format!("127.0.0.1:{port}").parse().unwrap()
}

// ✅
use std::net::{Ipv4Addr, SocketAddr, SocketAddrV4};
use std::num::NonZeroU16;

fn bind(port: NonZeroU16) -> SocketAddr {
    SocketAddr::V4(SocketAddrV4::new(Ipv4Addr::LOCALHOST, port.get()))
}
```

## Steps

1. Load this skill + `docs/fcis-rust.md`
2. If the crate exists, run `load-context` first
3. Apply RULES to the diff; do not add types/traits “for later”

## Validation

RED: `cargo test <test_name> -- --exact`. Done: commands in `docs/skill-authoring.md` (fmt, clippy `--all-targets -D warnings`, `cargo test`). No new deps. No `unwrap` on recoverable paths.

## Pitfalls

| ❌ | ✅ |
|----|----|
| New crate for what `std` does | `std` / existing dep |
| `bool` pairs for states | `enum` |
| Clone to please borrowck | restructure or borrow |
| Essay comments | the type and the test |

## Integration

| Predecessor | This | Successor |
|-------------|------|-----------|
| `load-context` | rust-essentials | `ownership-borrowing`, `type-driven-design`, `error-handling` |
| playbook `tdd` | rust-essentials | implementation after RED |
