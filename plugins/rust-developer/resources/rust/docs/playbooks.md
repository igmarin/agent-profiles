# Playbooks

Sequenced workflows with hard gates and HITL. They load atomics; they do not re-teach FCIS.

Quality commands: `docs/skill-authoring.md`.

## Written

| Playbook | Path | Gate |
|----------|------|------|
| `tdd` | `skills/tdd/` | RED `cargo test <test_name> -- --exact` → user approves → green → quality commands |

## Not written

Do not load these. When added, `name` must match the directory (`skills/<name>/SKILL.md`).

| Planned id | Intended path | Gate (when written) |
|------------|---------------|---------------------|
| `bug-fix` | `skills/bug-fix/` | Repro test first |
| `quality` | `skills/quality/` | quality commands; `cargo deny` if `deny.toml` exists |
| `code-review-playbook` | `skills/code-review-playbook/` | Critical/Major/Minor; tests for new logic |
| `setup` | `skills/setup/` | toolchain, MSRV, fmt/clippy, CI |
| `new-crate` | `skills/new-crate/` | lib vs bin, workspace, public API, rustdoc |
| `unsafe-change` | `skills/unsafe-change/` | `# Safety` + `// SAFETY:` + Miri before merge |

Until those exist, the router uses `rust-essentials` and `tdd`.
