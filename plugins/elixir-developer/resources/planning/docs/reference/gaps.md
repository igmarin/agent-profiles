# Gaps

What this pack does not cover yet, and known drift.

## Missing skills

Do not add these in the same change as a quality pass.

| Gap | Why it matters | Notes |
|-----|----------------|-------|
| Dedicated CI/CD planning skill | Teams ask how to stand up pipelines. | Register only. `setup-ci-cd`-style work is out of this pack's current catalog. |
| Tracker automation beyond draft `github-issue` | Jira/Linear create-and-sync is requested often. | `plan-tickets` stays draft-only unless the user asks. `github-issue` is GitHub-only. |
| Formal estimation calibration / planning poker | `estimate-tasks` assigns relative size; it does not run a ceremony. | — |
| Release / launch checklist | Delivery-lead stops at retrospective. | — |

## Drift

| Item | Status |
|------|--------|
| Description contract | When + triggers, target ≤ 600 chars, spec ceiling 1024. Opposite of `ruby-core-skills/docs/skill-description-strategy.md` Rule 1 (“pack every hard rule into one period-free sentence”). |
| Host context | `AGENTS.md` is the source. `CLAUDE.md` is a stub. `GEMINI.md` is absent. |
| Evals | No `personal-evals/` in this repo. Do not import core or rails evals. |
| `rs-guard` on Dependabot PRs | That job needs `DEEPSEEK_API_KEY`. Missing secret on fork/Dependabot PRs is GitHub, not a pack bug. Do not “fix” with `pull_request_target`. |
| `.claude/worktrees/` | Leftover copies if present. Not in `directory.json`. Ignore. |

## Description strategy conflict

`ruby-core-skills` still tells authors to pack every hard rule into sentence one. This repo does not. Follow-up: amend that rule in core so authors do not revert slim descriptions here.

## CI

Catalog checks live in `scripts/validate-skills.sh` and `.github/workflows/ci.yml`. There is no eval validator because there are no evals.
