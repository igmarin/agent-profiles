---
name: rails-implement-background-job
description: 'Use when adding or reviewing an Active Job / Sidekiq / Solid Queue worker.
  Cover idempotency, retry_on, and discard_on. Trigger words: background job, Active
  Job, Sidekiq, Solid Queue, worker.'
license: MIT
metadata:
  source-id: igmarin/rails-agent-skills:implement-background-job
  source-commit: 08661ee9b537444253732d9d353f05fac0ac2f27
  kind: atomic
  dependencies: '[]'
---

Resolve skill names through `../../skill-map.json`; use the source pack to disambiguate. Load only the workflow and resources needed for the authorized task.

# Implement Background Job

Apply the [execution contract](../../resources/rails/docs/agent-contract.md) before this procedure.

Use this skill when the task is to add, configure, or review background jobs in a Rails application.

## HARD-GATE

```text
EVERY job MUST have its test written and validated BEFORE implementation:
  1. Write the job spec (idempotency, retry, error handling)
  2. Run the spec — verify it fails
  3. ONLY THEN write the job class

The authoritative perform contract — EVERY perform method does exactly three things:
  1. Load the record from the passed ID
  2. Guard for idempotency / permanent no-op conditions
  3. Delegate the side effect or orchestration to a service object

If perform needs more than that, extract a service.
EVERY job that performs a side effect (charge, email, API call) MUST have
an idempotency check BEFORE the side effect.
```

## Core Rules

| Aspect | Rule |
|--------|------|
| Arguments | Pass IDs, not objects |
| Retries | `retry_on` (explicit `attempts:`) for transient; `discard_on` for permanent errors |
| Backend (Rails 8) | Solid Queue (database-backed, no Redis) |
| Backend (Rails 7) | Sidekiq + Redis for high throughput |
| Recurring | `config/recurring.yml` (Solid Queue) or cron/sidekiq-cron |
| Anti-patterns | No ActiveRecord objects as args; no `:inline`/`:async` in production; no business logic in `perform` |

## Core Process

1. Write the job spec first — idempotency, retry, and error handling — and run it to confirm it fails.
2. Write the job class following the perform contract in HARD-GATE.
3. Add `retry_on` with explicit `attempts:` limit and `discard_on` for at least one permanent error.
4. Run the full test suite.
5. Enqueue or perform the job twice — confirm the second run is a no-op.
6. For recurring jobs, define them in `config/recurring.yml` (Rails 8) or the chosen scheduler config.

## Extended Resources

**Rails 8 vs Rails 7**
| Aspect | Rails 7 and earlier | Rails 8 |
|--------|---------------------|---------|
| Default | No default; set `queue_adapter` (often Sidekiq) | **Solid Queue** (database-backed) |
| Dev/test | `:async` or `:inline` | Same |
| Recurring | External (cron, sidekiq-cron) | `config/recurring.yml` |
| Dashboard | Third-party (Sidekiq Web) | **Mission Control Jobs** |

**Examples**

**Thin job with idempotency and retry:**
```ruby
class SendInvoiceReminderJob < ApplicationJob
  queue_as :default
  retry_on Net::OpenTimeout, wait: :polynomially_longer, attempts: 5
  discard_on ActiveRecord::RecordNotFound

  def perform(invoice_id)
    invoice = Invoice.find(invoice_id)
    return if invoice.reminder_sent_at?

    InvoiceReminders::Send.call(invoice:)
  end
end
```

**Service owns the side effect and state update:**
```ruby
module InvoiceReminders
  class Send
    def self.call(invoice:)
      InvoiceMailer.overdue(invoice).deliver_now
      invoice.update!(reminder_sent_at: Time.current)
    end
  end
end
```

- [BACKENDS.md](../../resources/rails/skills/infrastructure/implement-background-job/BACKENDS.md) — Solid Queue vs Sidekiq setup, configuration details, and Redis requirements.
Load these files only when their specific content is needed:

- **[../../resources/rails/skills/infrastructure/implement-background-job/assets/job_patterns.md](../../resources/rails/skills/infrastructure/implement-background-job/assets/job_patterns.md)** — Use when implementing multi-step orchestration or batch job patterns
- **[../../resources/rails/skills/infrastructure/implement-background-job/assets/retry_examples.md](../../resources/rails/skills/infrastructure/implement-background-job/assets/retry_examples.md)** — Use when configuring `retry_on`/`discard_on` for specific error classes beyond the basic patterns above

## Output Checklist

- [ ] Backend decision stated (Rails version/scale → Solid Queue or Sidekiq)
- [ ] Job spec shown first; command run; confirms failure before implementation
- [ ] `perform` receives IDs, loads record, guards idempotency, delegates to service
- [ ] `retry_on` with `attempts:` limit and `discard_on` for permanent error
- [ ] Double-run verification confirms second run is a no-op
- [ ] Recurring job (if any) defined in `config/recurring.yml` or scheduler config
- [ ] If ops docs requested: record backend, retry, recurring schedule, and idempotency decisions in `process_log.md`

## Integration

| Skill | When to chain |
|-------|---------------|
| **review-migration** | Solid Queue uses DB tables; add migrations safely |
| **security-check** | Jobs receive serialized input; validate like any entry point |
| **write-tests** | TDD gate: write job spec before implementation; use `perform_enqueued_jobs` |
| **create-service-object** | Keep `perform` thin; call service objects for business logic |
