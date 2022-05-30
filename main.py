from pprint import pprint
from gui import SudokuRandomPuzzleUI, SudokuUserPuzzleUI, MainMenu
from solver import solve

if __name__ == '__main__':

    # board = [
    #     [3, 9, 0,   0, 5, 0,   0, 0, 0],
    #     [0, 0, 0,   2, 0, 0,   0, 0, 5],
    #     [0, 0, 0,   7, 1, 9,   0, 8, 0],
    #
    #     [0, 5, 0,   0, 6, 8,   0, 0, 0],
    #     [2, 0, 6,   0, 0, 3,   0, 0, 0],
    #     [0, 0, 0,   0, 0, 0,   0, 0, 4],
    #
    #     [5, 0, 0,   0, 0, 0,   0, 0, 0],
    #     [6, 7, 0,   1, 0, 5,   0, 4, 0],
    #     [1, 0, 9,   0, 0, 0,   2, 0, 0]
    # ]

    # pprint(board)
    # print("    ")
    # print(solve(board))
    # pprint(board)

    gui = MainMenu()
