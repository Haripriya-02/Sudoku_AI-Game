# Colab UI integration note

Use the interactive UI cell developed in your notebook after the solver and puzzle are defined. The UI expects:
- `PUZZLE`: a 9x9 list, with 0 for empty cells
- `solution = solve_sudoku(PUZZLE)`
- `solve_sudoku(board)`: the Z3 solver function

For best compatibility, paste the interface cell into Colab after those definitions. Colab widgets can render differently depending on the browser and notebook theme.
