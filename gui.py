from tkinter import *
from solver import solve

PADDING = 40
BOARD_SIZE = 540
CELL_SIZE = BOARD_SIZE // 9
CELL_COLOR = "white"
FONT = ("Helvetica", 20)
SPEED_MS = 1
DIFFICULTY = {"Easy": "easy",
              "Medium": "medium",
              "Hard": "hard"}


class SudokuUI:
    def __init__(self, board):
        self.board = board
        self.root = Tk()
        self.root.title("Sudoku Solver")
        self.puzzle = Frame(master=self.root, bg=CELL_COLOR, highlightthickness=1)
        self.puzzle.pack(padx=PADDING, pady=(PADDING, PADDING//3))
        self.button_grid = []

        self.create_board()

        menu = Frame(master=self.root)
        menu.pack(pady=(0, PADDING//3))
        Button(menu, text="l▶", font=("Helvetica", 10), command=lambda: self.change_speed(40)).grid(row=0, column=0)
        Button(menu, text="▶", width=2, font=("Helvetica", 10), command=lambda: self.change_speed(1)).grid(row=0, column=1)
        Button(menu, text="▶▶", font=("Helvetica", 10), command=lambda: self.change_speed(0)).grid(row=0, column=2)
        Button(menu, text="Solve", font=("Helvetica", 12),
               command=self.display_solver).grid(row=1, column=0, columnspan=3, pady=(5, 0), sticky="nsew")
        # self.solve_btn.pack(anchor="e", pady=(0, PADDING))

        # self.root.mainloop()

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
                             font=FONT, bg=CELL_COLOR)
                btn.grid(row=i % 3, column=j % 3, sticky="nsew")
                self.button_grid[i].append(btn)

        # Populate the board with initial values
        for row in range(9):
            for col in range(9):
                if 0 < self.board[row][col] < 10:
                    self.button_grid[row][col].config(text=self.board[row][col], command=None,
                                                      bg="#e6e6e6", activebackground="#e6e6e6")

    def fill_cell(self, row, col, number):
        self.button_grid[row][col].config(text=number, bg="gold")
        self.root.update()
        self.root.after(ms=SPEED_MS, func=None)
        self.button_grid[row][col].config(text=number, bg="light blue")
        self.root.update()
        # self.root.after(ms=MS, func=None)

    def empty_cell(self, row, col):
        self.button_grid[row][col].config(text="", bg=CELL_COLOR)
        # self.root.after(ms=SPEED_MS, func=print(row, col))
        self.root.update()

    def display_solver(self):
        solve(self.board, self, display=True)

    def change_speed(self, num):
        global SPEED_MS
        SPEED_MS = num


class SudokuNoInputUI(SudokuUI):
    def __init__(self, board):
        super().__init__(board)

        self.root.mainloop()


class SudokuUserInputUI(SudokuUI):
    def __init__(self):
        board = [[0 for col in range(9)] for row in range(9)]
        super().__init__(board)

        self.tracked_button = None
        for row in self.button_grid:
            for btn in row:
                btn.bind('<Button-1>', self.button_click)
        self.root.bind_all("<Key>", self.key_press)

        self.root.mainloop()

    def key_press(self, event):
        if self.tracked_button:
            if event.char.isdigit() and event.char != "0":  # 1 - 9
                key = int(event.char)
                self.tracked_button.config(text=key)  # TODO bg="#e6e6e6"?
            elif event.char == "0" or event.char == "":  # 0 or special characters (for deletion)
                self.tracked_button.config(text="")
            self.tracked_button.config(bg=CELL_COLOR)
            self.tracked_button = None

    def button_click(self, event):
        btn = event.widget
        if self.tracked_button:
            self.tracked_button.config(bg=CELL_COLOR)
        self.tracked_button = btn
        btn.config(bg="yellow")

    def display_solver(self):
        if solve(self.board, self, display=False):  # if puzzle solvable, then display solution
            solve(self.board, self, display=True)
            print(self.board)
            print("Done!")
        else:
            print("Puzzle not solvable.")
