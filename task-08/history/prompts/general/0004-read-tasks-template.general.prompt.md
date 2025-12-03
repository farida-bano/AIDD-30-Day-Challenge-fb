---
id: 0004
title: Read Tasks Template
stage: general
date: 2025-12-03
surface: agent
model: gemini-1.5-pro
feature: none
branch: main
user: user
command: read tasks-template.md file
labels: ["context"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - task-08/.specify/templates/tasks-template.md
tests:
  null
---

## Prompt

read tasks-template.md file

## Response snapshot

# Calculator Development Task Template

## Task ID: [TASK-ID]
**Task Title:** [Brief descriptive title]
**Priority:** [High/Medium/Low]
**Status:** [Not Started/In Progress/Review/Completed/Blocked]
**Assigned To:** [Developer Name]
**Due Date:** [YYYY-MM-DD]
**Estimated Effort:** [X] hours/days
**Actual Effort:** [X] hours/days
**Points/Complexity:** [Story Points/Complexity Score]

---

## 1.0 Task Description

### Objective
[Clear, concise statement of what needs to be accomplished]

## Outcome

- ✅ Impact: Successfully read the tasks template.
- 🧪 Tests: N/A
- 📁 Files: Read tasks-template.md
- 🔁 Next prompts: N/A
- 🧠 Reflection: Provided tasks template for context.

## Evaluation notes (flywheel)

- Failure modes observed: N/A
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
