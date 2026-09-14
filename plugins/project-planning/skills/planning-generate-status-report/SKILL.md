---
name: planning-generate-status-report
description: 'Use when writing a stakeholder status report, sprint update, or weekly
  project update. Do not invent progress. Trigger words: status report, sprint update,
  weekly update, project status, stakeholder update.'
license: MIT
metadata:
  source-id: igmarin/agnostic-planning-skills:generate-status-report
  source-commit: ae074f9c8718013a6b2c618b3856e6914986b775
  kind: atomic
  dependencies: '[]'
---

Resolve skill names through `../../skill-map.json`; use the source pack to disambiguate. Load only the workflow and resources needed for the authorized task.

# Generating a Status Report

Produce a clear, honest status report.

## HARD-GATE
- Do not fabricate progress; unknown → "needs update".
- Do not hide blockers or risks.
- Use active voice; cite blockers with owners.

## Core Process
1. Gather task progress, sprint info, blockers, risk register.
2. Categorize items: Accomplished, In Progress, Blocked, Upcoming.
3. Write Executive Summary (2–4 sentences).
4. Fill sections: Accomplishments, In Progress, Blocked, Risks, Next Steps (see template).
5. Verify no status is fabricated.

## STATUS_REPORT_TEMPLATE
```markdown
# Status Report: [Project / Sprint Name]
**Period:** [Start] – [End]   **Prepared:** [Date]   **Author:** [Name]

## Executive Summary
**Health:** On Track | At Risk | Blocked
[2–4 sentences]

## Accomplishments
- [Task / milestone] — [context]

## In Progress
| Task | Owner | Status | ETA |

## Blocked
| Task | Blocker | Owner | Resolution Plan |

## Risks & Concerns
| # | Risk | Likelihood | Impact | Status Change |

## Next Steps
- [Action] — Owner: [Name], Due: [Date]
```

## Integration
- **identify-risks** for risk register
- **estimate-tasks** for effort references
