---
name: rails-create-engine
description: 'Use when scaffolding a new Rails engine. Keep a narrow public API and
  a dummy app. Trigger words: create engine, new engine, mountable engine.'
license: MIT
metadata:
  source-id: igmarin/rails-agent-skills:create-engine
  source-commit: 9c639c4de86a88075d78094bbeee203be8356cc1
  kind: atomic
  dependencies: '[]'
---

Resolve skill names through `../../skill-map.json`; use the source pack to disambiguate. Load only the workflow and resources needed for the authorized task.

# Create Engine

Apply the [execution contract](../../resources/rails/docs/agent-contract.md) before this procedure.

Use this skill when the task is to create, scaffold, or refactor a Rails engine, Rails plugin, or engine gem.

Keep this skill focused on structure and design. Use adjacent skills for installer details, deep test coverage, release workflow, or documentation work.

## Quick Reference

| Engine Type | When to Use |
|-------------|-------------|
| Plain gem | No Rails hooks or app directories needed; pure Ruby library |
| Railtie | Needs Rails initialization hooks but not models/controllers/routes/views |
| Engine | Needs Rails autoload paths, initializers, migrations, assets, jobs, or host integration |
| Mountable engine | Needs its own routes, controllers, views, assets, and namespace boundary |

## HARD-GATE

```text
Before engine work is complete, confirm all of the following:

STRUCTURE & CONTRACT:
1. Root file requires only version, configuration, and engine.
2. Public engines use isolate_namespace; configuration exposes .configure block.
3. Host model references are configurable strings (e.g., "User"), never hard-coded ::User.
4. Host-app contract is documented (see Host App Contract section).

SAFETY CHECKS:
5. Engine code never auto-applies migrations at boot (no db:migrate, ActiveRecord::Migrator, or config.paths['db/migrate'] in initializers).
6. Initializers are idempotent and safe in development reloads.
7. Assets and generators are namespaced and idempotent.

VERIFICATION COMMANDS:
8. Dummy app exists: `ls spec/dummy` or `ls test/dummy` should return the app directory.
9. Integration tests pass: `bundle exec rspec` or `bundle exec rake test` exits 0.
10. Routes load correctly: `bundle exec rails routes` inside dummy app shows engine routes.
11. No hard-coded host constants: `grep -r "::User\|::Employee" lib/ app/` returns nothing.
12. No migration auto-apply patterns: `grep -r "db:migrate\|ActiveRecord::Migrator\|config.paths\['db/migrate'\]" lib/` returns nothing.
```

## Core Process

1. Identify the engine type before writing code. Scaffold with the correct generator:
   ```bash
   rails plugin new my_engine --mountable   # mountable engine
   rails plugin new my_engine --full        # full engine (non-isolated)
   rails plugin new my_engine               # plain Railtie/gem
   ```
2. Define the host-app contract (what the host must provide, what the engine exposes, which extension points are supported). See [../../resources/rails/skills/create-engine/reference.md](../../resources/rails/skills/create-engine/reference.md) for the full contract template.
3. Create the minimal engine structure. **Checkpoint:** `bundle exec rake` inside the engine must pass.
4. Implement features behind the namespace. **Checkpoint:** mount engine in dummy app routes and verify with `bundle exec rails routes`.
5. Write minimum integration coverage through the dummy app. See [../../resources/rails/skills/create-engine/TESTING.md](../../resources/rails/skills/create-engine/TESTING.md) for coverage requirements.
6. Document the host-app contract clearly enough for follow-on work.

If the user does not specify the engine type, infer it from the requested behavior and say which type you chose.

## Extended Resources

- [../../resources/rails/skills/create-engine/reference.md](../../resources/rails/skills/create-engine/reference.md) — full host-app contract template, recommended file structure, and code scaffolding examples
- [../../resources/rails/skills/create-engine/EXAMPLES.md](../../resources/rails/skills/create-engine/EXAMPLES.md) — extended engine examples
- [../../resources/rails/skills/create-engine/TESTING.md](../../resources/rails/skills/create-engine/TESTING.md) — coverage requirements and dummy app setup
- [../../resources/rails/skills/create-engine/assets/examples.md](../../resources/rails/skills/create-engine/assets/examples.md)
- [../../resources/rails/skills/create-engine/assets/release-checklist.md](../../resources/rails/skills/create-engine/assets/release-checklist.md)

## Output Style

When asked to create or scaffold a Rails engine, your output `answer.md` MUST follow this style:

1. **Concrete Artifact Files**: Display the full generated `.gemspec` and `Rakefile` contents, correctly namespaced under the engine namespace.
2. **Verification & Rake Status**: Explicitly state that `bundle exec rake` inside the engine passes (exits 0), with a simulated passing output block.
3. **Integration Test Coverage**: Write integration specs covering configuration, routing, HTTP request flow, domain services, and host-integration hooks. See [../../resources/rails/skills/create-engine/TESTING.md](../../resources/rails/skills/create-engine/TESTING.md) for the required spec categories and paths. Keep unit tests for models/services separate from request/integration specs.
4. **Language**: Must be in English unless explicitly requested otherwise.

## Integration

| Skill | When to chain |
|-------|----------------|
| test-engine | Dummy app setup, integration tests, regression coverage |
| review-engine | Findings-first audits, structural review |
| document-engine | README, installation guide, host-app contract documentation |
| create-engine-installer | Generator-heavy setup, install scripts, copy migrations |
| generate-api-collection | When the engine exposes HTTP endpoints (generate/update Postman collection) |
