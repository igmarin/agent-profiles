# Agnostic Planning Skills

12 language-agnostic planning skills and 4 personas. Agents use them to write PRDs, break down work, estimate, rank a backlog, plan a sprint, run a retro, and track execution — without tying the process to a stack.

```text
Use an approved PRD or concrete user-authorized brief as scope. Small bugs and local fixes go directly to the stack workflow; create a PRD when product scope needs discovery.
```

Process skills (TDD gates, review, DDD) live in [`ruby-core-skills`](https://github.com/igmarin/ruby-core-skills). After a plan is approved, hand off to a stack pack such as [`rails-agent-skills`](https://github.com/igmarin/rails-agent-skills).

```mermaid
flowchart LR
  A[Vague ask] --> B[requirements-clarifier]
  B --> C[create-prd]
  C --> D{PRD approved?}
  D -->|no| C
  D -->|yes| E[generate-tasks]
  E --> F[plan-tickets]
  F -.-> G[github-issue]
```

```mermaid
flowchart TB
  subgraph thisRepo[agnostic-planning-skills]
    atomics[12 atomics]
    personas[4 personas]
  end
  core[ruby-core-skills]
  stack[stack pack]
  thisRepo --> core
  thisRepo --> stack
```

Also in the same ecosystem: [`hanakai-yaku`](https://github.com/igmarin/hanakai-yaku), [`agent-mcp-runtime`](https://github.com/igmarin/agent-mcp-runtime), [`ruby-skill-bench`](https://github.com/igmarin/ruby-skill-bench).

## Catalog

| Skill | Area |
|-------|------|
| `create-prd`, `review-prd` | PRD |
| `generate-tasks`, `plan-tickets`, `estimate-tasks` | Task management |
| `prioritize-backlog` | Backlog |
| `plan-sprint`, `create-retrospective` | Ceremony |
| `identify-risks`, `generate-status-report` | Execution |
| `requirements-clarifier` | Analysis |
| `github-issue` | GitHub issues |
| `product-owner`, `project-manager`, `tech-lead`, `delivery-lead` | Personas |

Full list: [docs/reference/skill-catalog.md](docs/reference/skill-catalog.md). Gaps: [docs/reference/gaps.md](docs/reference/gaps.md).

Name a persona when you want the whole chain: `product-owner` (scope → tickets), `tech-lead` (feasibility), `project-manager` (execution health), `delivery-lead` (PRD through retro).

## Install

```bash
# Install ALL skills and personas (non-interactive)
npx skills add igmarin/agnostic-planning-skills --full-depth --all

# Interactive: pick which skills to install (multi-select picker)
npx skills add igmarin/agnostic-planning-skills
```

Or with GitHub CLI v2.90.0+ (`gh skill`):

```bash
gh skill install igmarin/agnostic-planning-skills
gh skill install igmarin/agnostic-planning-skills create-prd --scope project
```

> **`--full-depth` is required.** The root `SKILL.md` is a catalog (`type: catalog`), not a standalone skill. Without `--full-depth`, the `skills` CLI treats that root file as the only skill for the repo and stops — you get 1 skill (the catalog) instead of all 16. `--full-depth` makes the CLI recurse into `skills/<category>/<name>/`.
>
> Without `--all`, the CLI opens an interactive multi-select picker listing all 16 skills. Omit `--all` when you want to choose a subset.

## Docs

| Need | Document |
|------|----------|
| Host context | [AGENTS.md](AGENTS.md) |
| How to invoke a persona | [docs/persona-guide.md](docs/persona-guide.md) |
| Skill layout | [docs/architecture.md](docs/architecture.md) |
| How skills chain | [docs/reference/integration-matrix.md](docs/reference/integration-matrix.md) |

## Contributing

- Artifacts in English unless the user asks otherwise.
- Keep scope authorization and evidence gates; a small fix does not require a PRD.
- `description` is when + triggers (≤ 600 chars). Procedure stays in the body.
- Keep public docs in sync with `directory.json`.
