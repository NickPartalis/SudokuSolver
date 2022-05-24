from pprint import pprint
import requests
from gui import SudokuNoInputUI, SudokuUserInputUI
from solver import solve

def generate_puzzle(difficulty):
    if difficulty not in ("easy", "medium", "hard"):
        difficulty = "random"

    # Sugoku API from Roberto Ortega (https://github.com/bertoort)
    url = "https://sugoku.herokuapp.com/board"
    params = {"difficulty": difficulty}

    response = requests.request("GET", url, params=params)
    return response.json()["board"]


if __name__ == '__main__':
    board = generate_puzzle("random")

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

    mode = input("Choose mode 1 or 2: ")
    if mode == "1":
        gui = SudokuNoInputUI(board)
    elif mode == "2":
        gui = SudokuUserInputUI()
