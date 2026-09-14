# FCIS for Rust

Pragmatic functional programming. Not Haskell-in-Rust.

```text
skip it → reuse in-crate → std → existing Cargo.toml dep → one line → minimum that works
```

Never skip: parse at the trust boundary, `Result` for recoverable failure, `// SAFETY:` on unsafe, a failing test for non-trivial logic.

## Explicit rejects

- Monad / HKT / category-theory crates
- `RefCell` / `Mutex` as the default (last resort)
- Clone to silence the borrow checker
- `unwrap` / `expect` for recoverable errors
- Avoiding `&mut` in a clearly local in-place algorithm

---

## 1. Functional core, imperative shell

Pure functions for rules and transforms. IO, clocks, process, network only at the edge.

```rust
// ❌ mixed
fn checkout(id: OrderId, db: &Db) -> Result<Charge, Error> {
    let order = db.load(id)?;
    let total = order.lines.iter().map(|l| l.amount).sum();
    db.charge(id, total)
}

// ✅
fn total(lines: &[Line]) -> Money {
    lines.iter().map(|l| l.amount).sum()
}

fn checkout(id: OrderId, db: &Db) -> Result<Charge, Error> {
    let order = db.load(id)?;
    db.charge(id, total(&order.lines))
}
```

## 2. Illegal states unrepresentable

Enums and newtypes, not booleans and strings. Parse once at the boundary (`TryFrom` / `FromStr`). Downstream takes the validated type.

## 3. `Result` + `?`

Fallible work returns `Result<T, E>`. Chain with `?`. Combinators (`map`, `and_then`, `map_err`) when they shorten the function. No custom railway crate.

## 4. Iterators over index loops

`iter` / `map` / `filter` / `fold` / `zip`. Index only for non-sequential access. Collect once, at the end.

## 5. Pattern match over nested `if`

`match`, `let-else`, `if let` chains. Exhaustive on *your* enums — no `_` that hides a new variant.

## 6. Immutability by default

Locals stay binding-immutable unless mutation is local and obvious. Interior mutability is a last resort, documented.

---

Idiomatic Rust wins. A tight `&mut` loop that is clearly local is better than a clever clone-heavy “pure” rewrite.
