# Implementation Checklist: Calculator

**Purpose**: To verify that all core requirements for the calculator feature are met before shipping.
**Created**: 2025-12-03
**Feature**: [specs/calculator/spec.md](specs/calculator/spec.md)

## Core Functionality

- [ ] CHK001 Addition (`+`) operation works correctly with integers and floats.
- [ ] CHK002 Subtraction (`-`) operation works correctly.
- [ ] CHK003 Multiplication (`*`) operation works correctly.
- [ ] CHK004 Division (`/`) operation works correctly.
- [ ] CHK005 Division by zero is handled gracefully (e.g., shows an error message).

## User Interface

- [ ] CHK006 All number buttons (0-9) are present and functional.
- [ ] CHK007 All operator buttons (+, -, *, /) are present and functional.
- [ ] CHK008 The 'Clear' (C) or 'All Clear' (AC) button resets the current calculation.
- [ ] CHK009 The display correctly shows user input and results.
- [ ] CHK010 The application has a clean and intuitive layout.

## Error Handling & Edge Cases

- [ ] CHK011 Entering multiple operators in a row is handled correctly.
- [ ] CHK012 Starting an expression with an operator is handled.
- [ ] CHK013 Very large numbers are displayed correctly (e.g., using scientific notation if necessary).

## Notes

- Check items off as completed: `[x]`
- This checklist should be reviewed by the QA team.
