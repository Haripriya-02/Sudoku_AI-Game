from z3 import Function, IntSort, BoolSort, Solver, ForAll, Implies, And, Sum, If, sat, Int

# Predicate: Val(r, c, d) is true when cell (r, c) contains digit d.
Val = Function("Val", IntSort(), IntSort(), IntSort(), BoolSort())

def solve_sudoku(board):
    """Solve a 9x9 Sudoku using quantified Val(r,c,d) constraints."""
    solver = Solver()
    r, c, d = Int("r"), Int("c"), Int("d")

    # Each cell contains exactly one digit from 1 to 9.
    cell_digit_count = Sum([If(Val(r, c, digit), 1, 0)
                            for digit in range(1, 10)])
    solver.add(ForAll(
        [r, c],
        Implies(And(r >= 0, r < 9, c >= 0, c < 9),
                cell_digit_count == 1)
    ))

    # Each digit appears exactly once in every row.
    row_count = Sum([If(Val(r, column, d), 1, 0)
                     for column in range(9)])
    solver.add(ForAll(
        [r, d],
        Implies(And(r >= 0, r < 9, d >= 1, d <= 9),
                row_count == 1)
    ))

    # Each digit appears exactly once in every column.
    column_count = Sum([If(Val(row, c, d), 1, 0)
                        for row in range(9)])
    solver.add(ForAll(
        [c, d],
        Implies(And(c >= 0, c < 9, d >= 1, d <= 9),
                column_count == 1)
    ))

    # Each digit appears exactly once in each 3x3 box.
    for box_r in range(0, 9, 3):
        for box_c in range(0, 9, 3):
            for digit in range(1, 10):
                box_count = Sum([
                    If(Val(rr, cc, digit), 1, 0)
                    for rr in range(box_r, box_r + 3)
                    for cc in range(box_c, box_c + 3)
                ])
                solver.add(box_count == 1)

    # Original clues become facts in the knowledge base.
    for row in range(9):
        for column in range(9):
            given = board[row][column]
            if given != 0:
                solver.add(Val(row, column, given))

    if solver.check() != sat:
        return None

    model = solver.model()
    result = []
    for row in range(9):
        result_row = []
        for column in range(9):
            value = next(
                digit for digit in range(1, 10)
                if model.evaluate(
                    Val(row, column, digit), model_completion=True
                ) == True
            )
            result_row.append(value)
        result.append(result_row)
    return result


def valid_solution(grid):
    """Return True if all Sudoku rows, columns, and boxes are valid."""
    target = set(range(1, 10))
    if any(set(row) != target for row in grid):
        return False
    if any({grid[r][c] for r in range(9)} != target for c in range(9)):
        return False
    for br in range(0, 9, 3):
        for bc in range(0, 9, 3):
            if {grid[r][c] for r in range(br, br+3)
                for c in range(bc, bc+3)} != target:
                return False
    return True
