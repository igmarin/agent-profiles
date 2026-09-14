---
name: rails-tdd
description: 'Use when running the full Rails TDD loop: failing spec, implement, review,
  PR. Trigger words: TDD, red-green-refactor, write tests first, test-driven.'
license: MIT
metadata:
  source-id: igmarin/rails-agent-skills:tdd
  source-commit: 08661ee9b537444253732d9d353f05fac0ac2f27
  kind: workflow
  dependencies: '["igmarin/rails-agent-skills:load-context", "igmarin/rails-agent-skills:plan-tests",
    "igmarin/rails-agent-skills:write-tests", "igmarin/rails-agent-skills:code-review",
    "igmarin/ruby-core-skills:tdd-process", "igmarin/ruby-core-skills:write-yard-docs"]'
---

Resolve skill names through `../../skill-map.json`; use the source pack to disambiguate. Load only the workflow and resources needed for the authorized task.

# TDD Persona

Apply the [execution contract](../../resources/rails/docs/agent-contract.md) before this procedure.

## Agent Phases

### Phase 1: Context & Test Design
1. **context/load-context**: Load schema, routes, and patterns.
2. **testing/plan-tests**: Choose the best first failing spec.
3. **testing/write-tests**: Write test and verify failure.

**HARD GATE — tdd-process *(from ruby-core-skills)***
- Test EXISTS and is RUN.
- FAILS for correct reason (e.g., `undefined method 'full_name'`).
- If FAIL is incorrect (syntax, config), return to `write-tests`.

### Phase 2: Implementation
1. **Proposal Checkpoint**: Propose implementation (e.g., "Concatenate first + last name").
2. **Scope Check**: Continue within the existing authorized scope.
3. **Minimal Implement**: Smallest change to pass test.
4. **Verify PASS**: `bundle exec rspec spec/path/to/spec.rb`.

*If test does not pass, fix minimal changes and re-verify.*

### Phase 3: Iterate (Optional)
Return to Phase 1 for next behavior or proceed to Phase 4.

### Phase 4: Finish
1. **Quality Check**: `bundle exec rubocop && bundle exec brakeman && bundle exec rspec`.
2. **write-yard-docs *(from ruby-core-skills)***: Document public Ruby API.
3. **code-quality/code-review**: Self-review PR diff.
4. **Open PR**: Feature complete.

## Concrete Example

Abbreviated walkthrough for adding a `full_name` method to a `User` model. For the full end-to-end example, see [../../resources/rails/skills/personas/tdd/assets/example.md](../../resources/rails/skills/personas/tdd/assets/example.md).

**Step 1 — Write the failing spec** (`spec/models/user_spec.rb`):
```ruby
RSpec.describe User, type: :model do
  describe '#full_name' do
    it 'returns first and last name joined by a space' do
      user = User.new(first_name: 'Jane', last_name: 'Doe')
      expect(user.full_name).to eq('Jane Doe')
    end
  end
end
```
Run: `bundle exec rspec spec/models/user_spec.rb`
Expected failure: `NoMethodError: undefined method 'full_name' for #<User ...>` ✅

**Step 2 — State the approach**
> Proposal: Add `def full_name = "#{first_name} #{last_name}"` to `app/models/user.rb`.

**Step 3 — Minimal implementation** (`app/models/user.rb`):
```ruby
def full_name
  "#{first_name} #{last_name}"
end
```
Run: `bundle exec rspec spec/models/user_spec.rb` → `1 example, 0 failures` ✅

**Step 4 — Quality check**:
```bash
bundle exec rubocop && bundle exec brakeman && bundle exec rspec
```
All green → write YARD docs → self-review → open PR.

---

## Output Style

When completing a TDD cycle, produce a report following the template in [../../resources/rails/skills/personas/tdd/assets/tdd-report-template.md](../../resources/rails/skills/personas/tdd/assets/tdd-report-template.md). At minimum the report must include:

- **RED**: spec file path and line, exact failure class and message, confirmation the failure is for the correct reason.
- **Proposal**: one-line implementation summary and the authorization scope.
- **GREEN**: implementation file path and line range, spec pass confirmation.
- **Iterate**: number of additional RED→GREEN cycles and a summary of each.
- **Quality Gate**: RuboCop, Brakeman, full RSpec suite, YARD docs, and self-review results.

---

## Integration

| Predecessor | This Persona | Successor |
|-------------|--------------|----------|
| load-context | tdd | code-review |
| define-domain-language | tdd | quality |
| None (standalone) | tdd | PR submission |

**Use `plan-tests` alone** if you only need to decide which test to write next.

**Use `write-tests` alone** if the test design is already decided and you only need to implement the spec.

---

## Error Recovery

**Test fails for the wrong reason (syntax/config error):**
1. Identify error class — `SyntaxError`, `NameError`, `LoadError` indicate test problems, not missing features.
2. Fix the test to correctly target the missing behavior and re-run until the failure class is correct (e.g., `NoMethodError`).

**Implementation makes test pass but breaks other tests:**
1. Run `bundle exec rspec` to identify regressions.
2. Revise implementation to satisfy both the new test and existing tests.
3. If impossible, the feature conflicts with existing behavior — discuss with user before proceeding.

**Quality gate fails (RuboCop/Brakeman):**
1. Run `bundle exec rubocop -a` for auto-correctable offenses; fix remaining ones manually.
2. For Brakeman warnings, assess whether they are false positives — if real, fix before proceeding.
