# Skill Catalog

12 atomic planning skills and 4 personas. `directory.json` is the source of truth.

| Name | Type | Area | Use when | Path |
|------|------|------|----------|------|
| `create-prd` | atomic | PRD | Writing a PRD or feature spec | `skills/prd/create-prd/SKILL.md` |
| `review-prd` | atomic | PRD | Auditing a PRD for gaps | `skills/prd/review-prd/SKILL.md` |
| `generate-tasks` | atomic | Task management | Breaking an approved PRD into tasks | `skills/task-management/generate-tasks/SKILL.md` |
| `plan-tickets` | atomic | Task management | Drafting tracker tickets (draft-only by default) | `skills/task-management/plan-tickets/SKILL.md` |
| `estimate-tasks` | atomic | Task management | Sizing work | `skills/task-management/estimate-tasks/SKILL.md` |
| `prioritize-backlog` | atomic | Backlog | Ranking a backlog (RICE, MoSCoW, WSJF, value-vs-effort) | `skills/backlog/prioritize-backlog/SKILL.md` |
| `plan-sprint` | atomic | Ceremony | Selecting tickets and a sprint goal | `skills/ceremony/plan-sprint/SKILL.md` |
| `create-retrospective` | atomic | Ceremony | Writing a sprint retro | `skills/ceremony/create-retrospective/SKILL.md` |
| `identify-risks` | atomic | Execution | Building a risk register | `skills/execution/identify-risks/SKILL.md` |
| `generate-status-report` | atomic | Execution | Writing a stakeholder status update | `skills/execution/generate-status-report/SKILL.md` |
| `requirements-clarifier` | atomic | Analysis | Turning a vague ask into requirements | `skills/analysis/requirements-clarifier/SKILL.md` |
| `github-issue` | atomic | GitHub issues | Creating or updating GitHub issues | `skills/github-issues/github-issue/SKILL.md` |
| `product-owner` | persona | Personas | Discovery through sprint-ready tickets | `skills/personas/product-owner/SKILL.md` |
| `project-manager` | persona | Personas | Estimates, risks, and status | `skills/personas/project-manager/SKILL.md` |
| `tech-lead` | persona | Personas | Technical go/no-go on a PRD | `skills/personas/tech-lead/SKILL.md` |
| `delivery-lead` | persona | Personas | PRD through retrospective | `skills/personas/delivery-lead/SKILL.md` |

## If you need…

| You need | Skill |
|----------|-------|
| Clarify a vague ask | `requirements-clarifier` |
| Write or review a PRD | `create-prd` → `review-prd` |
| Break down approved scope | `generate-tasks` → `estimate-tasks` |
| Draft tickets or GitHub issues | `plan-tickets` → `github-issue` |
| Rank and commit a sprint | `prioritize-backlog` → `plan-sprint` |
| Execution health | `identify-risks` → `generate-status-report` |
| End-to-end planning | `product-owner` |
| Technical feasibility | `tech-lead` |
| Full delivery cycle | `delivery-lead` |

See also: [integration matrix](integration-matrix.md), [persona guide](../persona-guide.md), [gaps](gaps.md).
