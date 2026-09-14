# Example Estimation Session

Supplementary reference only. Illustrates a complete estimation session, including a spike-blocked item.

**Framework:** Story points (Fibonacci) — inferred from backlog context.

| ID | Task | Estimate | Confidence | Notes |
|----|------|----------|------------|-------|
| T1 | Add user login via email/password | 3 | High | Well-understood auth pattern, existing library available |
| T2 | Build admin dashboard with role filtering | 8 | Medium | UI scope is clear; role logic may expand |
| T3 | Integrate payment gateway | WARNING TBD | Low | API complexity unknown — spike required before estimating |
| T4 | Write unit tests for auth module | 2 | High | Scope directly tied to T1, straightforward |

**Flagged items:**

- **T3 — "Integrate payment gateway":** Low confidence. Recommend a time-boxed spike (1–2 days) to evaluate API docs, sandbox availability, and edge-case handling before assigning points.

**Summary:** 3 estimated tasks total 13 points (High: 2, Medium: 1). T3 blocked pending spike. Re-estimate T3 after spike completes.
