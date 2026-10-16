# Sudoku AI — Predicate Calculus + Z3

A beginner-friendly Sudoku solver that models Sudoku with the predicate `Val(r,c,d)` and solves the resulting constraints using Z3. The interactive version is designed to run directly in Google Colab with `ipywidgets`—no local host or separate web server is required.

## Logic model

- `Val(r,c,d)`: cell `(r,c)` contains digit `d`.
- Each cell has exactly one digit from 1 to 9.
- Each digit occurs exactly once in every row, column, and 3×3 box.
- The original clues are asserted as facts.
- Z3 searches for a satisfying assignment.

The solver uses universally quantified Z3 formulas for the cell, row, and column constraints, and explicit constraints for each 3×3 box. It is accurate to describe this as a **predicate-calculus-style, quantified constraint model implemented with Z3/SMT**, rather than a standalone first-order logic theorem prover.

## Run in Google Colab

1. Open [Google Colab](https://colab.research.google.com/).
2. Create a new notebook.
3. Install dependencies:

   ```python
   !pip -q install z3-solver ipywidgets
   ```
4. Copy the solver and UI cells from the notebook or source files into the notebook.
5. Run cells from top to bottom. The UI appears in the notebook output.

No localhost, Streamlit, or separate website is needed.

## Repository contents

- `src/sudoku_solver.py` — Z3 `Val(r,c,d)` solver and solution validation.
- `src/puzzle.py` — example Sudoku puzzle.
- `presentation/sudoku_ai_presentation.tex` — Beamer slides inspired by the provided logic-agent presentation structure.
- `presentation/video_script.md` — short demo narration.
- `presentation/linkedin_post.md` — editable LinkedIn draft.
- `requirements.txt` — Python dependencies.

## Notes

The repository contains the core solver. The interactive Colab widget interface can be included in a `.ipynb` notebook as a next step. The quantified solver may take longer than a simple integer-variable model on some environments because quantified SMT solving is more complex.
