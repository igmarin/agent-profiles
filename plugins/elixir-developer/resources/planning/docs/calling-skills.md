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

> [!IMPORTANT]
> **`--full-depth` is required.** The root `SKILL.md` is a catalog (`type: catalog`), not a standalone skill. Without `--full-depth`, the `skills` CLI treats that root file as the only skill for the repo and stops — you get 1 skill (the catalog) instead of all 16. `--full-depth` makes the CLI recurse into `skills/<category>/<name>/`.
>
> Without `--all`, the CLI opens an interactive multi-select picker listing all 16 skills. Omit `--all` when you want to choose a subset.

#### Project-Level (Local) Installation
To install skills for your current project workspace:
```bash
# Install ALL skills and personas (non-interactive)
npx skills add igmarin/agnostic-planning-skills --full-depth --all

# Interactive: pick which skills to install (multi-select picker)
npx skills add igmarin/agnostic-planning-skills

# Install a specific skill (e.g., create-prd)
npx skills add igmarin/agnostic-planning-skills@create-prd --full-depth
```

#### Global Installation
To install skills globally for your AI coding assistant:
```bash
# Install ALL skills and personas globally
npx skills add igmarin/agnostic-planning-skills --full-depth --all --global

# Install a specific skill globally (e.g., create-prd)
npx skills add igmarin/agnostic-planning-skills@create-prd --full-depth --global
```

---

Names and paths: [skill catalog](reference/skill-catalog.md).
