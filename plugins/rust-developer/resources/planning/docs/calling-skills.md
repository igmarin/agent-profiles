# Calling Skills and Personas

Agnostic Planning Skills can be invoked in different ways depending on your environment and desired level of autonomy.

## Invocation Methods

| Method | Syntax | Best For |
|--------|--------|----------|
| **Chat Commands** | `@skill-name` or `/skill-name` | Explicitly forcing the agent to follow a specific skill's instructions |
| **CLI (`gh skill` / `skills.sh`)** | `gh skill install ...` | Local installation, pinning versions, reproducible setups |

> MCP support (`use_skill`, `use_agent`) is planned but not yet implemented.

---

## Using Skills

### Via Chat Commands

In environments like Cursor, Windsurf, or Gemini CLI:

```text
@create-prd Add Google OAuth login to the app
@review-prd Review the login PRD for completeness
@generate-tasks Break down the approved login PRD
@estimate-tasks Estimate the login task breakdown
@identify-risks Scan the login plan for risks
@prioritize-backlog Rank the remaining feature requests
@plan-tickets Draft tickets for the search feature
@github-issue Create a bug report for the login page
@plan-sprint Select tickets and define the sprint goal
@generate-status-report Create a status report for stakeholders
@create-retrospective Generate the sprint retrospective
```

---

## Using Personas

Personas orchestrate multiple skills through phases with approval gates.

### Via Chat Commands

```text
@requirements-clarifier Clarify the user notification system requirements
@product-owner Plan the user notification system feature
@project-manager Track execution of the current sprint
@tech-lead Review the notification PRD for feasibility
@delivery-lead Run the full delivery cycle for the notification feature
```

---

## Installing Skills

### Via GitHub CLI

```bash
# Install a specific skill
gh skill install igmarin/agnostic-planning-skills create-prd --scope project

# Install all skills
gh skill install igmarin/agnostic-planning-skills
```

### Via skills.sh

There is **no** root `SKILL.md`. Each folder under `skills/` is its own skill.

#### Project-Level (Local) Installation
To install skills for your current project workspace:
```bash
npx skills add igmarin/agnostic-planning-skills
npx skills add igmarin/agnostic-planning-skills --skill '*'
npx skills add igmarin/agnostic-planning-skills --skill create-prd
```

#### Global Installation
To install skills globally for your AI coding assistant:
```bash
npx skills add igmarin/agnostic-planning-skills --skill '*' -g
npx skills add igmarin/agnostic-planning-skills --skill create-prd -g
```

---

Names and paths: [skill catalog](reference/skill-catalog.md).
