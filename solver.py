def is_valid(board, num, row, col):
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


def solve(board):
    """Solves a Sudoku puzzle, if possible. Returns True if successfully solved."""
    # Find the next empty spot
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for guess in range(1, 10):
                    if is_valid(board, guess, row=i, col=j):
                        board[i][j] = guess
                        # Recursion
                        if solve(board):
                            return True
                    # Backtracking
                    board[i][j] = 0  # Runs if the next "step" has no valid answer
                return False

    return True  # Runs when there are no empty slots, so the puzzle is solved
