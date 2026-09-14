# Agent Profiles

Portable developer roles assembled from the authoritative planning, Elixir,
Ruby, Rails, and Rust skill packs. A role chooses the smallest relevant
workflow, preserves project conventions, and finishes authorized work with
real verification evidence.

## Bundles

| Bundle | Roles | Source packs |
| --- | --- | --- |
| `project-planning` | product-owner, project-manager, tech-lead, delivery-lead | agnostic planning |
| `elixir-developer` | elixir-developer | planning, Elixir/Phoenix |
| `ruby-developer` | ruby-developer, rails-developer | planning, Ruby core, Rails |
| `rust-developer` | rust-developer | planning, Rust core |

`plugins/` contains self-contained Devin and Codex-compatible bundles.
`skill-map.json` resolves every qualified source identity to its exported skill;
`provenance.json` records source commits and file hashes. `migration.json`
keeps unambiguous legacy names for one major release and records collisions.

## Build and validate

```bash
uv sync
uv run python scripts/profiles.py validate
uv run python scripts/profiles.py build
uv run python scripts/profiles.py check-exports
uv run python -m unittest discover -s tests -v
```

Release builds require clean source content at the exact commits in
`profiles.json`. `build --working-tree` is only for local authoring.

## Evaluation policy

Structural, routing, resource-closure, and installation checks run without a
model. Behavioral evaluation batches are manual until each batch has an
explicit token or cost cap. Store a completed batch's fixtures, repeated runs,
host/model versions, source commits, usage, raw results, and limitations under
`reports/`. A missing or inconclusive batch is reported as such, never as an
improvement claim.

## Migration and rollback

Keep using source-pack names and paths while their alias is unambiguous. Use
the qualified identity when two packs expose the same name. Roll back by
installing the earlier bundle revision and its recorded source commits; do not
mix generated resources from different bundle versions.
