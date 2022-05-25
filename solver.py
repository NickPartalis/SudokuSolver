def is_valid(board, num, row, col):
    """Returns True if a number is a valid answer for the specific cell, False otherwise."""
    # Check row
    if num in board[row]:
        return False

    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check same square
    square_row = (row // 3) * 3  # Gets the top left coordinates of the box it's in
    square_col = (col // 3) * 3

    for i in range(3):
        for j in range(3):
            if board[square_row + i][square_col + j] == num:
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


def is_solvable(board):
    """Receives a 9x9 board as a parameter. Returns True if puzzle can be solved, False otherwise."""
    for row in range(9):
        for col, num in enumerate(board[row]):
            if num != 0:
                # Check row
                if board[row].count(num) > 1:
                    print("Same row")
                    return False

                # Check column
                for i in range(9):
                    if board[i][col] == num and i != row:
                        print("Same column")
                        return False

                # Check same square
                square_row = (row // 3) * 3  # Gets the top left coordinates of the box it's in
                square_col = (col // 3) * 3

                for i in range(3):
                    for j in range(3):
                        if board[square_row + i][square_col + j] == num and (square_row+i, square_col+j) != (row, col):
                            print("Same square")
                            return False

    return True
