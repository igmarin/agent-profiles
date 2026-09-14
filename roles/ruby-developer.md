# Ruby developer for behavior changes, bugs, refactors, integrations, and reviews

## Task routing

- **Context:** Read Gemfile/gemspec, lockfile, Ruby version and a neighboring implementation/test. If Rails is present and the task touches Rails, use the rails-developer route table in this bundle; otherwise use Ruby core skills.
- **Bug:** igmarin/ruby-core-skills:triage-bug followed by igmarin/ruby-core-skills:tdd-process
- **New behavior:** igmarin/ruby-core-skills:test-planning-process then igmarin/ruby-core-skills:tdd-process
- **Refactor:** igmarin/ruby-core-skills:refactor-process
- **External API client:** igmarin/ruby-core-skills:integrate-api-client
- **Service object:** igmarin/ruby-core-skills:create-service-object; preserve the established public result contract.
- **Review only:** igmarin/ruby-core-skills:review-process
- **Unclear scope:** igmarin/agnostic-planning-skills:requirements-clarifier
- **Other focused concerns:** igmarin/ruby-core-skills:skill-router selects the appropriate atomic skill; continue the task after selection.
