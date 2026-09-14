# Integration Matrix — Agnostic Planning Skills

Integration matrix: which skill connects to which and in what order.

---

## Format

- `A → B` means: after A, B typically follows
- `[gate]` indicates mandatory approval gate

---

## Complete Persona Loops

### Product Owner (Planning Lifecycle)

```mermaid
graph TD
    A[Feature Idea] --> B[Phase 1: Discovery]
    B --> C[Phase 2: PRD Draft]
    C --> D{PRD Approved?}
    D -->|No| E[Phase 3: Review & Revise]
    E --> C
    D -->|Yes| F[Phase 4: Task Estimation]
    F --> G[Phase 5: Ticket Generation]
    G --> H{Tickets Approved?}
    H -->|No| G
    H -->|Yes| I[Phase 6: Sprint Placement]
    I --> J{Sprint Confirmed?}
    J -->|No| I
    J -->|Yes| K[Ready for Development]
```

### Project Manager (Execution Tracking)

```mermaid
graph TD
    A[Task List / PRD] --> B["Phase 1: Estimation<br/>estimate-tasks"]
    B --> C{Estimates Reviewed?}
    C -->|No| B
    C -->|Yes| D["Phase 2: Risk Assessment<br/>identify-risks"]
    D --> E{Risks Accepted?}
    E -->|No| D
    E -->|Yes| F[Phase 3: Tracking Setup]
    F --> G["Phase 4: Status Reporting<br/>generate-status-report"]
    G --> H{Report Approved?}
    H -->|No| G
    H -->|Yes| I[Share with Stakeholders]
```

---

## Full Pipeline

```text
requirements-clarifier → create-prd → review-prd → [gate: PRD approved] → generate-tasks → estimate-tasks → identify-risks → prioritize-backlog → plan-tickets → (github-issue) → plan-sprint → generate-status-report → create-retrospective
```

---

## Integrations by Skill

### requirements-clarifier

| Next | When |
|------|------|
| create-prd | After requirements are clarified and approved, draft the PRD |
| generate-tasks | If clarification uncovered concrete implementation tasks |

### create-prd

| Next | When |
|------|------|
| review-prd | Always after PRD draft — review for completeness and feasibility |
| generate-tasks | After PRD reviewed and approved |
| plan-tickets | If tickets needed directly from PRD scope |

### review-prd

| Next | When |
|------|------|
| generate-tasks | After review passes (Approved or Approved with Suggestions) |
| create-prd | If review returns Needs Revision — loop back to re-draft |
| tech-lead | For deeper feasibility and estimation quality assessment |

### generate-tasks

| Next | When |
|------|------|
| estimate-tasks | To assign effort estimates to the task breakdown |
| plan-tickets | If the same initiative needs ticket drafts |

### estimate-tasks

| Next | When |
|------|------|
| identify-risks | After estimation, to assess risks surfaced by high-uncertainty tasks |
| plan-sprint | To select tickets based on capacity vs estimates |

### identify-risks

| Next | When |
|------|------|
| generate-status-report | Include the risk register in stakeholder status updates |
| plan-tickets | If risks reveal new ticket dependencies |
| plan-sprint | Scan sprint plan for dependency and capacity risks |

### plan-tickets

| Next | When |
|------|------|
| github-issue | Create GitHub issues from approved ticket drafts |
| prioritize-backlog | After tickets drafted, rank them for sprint selection |
| (Create in tracker) | After ticket drafts approved |
| plan-sprint | Selected tickets feed into sprint planning |

### github-issue

| Next | When |
|------|------|
| plan-sprint | After issues are created continue with sprint planning |
| plan-tickets | If issues need to be revised or re-drafted |

### prioritize-backlog

| Next | When |
|------|------|
| plan-sprint | Use ordered backlog to select sprint candidates |
| plan-tickets | If newly prioritized items need ticket drafts |

### plan-sprint

| Next | When |
|------|------|
| generate-status-report | Report sprint progress to stakeholders |
| (Begin implementation) | Start working on sprint tickets |
| create-retrospective | After sprint ends, generate retrospective |

### generate-status-report

| Next | When |
|------|------|
| (Share with stakeholders) | After report approved |
| identify-risks | If report reveals new or escalating risks |
| create-retrospective | Status reports feed into end-of-sprint retrospective |

### create-retrospective

| Next | When |
|------|------|
| plan-sprint | Action items feed into the next sprint plan |
| project-manager | Feed action items into execution tracking |

---

## Quick Decision Matrix

```text
Have a feature idea?
  └─ create-prd → review-prd → generate-tasks → estimate-tasks

Need to prioritize?
  └─ prioritize-backlog → plan-sprint

Need execution tracking?
  └─ project-manager (persona)
     └─ estimate-tasks → identify-risks → generate-status-report

Full end-to-end planning?
  └─ product-owner (persona)

Need technical review?
  └─ tech-lead (persona)

Full delivery cycle?
  └─ delivery-lead (persona)

Sprint done?
  └─ create-retrospective

Need to create GitHub issues?
  └─ plan-tickets → github-issue
```

---

## Checkpoints and Gates

| Name | Type | Defined in | Purpose |
|------|------|------------|---------|
| PRD Approved | gate | create-prd, product-owner, delivery-lead | Don't generate tasks without approved PRD |
| Estimation Review | gate | estimate-tasks, project-manager | Don't proceed if >30% of tasks have low confidence |
| Risk Acceptance | gate | identify-risks, project-manager | Every High/High risk must have an owner and plan |
| Ticket Approved | gate | plan-tickets, product-owner | Don't create tracker issues without approval |
| Status Report Approved | gate | generate-status-report, project-manager | Don't share report without approval |
| Sprint Confirmed | gate | product-owner | Don't assume sprint placement |
| Sprint Commitment | gate | plan-sprint, delivery-lead | Don't proceed without committed sprint plan |
| Retrospective Complete | gate | create-retrospective, delivery-lead | Don't close cycle without action items |

---

## See Also

- [Skill Catalog](skill-catalog.md) — Complete skills list with descriptions and trigger words
- [Persona Guide](../persona-guide.md) — Persona workflows with Mermaid diagrams

## Developer handoff

Use the delivery-lead checkpoint for multi-stage handoffs: authorized scope, acceptance criteria, qualified skill identities, artifacts, check evidence, blockers, and next action. The receiving stack role verifies current repository state and executes its workflow. Small bugs use the developer bug-fix workflow directly; no PRD is required.
