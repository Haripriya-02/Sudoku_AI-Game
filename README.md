# AI Sudoku Game — Predicate Calculus + Z3

A playable 9×9 Sudoku game for Google Colab. It uses the Boolean predicate `Val(r,c,d)` and the Z3 constraint solver.

## Features
- Interactive board and on-screen number pad
- New Game, Check, Hint, Solve with AI, and Clear entries
- Original clues are locked
- Highlights conflicts and incorrect filled entries
- Two built-in puzzles
- Logical explanation and solution verification test

## Run in Google Colab
1. Download `AI_Sudoku_Predicate_Calculus.ipynb`.
2. Open https://colab.research.google.com/.
3. Choose **File → Upload notebook**.
4. Upload the notebook and run all cells from top to bottom.
5. Play using the board shown in the notebook output.

The first cell installs `z3-solver`; internet access is required for this step.

## Predicate and constraints
`Val(r,c,d)` is true if row `r`, column `c` contains digit `d`.

The model enforces:
1. Every cell contains at least one digit.
2. Every cell contains at most one digit.
3. A digit cannot repeat in a row.
4. A digit cannot repeat in a column.
5. A digit cannot repeat in a 3×3 box.
6. Original puzzle clues remain fixed.

The first two rules together mean each cell contains exactly one digit. Z3 checks satisfiability and returns a model that the game displays as a solved grid.

## Technology
Python, Google Colab, Z3 Solver, IPython display, HTML/CSS and JavaScript.

## Limitations
The interactive callbacks are designed for Google Colab, not a regular Python terminal. The current game uses two predefined puzzles and does not yet generate puzzles or prove uniqueness.

## Academic note
Z3 is an SMT solver. This implementation uses its Boolean-constraint interface to represent the finite propositions `Val(r,c,d)`.
