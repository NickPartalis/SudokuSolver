from tkinter import *
from solver import solve
import pprint

PADDING = 40
BOARD_SIZE = 540
CELL_SIZE = BOARD_SIZE // 9
CELL_COLOR = "white"
FONT = ("Helvetica", 20)
MS = 1


# class SudokuCell(Button):
#     def __init__(self):
#         super().__init__()
#         self.btn = Button(master=frame_list[i // 3][j // 3], bd=1, text="", relief=SUNKEN, width=3, height=1,
#                font=("Helvetica", 20), bg=CELL_COLOR, activebackground="yellow")

class SudokuUI:
    def __init__(self, board):
        self.board = board
        self.root = Tk()
        self.root.title("Sudoku Solver")
        self.puzzle = Frame(master=self.root, bg=CELL_COLOR, highlightthickness=1)
        self.puzzle.pack(padx=PADDING, pady=PADDING)
        self.button_grid = []

        self.create_board()

        self.btn = Button(text="Solve", font=("Helvetica", 12), command=lambda: self.display_solver())
        self.btn.pack(anchor="s", pady=(0, 20))
        # self.display_solver()
        # solve(board=self.board, puzzle=self)

        self.root.mainloop()

    def create_board(self):
        # Create the board
        frame_list = []
        for i in range(3):
            frame_list.append([])
            for j in range(3):
                frame = Frame(master=self.puzzle, bd=0, highlightthickness=1, highlightbackground="black")
                frame.grid(row=i, column=j, sticky="nsew")
                frame.rowconfigure(0, minsize=CELL_SIZE, weight=1)
                frame.columnconfigure(0, minsize=CELL_SIZE, weight=1)
                frame_list[i].append(frame)

        for i in range(9):
            self.button_grid.append([])
            for j in range(9):
                btn = Button(master=frame_list[i//3][j//3], bd=1, text="", relief=SUNKEN, width=3, height=1,
                             font=FONT, bg=CELL_COLOR, activebackground="yellow")
                btn.grid(row=i % 3, column=j % 3, sticky="nsew")
                self.button_grid[i].append(btn)

        # Populate the board with initial values
        for row in range(9):
            for col in range(9):
                if 0 < self.board[row][col] < 10:
                    self.button_grid[row][col].config(text=self.board[row][col], command=None,
                                                      bg="#e6e6e6", activebackground="#e6e6e6")

    def change_btn_color(self, row, col, color):
        self.button_grid[row][col].config(bg=color)

    def fill_cell(self, row, col, number):
        self.button_grid[row][col].config(text=number, bg="gold")
        self.root.update()
        self.root.after(ms=MS, func=None)
        self.button_grid[row][col].config(text=number, bg="light blue")
        self.root.update()
        # self.root.after(ms=MS, func=None)

    def empty_cell(self, row, col):
        self.button_grid[row][col].config(text="", bg=CELL_COLOR)
        # self.root.after(ms=MS, func=print(row,col))
        self.root.update()

    def display_solver(self):
        solve(self.board, self)

    # def draw_grid(self):
    #     for i in range(10):
    #         line_width = 2 if i % 3 == 0 else 1  # wider lines for borders and 3x3 boxes
    #         self.canvas.create_line((MARGIN + i * BOX_SIZE, MARGIN),
    #                                 (MARGIN + i * BOX_SIZE, MARGIN + BOARD_SIZE), width=line_width)
    #     for i in range(10):
    #         line_width = 2 if i % 3 == 0 else 1
    #         self.canvas.create_line((MARGIN, MARGIN + i * BOX_SIZE),
    #                                 (MARGIN + BOARD_SIZE, MARGIN + i * BOX_SIZE), width=line_width)
