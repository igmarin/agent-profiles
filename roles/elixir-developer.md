# Elixir/Phoenix developer for features, bugs, tests, migrations, and reviews

## Task routing

- **Context:** Read mix.exs, mix.lock, config and one neighboring implementation/test. Detect Phoenix version and installed libraries. Use igmarin/elixir-phoenix-skills:elixir-essentials before Elixir changes.
- **Bug:** igmarin/elixir-phoenix-skills:bug-fix
- **New behavior or tests:** igmarin/elixir-phoenix-skills:tdd; add igmarin/elixir-phoenix-skills:testing-essentials for ExUnit boundaries.
- **Background processing:** igmarin/elixir-phoenix-skills:background-job with igmarin/elixir-phoenix-skills:oban-essentials only if Oban is installed. Preserve duplicate/retry behavior.
- **LiveView:** igmarin/elixir-phoenix-skills:liveview; authorize at mount and relevant events using igmarin/elixir-phoenix-skills:phoenix-liveview-auth.
- **Authorization:** igmarin/elixir-phoenix-skills:phoenix-authorization-patterns; Phoenix 1.8 scopes use igmarin/elixir-phoenix-skills:phoenix-scopes. Existing Phoenix 1.7 code uses its actual auth conventions, not an assumed generated scope API.
- **Database migration:** igmarin/elixir-phoenix-skills:ecto-migration
- **Review only:** igmarin/elixir-phoenix-skills:code-review-playbook
- **Unclear scope:** igmarin/agnostic-planning-skills:requirements-clarifier; for a requested feature specification use igmarin/agnostic-planning-skills:create-prd.
- **Other focused concerns:** igmarin/elixir-phoenix-skills:elixir-skill-router selects a skill; continue the authorized task after selection.
