# Test Command Lookup Table

| Config File / Indicator | Detection Command | Test Command |
|---|---|---|
| `package.json` with `test` script | `jq '.scripts.test' package.json` | `npm test` (or `yarn test` / `pnpm test`) |
| `Cargo.toml` | `test -f Cargo.toml` | `cargo test` |
| `Gemfile` + rspec | `grep -q rspec Gemfile` | `bundle exec rspec` |
| `go.mod` | `test -f go.mod` | `go test ./...` |
| `pyproject.toml` + pytest | `grep -q pytest pyproject.toml` | `pytest` |
| `Makefile` with test target | `grep -q '^test:' Makefile` | `make test` |
| Fallback | — | Default test suite for detected language |
