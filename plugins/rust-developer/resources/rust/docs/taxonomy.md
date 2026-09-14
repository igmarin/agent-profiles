# Taxonomy

See [architecture.md](architecture.md) for SKILL.md conventions and [index.md](index.md) for navigation.

Physical layout is **flat** so `npx skills add` lists each skill:

```text
skills/<skill-name>/SKILL.md
```

Logical groups (Rust Core, Playbooks, …) live in `skills.sh.json`, not in nested folders. Do not add a root `SKILL.md` — the skills CLI then installs the repo as one skill and skips `skills/`.

| Kind | `type` | Role |
|------|--------|------|
| Atomic | `atomic` | One domain: rules + one example pair + gates |
| Playbook | `playbook` | Phases, hard gates, HITL; loads atomics |
| Orchestrator | `orchestrator` | Routes; never implements |

A folder is only loadable when it contains `SKILL.md` and is a `directory.json` key. Empty planned folders are not skills.

Playbooks do not re-teach atomics. Atomics do not re-teach `docs/fcis-rust.md`.
