# Agent Profiles

Ready-made developer roles built from five skill packs I maintain separately:
planning, Elixir/Phoenix, Ruby core, Rails, and Rust core. Each role picks the
smallest workflow that fits the task, follows the target project's conventions,
and backs up its work with test output you can check.

## Install a bundle

Pick the bundle that matches your stack. Each folder under `plugins/` works on
its own with Devin or Codex.

| Bundle | You get | Built from |
| --- | --- | --- |
| `project-planning` | product-owner, project-manager, tech-lead, delivery-lead | planning |
| `elixir-developer` | elixir-developer | planning, Elixir/Phoenix |
| `ruby-developer` | ruby-developer, rails-developer | planning, Ruby core, Rails |
| `rust-developer` | rust-developer | planning, Rust core |

Copy the bundle folder into your host's plugin directory, then point the agent
at it. To use a skill inside a bundle, look up its path in that bundle's
`skill-map.json` and read the `SKILL.md` it points to. `provenance.json` shows
which source commits the bundle was built from. `migration.json` maps old
unqualified skill names to their current qualified names.

## Compose a new role

This repo owns role composition. The five source repos own skill content, so
start there if you want to change what a skill teaches. To change which skills
a role uses:

1. Edit the role file in `roles/` or the pack list in `profiles.json`.
2. Rebuild the bundles: `uv run python scripts/profiles.py build`
3. Run the checks: `uv run python scripts/profiles.py validate`,
   `check-exports`, `routing`, then `uv run python -m unittest discover -s tests -v`
4. Commit `profiles.json`, `roles/`, and the rebuilt `plugins/` together.

`build --working-tree` skips the pinned-commit check so you can iterate
locally. Release builds use the exact commits in `profiles.json` and fail if a
source checkout is dirty. Never hand-edit files under `plugins/`; they get
overwritten on the next build.

## Checks

`uv sync` installs the one dependency (PyYAML). Then:

```bash
uv run python scripts/profiles.py validate
uv run python scripts/profiles.py build
uv run python scripts/profiles.py check-exports
uv run python scripts/profiles.py routing
uv run python -m unittest discover -s tests -v
```

CI splits this into two jobs. `unit` runs the Python tests without any source
packs. `pinned build` clones each source pack at its pinned commit, validates,
rebuilds, and fails if the committed `plugins/` differ from a clean build. A
weekly watcher opens a PR when a source pack moves past its pin.

## Evaluation policy

Structural, routing, resource-closure, and installation checks run without a
model. Anything that needs a model waits until the batch has a written token
or cost cap. Keep each finished batch under `reports/`: fixtures, repeated
runs, host and model versions, source commits, usage, raw results, and what
the batch did not cover. If a batch is missing or inconclusive, say so. Do not
present it as an improvement.

## Migration and rollback

Keep using a short skill name while it maps to exactly one skill. Switch to
the qualified form (`pack:skill`) once two packs use the same name. To roll
back, install the earlier bundle and check out the source commits listed in
that bundle's `provenance.json`. Do not mix skills from different bundle
versions.

