# Agent Profiles

The five specialist repositories own skill content. This repository owns role
composition, native exports, and cross-pack proof. Edit `roles/` or `profiles.json`,
then regenerate `plugins/`; generated skill copies are not independent sources.

Use `uv run python scripts/profiles.py --help` for build and validation commands.
Run `uv run python -m unittest discover -s tests -v` before committing.
Paid evaluations require an explicit batch usage cap. Record unrun checks as unrun.

Prefer standard-library functions and native host features. Add no agent runtime,
MCP service, model override, or permission override to make a role work.
Keep contributor instructions out of plugin-root AGENTS.md files.
