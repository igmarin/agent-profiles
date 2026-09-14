---
name: ownership-borrowing
type: atomic
tags: [atomic]
license: MIT
description: >
  Borrow before clone. Accept &[T]/&str. Arc vs Rc. Interior mutability last.
  Trigger: clone, borrow, lifetime, Arc, Rc, RefCell, Mutex, Cow, ownership.
metadata:
  version: "1.0.0"
  user-invocable: "true"
---

# Ownership and borrowing

Apply the [execution contract](../../docs/agent-contract.md) before this procedure.

## Goal

No allocation that a borrow would cover. Shared mutability only when the type system requires it.

## Inputs / outputs

- In: a function or type that owns or shares data
- Out: API that takes the least ownership it needs

## Reads / writes

- Read: the function and its callers
- Write: none unless a playbook opened the task

## Approval

None to drop clones. State lifecycle and concurrency cost before adding `Arc`, `Rc`, `Mutex`, `RwLock`, or `RefCell`; stop for approval if that choice changes the accepted design or scope.

## RULES — no exceptions

1. Prefer `&T` / `&mut T` over `.clone()`
2. Accept `&[T]` not `&Vec<T>`; `&str` not `&String`
3. `Cow<'_, T>` only when you sometimes own
4. `Arc<T>` across threads; `Rc<T>` single-thread only
5. `RefCell` / `Mutex` / `RwLock` last; document why
6. `Copy` for tiny, obviously copyable types; otherwise explicit `Clone`
7. Move large values; `Box` if the move itself is the cost
8. Elide lifetimes until the compiler asks

## Example

```rust
// ❌
fn count_words(text: &String) -> usize {
    text.clone().split_whitespace().count()
}

// ✅
fn count_words(text: &str) -> usize {
    text.split_whitespace().count()
}
```

Clone is justified when storing, sending `'static` to a thread, or the type is `Copy`.

## Steps

1. Grep the touched fn for `.clone(`
2. If the clone is not stored or sent, borrow
3. Widen params to slices/str

## Validation

`cargo test` on the crate (or `cargo test <test_name> -- --exact` if a test is already red). Diff should drop clones or justify each remainder in one comment.

## Pitfalls

| ❌ | ✅ |
|----|----|
| `data.clone()` to call a reader | pass `&data` |
| `Mutex` for a single-thread cache | `RefCell` or, better, owned local |
| Lifetime soup | elide; name only `'src` / `'a` when needed |

## Integration

Predecessor: `rust-essentials`. Successor: `type-driven-design`. Do not hold a lock across `.await`.
