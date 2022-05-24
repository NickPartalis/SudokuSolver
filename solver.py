def is_valid(board, num, row, col):
    """Returns True if a number is a valid answer for the specific cell, False otherwise."""
    # Check row
    if num in board[row]:
        return False

    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check same box
    box_row = (row // 3) * 3  # Gets the top left coordinates of the box it's in
    box_col = (col // 3) * 3

    for i in range(3):
        for j in range(3):
            if board[box_row + i][box_col + j] == num:
                return False

    return True


def solve(board, puzzle=None, display=False):
    """Solves a Sudoku puzzle, when possible. Returns True if successfully solved, False otherwise."""
    # Find the next empty spot
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for guess in range(1, 10):
                    if is_valid(board, guess, row=i, col=j):
                        board[i][j] = guess
                        if display:
                            puzzle.fill_cell(i, j, guess)
                        # Recursion
                        if solve(board, puzzle, display):
                            return True
                    # Backtracking
                    board[i][j] = 0  # Runs if the next "step" has no valid answer
                    if display:
                        puzzle.empty_cell(i, j)
                return False

    return True  # Runs when there are no empty slots, so the puzzle is solved
