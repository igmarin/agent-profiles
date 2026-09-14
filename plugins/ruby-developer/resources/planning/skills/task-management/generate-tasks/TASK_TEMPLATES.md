# Task List Template

```markdown
# Task List: [Feature Name]

Based on: `prd-[feature-name].md`

## Relevant Files

- `path/to/file.ext` — Description of relevance.
- `path/to/file.test.ext` — Test coverage.

## Tasks

- [ ] 0.0 Create feature branch: `git checkout -b feature/[feature-name]`
- [ ] 1.0 Core Behavior (TDD Quadruplet)
  - [ ] 1.1a Write failing test for [behavior] (`<test-dir>/path/to/test.ext`)
  - [ ] 1.1b Run test command — verify failure
  - [ ] 1.1c Implement behavior to pass test (`<source-dir>/path/to/file.ext`)
  - [ ] 1.1d Run test command — verify success
- [ ] 2.0 API Documentation & Code Review
  - [ ] 2.1 Document public API methods
  - [ ] 2.2 Self-review diff before PR
```
