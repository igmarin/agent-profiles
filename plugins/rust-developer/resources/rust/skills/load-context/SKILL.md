---
name: load-context
type: atomic
tags: [atomic]
license: MIT
description: >
  MANDATORY on an existing crate before code, tests, or review. Read Cargo.toml,
  toolchain, one neighbor module and its test. Cite paths. Trigger: load context,
  existing crate, before I code, workspace, rustc version.
metadata:
  version: "1.0.0"
  user-invocable: "true"
---

# Load context

Apply the [execution contract](../../docs/agent-contract.md) before this procedure.

## Goal

Match the crate in front of you, not a generic tutorial.

## Inputs / outputs

- In: project root of the user’s crate
- Out: Context Summary (template below). Confusion Block if two patterns conflict.

## Reads / writes

- Read: `Cargo.toml`, `Cargo.lock` if present (versions only), `rust-toolchain.toml` if present, `src/lib.rs` or `src/main.rs`, one sibling module, one sibling test
- Write: none

## Approval

None. Read-only.

## RULES — no exceptions

1. Do not propose code or tests until the Context Summary is posted
2. Do not read the whole repo — `Cargo.toml` + toolchain + one neighbor + its test
3. Cite real paths
4. On two conflicting patterns, post a Confusion Block and wait — do not pick silently

## Steps

1. Name the layer in one line (lib API, bin/clap, async task, unsafe, workspace crate).
2. Read `Cargo.toml`: edition, `rust-version`, bins/libs, features, relevant deps.
3. Read `rust-toolchain.toml` or note “stable unspecified.”
4. Open one neighbor that already solves a similar problem, and its test (`src/…`, `tests/…`, or `#[cfg(test)]`).
5. Post the summary. If two patterns conflict, stop with a Confusion Block — do not pick silently.

## Validation

Summary cites real paths. No code in the same message unless the user already approved skipping this skill or the selected workflow is already authorized.

## Output

```text
### Context Summary
**Layer:** <lib | bin | workspace member | test | build.rs>
**Cargo:** edition=<…>; rust-version=<… or none>; bins/libs=<…>
**Deps that matter:** <name ver — why>
**Neighbor:** <path> — <one convention>
**Test neighbor:** <path> — <how they assert>
**Drift:** <none | spec vs code>
**Next:** <tdd | rust-essentials>
```

### Confusion Block

```text
### Confusion Block
**Conflict:** <path A> does X; <path B> does Y
**Options:** <A> | <B>
**Question:** which pattern should this change follow?
```

Wait for an explicit answer. Do not implement.

## Pitfalls

| ❌ | ✅ |
|----|----|
| Dump `src/` | one neighbor |
| Assume tokio/clap exist | read `Cargo.toml` |
| Start coding | summary first |

## Integration

Always first on an existing crate. Successor: playbook `tdd`, then `rust-essentials`.
