# Example Sprint Plan

```
Sprint 14 | 2025-08-04 → 2025-08-15 | 10 days | Team: 4 engineers
Capacity: 4 × 10 × 6h × 0.8 = 192h | Velocity baseline: 38 pts

Sprint Goal: Enable customers to reset their own passwords without support intervention.

| Rank | Ticket  | Estimate | Confidence | Notes                        |
|------|---------|----------|------------|------------------------------|
| 1    | AUTH-42 | 8 pts    | High       | Core reset flow              |
| 2    | AUTH-43 | 5 pts    | High       | Email token service          |
| 3    | AUTH-44 | 3 pts    | High       | Rate-limiting middleware     |
| 4    | UI-88   | 5 pts    | Medium     | Reset UI — design ready      |
| 5    | AUTH-47 | 5 pts    | Medium     | Audit logging                |
| 6    | TEST-12 | 3 pts    | High       | E2E tests for reset flow     |

Total committed: 29 pts (76% of velocity — within 80% cap)
Buffer: 9 pts (24%)
Stretch goal: AUTH-50 (3 pts) — token expiry config, pull in if buffer allows.

Deferred (top candidates for Sprint 15):
1. AUTH-51 — SSO integration (13 pts) — too large, split first.
2. UI-90  — Account settings redesign (8 pts) — blocked on design review.
3. PERF-05 — Login latency optimisation (5 pts) — lower priority this cycle.
```
