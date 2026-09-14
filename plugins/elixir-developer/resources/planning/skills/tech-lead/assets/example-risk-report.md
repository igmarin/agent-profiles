# Example: Technical Risk Report

Illustrates a No-Go outcome with two High-severity blockers and insufficient estimation coverage.

```
## Technical Risk Report

### PRD Review Summary
- Completeness: Conditional Pass
- Testability: Pass
- Clarity: Pass
- Open gaps:
  - Non-functional requirement for API response time is missing a numeric threshold
  - Out-of-scope items section is absent

### Feasibility Assessment
| Concern | Area | Severity | Recommendation |
|---------|------|----------|----------------|
| Real-time sync requires sub-100ms latency across regions but no CDN or edge strategy is defined | Architecture | High | Define latency budget per region and add edge caching to scope, or relax the latency requirement |
| OAuth provider dependency has no fallback if provider is unavailable | Integration | Medium | Add graceful degradation or session persistence fallback |
| "AI-powered recommendations" referenced with no model or data pipeline specified | Scope Clarity | High | Specify model source, training data ownership, and inference latency target |

### Estimation Quality
- Coverage: 72% — testing and deployment tasks are not estimated
- Realism flags: 2 — "Backend API" estimated as a single 10-day task with no decomposition; "Auth integration" has no dependency on third-party availability
- Consistency issues: Frontend tasks estimated at 0.5x the effort of equivalent backend tasks with no stated justification

### Go / No-Go Recommendation
**Recommendation**: No-Go

**Rationale**: Two High-severity feasibility blockers exist that cannot be resolved without PRD revision. Estimation coverage is below threshold and the lack of decomposition introduces significant delivery risk. The PRD is not yet ready for engineering kickoff.

**Conditions**:
- Resolve the real-time latency architecture concern with a defined strategy
- Specify the AI recommendation pipeline and data ownership
- Re-estimate with full task decomposition and coverage of non-functional, testing, and deployment work

### Next Steps
- Product owner to revise NFR section with numeric thresholds (owner: PM)
- Engineering lead to define edge/CDN strategy and update architecture notes
- Re-submit revised PRD and estimates for a second Tech Lead review cycle
```
