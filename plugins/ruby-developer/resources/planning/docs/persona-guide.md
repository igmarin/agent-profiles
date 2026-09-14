# Persona Guide

Index of the four orchestrators. Phase steps and gates live in each persona `SKILL.md` — one owner.

| Persona | Use when | Path |
|---------|----------|------|
| `product-owner` | Feature needs discovery → PRD → tasks → tickets → sprint | [SKILL.md](../../../skills/planning-product-owner/SKILL.md) |
| `project-manager` | Sprint or project needs estimates, risks, and a status report | [SKILL.md](../../../skills/planning-project-manager/SKILL.md) |
| `tech-lead` | PRD needs a technical go/no-go | [SKILL.md](../../../skills/planning-tech-lead/SKILL.md) |
| `delivery-lead` | Full cycle from PRD through retrospective | [SKILL.md](../../../skills/planning-delivery-lead/SKILL.md) |

## product-owner

```mermaid
graph TD
    A[Feature idea] --> B[Discovery]
    B --> C[PRD draft]
    C --> D{PRD approved?}
    D -->|no| C
    D -->|yes| E[Tasks]
    E --> F[Tickets]
    F --> G{Tickets approved?}
    G -->|no| F
    G -->|yes| H[Sprint placement]
    H --> I{Sprint confirmed?}
    I -->|no| H
    I -->|yes| J[Ready for development]
```

## project-manager

```mermaid
graph TD
    A[Task list / PRD] --> B[estimate-tasks]
    B --> C{Estimates reviewed?}
    C -->|no| B
    C -->|yes| D[identify-risks]
    D --> E{Risks accepted?}
    E -->|no| D
    E -->|yes| F[Tracking setup]
    F --> G[generate-status-report]
    G --> H{Report approved?}
    H -->|no| G
    H -->|yes| I[Share]
```

## tech-lead

```mermaid
graph TD
    A[PRD] --> B[review-prd]
    B --> C{Verdict?}
    C -->|Needs revision| D[Back to create-prd]
    C -->|Approved| E[Feasibility]
    E --> F{Feasible?}
    F -->|High blocker| G[Report and stop]
    F -->|yes| H[Estimation quality]
    H --> I{Quality OK?}
    I -->|no| H
    I -->|yes| J[Technical risk report]
    J --> K[Go / No-go / Go with conditions]
```

## delivery-lead

```mermaid
graph TD
    A[Feature idea] --> B[Scope: create-prd + review-prd]
    B --> C{PRD approved?}
    C -->|no| B
    C -->|yes| D[Plan: tasks + estimates + risks]
    D --> E[Prioritize: backlog + tickets]
    E --> F[plan-sprint]
    F --> G{Sprint committed?}
    G -->|no| F
    G -->|yes| H[Execute: status + risks]
    H --> I[create-retrospective]
    I --> J{Retro complete?}
    J -->|no| I
    J -->|yes| K[Delivery complete]
```

## See also

- [Skill catalog](reference/skill-catalog.md)
- [Integration matrix](reference/integration-matrix.md)

## Composition and resume

Existing names and `type: persona` remain compatible with installed consumers. Product owner, project manager, and tech lead own planning outcomes; delivery lead coordinates the delivery workflow. The composed developer profiles load implementation skills from their authoritative stack packs.

An approved PRD or concrete authorized brief supplies scope. Reuse prior authorization; small bugs go directly to a developer's bug-fix workflow. The [delivery checkpoint contract](../skills/personas/delivery-lead/SKILL.md#authorization-and-checkpoints) carries acceptance criteria, skill identities, evidence, and blockers across handoffs. A missing required skill blocks the dependent step and names the installation repair; optional gaps are disclosed.

Install or roll back using a pinned pack commit and its matching composed bundle. Existing planning skill names and paths are unchanged; avoid mixing versions of templates and their calling skills.
