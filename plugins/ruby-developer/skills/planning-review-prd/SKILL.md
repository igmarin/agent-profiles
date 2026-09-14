---
name: planning-review-prd
description: 'Use when reviewing a PRD for completeness, testability, clarity, or
  feasibility. Trigger words: review PRD, PRD review, validate PRD, feasibility check,
  requirements review.'
license: MIT
metadata:
  source-id: igmarin/agnostic-planning-skills:review-prd
  source-commit: 850967c1250b4acd32a59c2fc94d67a55fad04de
  kind: atomic
  dependencies: '[]'
---

Resolve skill names through `../../skill-map.json`; use the source pack to disambiguate. Load only the workflow and resources needed for the authorized task.

# Reviewing a PRD

Evaluate a PRD for quality — not agreement with a preferred solution.

## HARD-GATE
- Review the document, not the idea.
- Every finding must cite a specific PRD section (redact sensitive data).
- No alternative solutions unless a requirement is infeasible.

## Core Process
1. Receive the PRD.
2. Apply the review checklist (completeness, testability, clarity, feasibility, scope, dependencies, edge cases).
3. Classify each finding as Critical, Suggestion, or Note.
4. Produce a findings table with severity, evidence, and recommendation.
5. Verdict: Approved / Approved with Suggestions / Needs Revision.
6. If Needs Revision, instruct author to address Critical findings and re-run review.

## Output
- Verdict.
- Findings table with columns: #, Severity, Section, Finding, Evidence, Recommendation.
- Summary with count by severity.
- Acknowledgement of well-written sections.

## Review Checklist (abbreviated)
**Completeness:** goals and success metrics are measurable; out-of-scope explicit.
**Testability:** requirements can be verified with pass/fail tests; acceptance criteria are specific.
**Clarity:** no undefined jargon; no ambiguous modal verbs.
**Feasibility:** timeline realistic; dependencies identified.
**Scope & Edge Cases:** failure scenarios described; migration/compatibility concerns.

Refer to the full checklist in the skill’s reference documentation.

## Integration
| Skill | When |
|-------|------|
| **create-prd** | Review immediately after PRD generation |
| **generate-tasks** | After review passes |
| **tech-lead** persona | For deeper feasibility assessment |
