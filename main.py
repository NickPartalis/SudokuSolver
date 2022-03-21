from pprint import pprint
from solver import solve
import requests


def generate_puzzle(difficulty):
    if difficulty not in ("easy", "medium", "hard"):
        difficulty = "random"

    # Sugoku API from Roberto Ortega (https://github.com/bertoort)
    url = "https://sugoku.herokuapp.com/board"
    params = {"difficulty": difficulty}

    response = requests.request("GET", url, params=params)
    return response.json()["board"]


if __name__ == '__main__':
    board = generate_puzzle("hard")

    pprint(board)
    print("    ")
    print(solve(board))
    pprint(board)

    # example_board = [
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

    # pprint(example_board)
    # print("    ")
    # print(solve(example_board))
    # pprint(example_board)

