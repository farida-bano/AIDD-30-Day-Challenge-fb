# ADR-001: Core Logic and Technology Stack for Calculator

> **Scope**: This ADR documents the decision to use standard Python for the initial implementation of the calculator's core logic, without an external GUI framework.

- **Status:** Proposed
- **Date:** 2025-12-03
- **Feature:** calculator
- **Context:** The project requires a simple calculator. The initial implementation focuses on core arithmetic operations. This decision addresses the technology choice for this first iteration.

## Decision

We will implement the calculator's core logic as a set of functions within a single Python script (`calculator.py`). The application will run in the command line and will not feature a graphical user interface (GUI) in this phase.

- **Language:** Python 3
- **Core Logic:** A module with functions for `add`, `subtract`, `multiply`, and `divide`.
- **User Interface:** None (Command-line execution only for now).
- **Dependencies:** No external libraries are required for the core logic.

## Consequences

### Positive

- **Simplicity & Speed:** Using standard Python allows for very fast initial development and testing.
- **No External Dependencies:** Avoids the complexity of managing GUI toolkits or other libraries for this simple use case.
- **Focus on Logic:** Ensures the core arithmetic is solid before investing in a user interface.
- **Easy to Test:** The functions can be easily unit-tested.

### Negative

- **No User-Friendly Interface:** Lack of a GUI makes it less intuitive for non-technical users.
- **Limited Functionality:** A command-line interface limits the complexity of interactions that can be supported in the future.

## Alternatives Considered

- **Python with Tkinter/PyQt:**
  - A GUI-based calculator using a standard Python library like Tkinter or a more powerful one like PyQt.
  - **Why rejected:** This adds unnecessary complexity for the initial phase, which is focused on proving out the core logic. A GUI can be added later as a separate feature.

- **Web-based Calculator (Flask/Django + HTML/CSS/JS):**
  - A calculator application served as a web page.
  - **Why rejected:** This would require a significantly larger setup (web server, frontend code, etc.) and is overkill for the current requirements.

## References

- Feature Spec: `specs/calculator/spec.md`
- Implementation Plan: `specs/calculator/plan.md`
- Related ADRs: None
- Evaluator Evidence: None
