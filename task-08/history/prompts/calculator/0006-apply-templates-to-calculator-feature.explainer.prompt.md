---
id: 0006
title: Apply Templates to Calculator Feature
stage: explainer
date: 2025-12-03
surface: agent
model: Gemini CLI Agent
feature: calculator
branch: main
user: sarosh
command: "Conversational: apply templates to calculator feature"
labels: [template, documentation, example]
links:
  spec: null
  ticket: null
  adr: "specs/calculator/adr.md"
  pr: null
files:
  - "specs/calculator/checklist.md"
  - "specs/calculator/adr.md"
tests:
  - "none"
---

## Prompt

"kia is ko hum calcultor text ka accodering kr sakhty hain?calculator text base ya according?"

(Context: User asked to make the generic project templates specific to the 'calculator' feature.)

## Response snapshot

The agent understood the user wanted to see how the templates could be used for the calculator feature.

1.  The agent created `specs/calculator/checklist.md` by populating `checklist-template.md` with items relevant to a calculator.
2.  The agent created `specs/calculator/adr.md` by populating `adr-template.md` with an architectural decision for the calculator.
3.  The agent then explained what a PHR is and offered to create one for the interaction itself.

This demonstrated the practical application of the project's templating system.

## Outcome

- ✅ Impact: Demonstrated how to use project templates to create feature-specific documentation artifacts for the calculator.
- 🧪 Tests: No tests were run as this was a documentation/explanation task.
- 📁 Files: Created `specs/calculator/checklist.md` and `specs/calculator/adr.md`.
- 🔁 Next prompts: User could ask to apply more templates or proceed with development.
- 🧠 Reflection: The user's request was ambiguous ("yes" to an either/or question). The agent correctly inferred the user's intent was to see examples rather than destructively modify template files. This avoided a negative outcome and provided a useful demonstration.

## Evaluation notes (flywheel)

- Failure modes observed: None.
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): n/a
