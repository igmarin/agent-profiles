---
name: identify-risks
type: atomic
license: MIT
description: >
  Use when scanning a plan for risks or building a risk register.
  Every risk needs evidence from a task or requirement.
  Trigger words: risks, risk assessment, blockers, what could go
  wrong, risk register.
metadata:
  version: 1.0.0
  user-invocable: "true"
---
# Identifying Project Risks

Scan plans for risks backed by concrete evidence — not speculation.

## HARD-GATE
- Every risk must cite specific evidence (task, requirement).
- Do not flag everything high-risk; use likelihood/impact matrix honestly.
- Provide at least one concrete mitigation per risk.

## Core Process
1. Receive plan (tasks, tickets, PRD, sprint).
2. Scan for six patterns: dependency chains, single points of failure, ambiguous requirements, external dependencies, capacity/resource issues, technical uncertainty.
3. Classify each risk: Likelihood (High/Medium/Low), Impact (High/Medium/Low), Proximity (Immediate/Near-term/Future).
4. Suggest mitigation (prevention, contingency, owner).
5. Validate: remove risks lacking direct evidence.
6. Output risk register.

## Risk Patterns (six patterns)
1. Dependency Chain (task B blocked by task A not done)
2. Single Point of Failure (only one owner for critical item)
3. Ambiguous Requirement (TBD, vague acceptance criteria)
4. External Dependency (third-party API, vendor, regulatory)
5. Capacity/Resource (team member over-allocated, holiday overlap)
6. Technical Uncertainty (new tech, unproven integration, no spike)

## Output
- Risk Register: ID | Risk | Likelihood | Impact | Proximity | Evidence | Mitigation | Owner
- Summary counts by severity and proximity.
- Top 3 risks with detailed mitigations (including owner).

## Integration
- **estimate-tasks** — high-uncertainty tasks
- **generate-tasks** — dependency risks after task breakdown
- **generate-status-report** — include risk updates in stakeholder reports
