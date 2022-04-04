from tkinter import *
from pprint import pprint

MARGIN = 40
BOARD_SIZE = 540
BOX_SIZE = BOARD_SIZE / 9


class SudokuUI:
    def __init__(self, board):
        self.board = board
        self.window = Tk()
        self.window.title("Sudoku Solver")
        self.puzzle = Frame(master=self.window, bg="white", highlightthickness=1)
        self.puzzle.pack(padx=MARGIN, pady=MARGIN)
        self.btn_grid = []

        # self.draw_grid()
        self.create_board()

        self.window.mainloop()

    def create_board(self):
        frame_list = []
        for i in range(3):
            frame_list.append([])
            for j in range(3):
                frame = Frame(master=self.puzzle, bd=0, highlightthickness=1)
                frame.grid(row=i, column=j, sticky="nsew")
                frame.rowconfigure(0, minsize=50, weight=1)
                frame.columnconfigure(0, minsize=50, weight=1)
                frame.config(highlightbackground="black")
                frame_list[i].append(frame)

        for i in range(9):
            self.btn_grid.append([])
            for j in range(9):
                btn = Button(master=frame_list[i//3][j//3], bd=1, text=f"{i},{j}", relief=SUNKEN, width=3, height=1,
                             font=("Helvetica", 20), bg="white", activebackground="yellow")
                btn.grid(row=i % 3, column=j % 3)
                self.btn_grid[i].append(btn)

    # def draw_grid(self):
    #     for i in range(10):
    #         line_width = 2 if i % 3 == 0 else 1  # wider lines for borders and 3x3 boxes
    #         self.canvas.create_line((MARGIN + i * BOX_SIZE, MARGIN),
    #                                 (MARGIN + i * BOX_SIZE, MARGIN + BOARD_SIZE), width=line_width)
    #     for i in range(10):
    #         line_width = 2 if i % 3 == 0 else 1
    #         self.canvas.create_line((MARGIN, MARGIN + i * BOX_SIZE),
    #                                 (MARGIN + BOARD_SIZE, MARGIN + i * BOX_SIZE), width=line_width)
