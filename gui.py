from tkinter import *
from tkinter import messagebox
from solver import solve, is_solvable
import requests

PADDING = 40
BOARD_SIZE = 540
CELL_SIZE = BOARD_SIZE // 9
CELL_COLOR = "white"
FONT = "Trebuchet"
DIFFICULTY = {"Easy": "easy",
              "Medium": "medium",
              "Hard": "hard"}


class MainMenu:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("610x600")
        self.root.resizable(False, False)
        self.root.title("Sudoku Solver")

        bg = PhotoImage(file="assets/sudoku_bg.png")
        self.canvas1 = Canvas(self.root)
        self.canvas1.pack(fill="both", expand=True)
        self.canvas1.create_image(0, 0, image=bg, anchor="nw")

        self.canvas1.create_text(300, 120, text="SudokuSolver", font=(FONT, 28, "bold"))

        mode1_btn = Button(width=18, text="Get a random puzzle", font=(FONT, 14), command=self.get_random_puzzle)
        mode2_btn = Button(width=18, text="Input your own puzzle", font=(FONT, 14), command=self.input_own_puzzle)
        exit_btn = Button(text="Exit", font=(FONT, 14), command=self.root.destroy)
        mode1_btn.place(x=190, y=290)
        mode2_btn.place(x=190, y=345)
        exit_btn.place(x=280, y=400)

        self.root.mainloop()

    @staticmethod
    def get_random_puzzle():
        SudokuRandomPuzzleUI()

    @staticmethod
    def input_own_puzzle():
        SudokuUserPuzzleUI()


class SudokuUI:
    def __init__(self, board):
        self.board = board
        self.root = Toplevel()
        self.root.title("Sudoku Solver")
        self.root.resizable(False, False)
        self.puzzle = Frame(master=self.root, bg=CELL_COLOR, highlightthickness=1)
        self.puzzle.pack(padx=PADDING, pady=(PADDING, PADDING // 3))
        self.speed_ms = 1
        self.button_grid = []

        self.create_board()

        menu = Frame(master=self.root)
        menu.pack()
        Button(menu, text="l▶", font=(FONT, 10), command=lambda: self.change_speed(40)).grid(row=0, column=0)
        Button(menu, text="▶", width=2, font=(FONT, 10), command=lambda: self.change_speed(1)).grid(row=0, column=1)
        Button(menu, text="▶▶", font=(FONT, 10), command=lambda: self.change_speed(0)).grid(row=0, column=2)
        self.solve_btn = Button(menu, text="Solve", font=(FONT, 12), command=self.display_solver)
        self.solve_btn.grid(row=1, column=0, columnspan=3, pady=(5, 0), sticky="nsew")

        self.display_check_var = IntVar()
        self.display_check = Checkbutton(self.root, text="Display algorithm steps", font=(FONT, 11),
                                         variable=self.display_check_var, onvalue=1, offvalue=0)
        self.display_check.pack(pady=(0, PADDING // 3))
        self.display_check.select()

    def create_board(self):
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
                btn = Button(master=frame_list[i // 3][j // 3], bd=1, text="", relief=SUNKEN, width=3, height=1,
                             font=(FONT, 20), bg=CELL_COLOR)
                btn.grid(row=i % 3, column=j % 3, sticky="nsew")
                self.button_grid[i].append(btn)

    def fill_cell(self, row, col, number):
        self.button_grid[row][col].config(text=number, bg="gold")
        self.root.update()
        self.root.after(ms=self.speed_ms, func=None)
        self.button_grid[row][col].config(bg="light blue")
        self.root.update()

    def empty_cell(self, row, col):
        self.button_grid[row][col].config(text="", bg=CELL_COLOR)
        self.root.update()

    def display_solver(self):
        self.solve_btn["state"] = DISABLED
        self.display_check["state"] = DISABLED

        if self.display_check_var.get() == 1:
            solve(self.board, self, display=True)
        else:
            solve(self.board, self, display=False)
            for row in range(9):
                for col in range(9):
                    if self.button_grid[row][col]["text"] == "":
                        self.button_grid[row][col].config(text=self.board[row][col], bg="light blue")
                        self.root.update()
                        self.root.after(ms=self.speed_ms, func=None)

        self.solve_btn["state"] = NORMAL

    def change_speed(self, num):
        self.speed_ms = num


class SudokuRandomPuzzleUI(SudokuUI):
    def __init__(self):
        board = self.generate_puzzle("random")
        super().__init__(board)

        # self.root.mainloop()

    def create_board(self):
        super().create_board()

        # Populate the board with initial values
        for row in range(9):
            for col in range(9):
                if 0 < self.board[row][col] < 10:
                    self.button_grid[row][col].config(text=self.board[row][col], command=None,
                                                      bg="#e6e6e6", activebackground="#e6e6e6")

    def display_solver(self):
        super().display_solver()
        self.solve_btn.config(text="Again", command=lambda: [SudokuRandomPuzzleUI(), self.root.destroy()])

    @staticmethod
    def generate_puzzle(difficulty):
        if difficulty not in ("easy", "medium", "hard"):
            difficulty = "random"

        # Sugoku API from Roberto Ortega (https://github.com/bertoort)
        url = "https://sugoku.herokuapp.com/board"
        params = {"difficulty": difficulty}

        response = requests.request("GET", url, params=params)
        return response.json()["board"]


class SudokuUserPuzzleUI(SudokuUI):
    def __init__(self):
        board = [[0 for _ in range(9)] for _ in range(9)]
        super().__init__(board)

        self.tracked_button = None
        for row in self.button_grid:
            for btn in row:
                btn.bind("<Button-1>", self.button_click)
        self.root.bind_all("<Key>", self.key_press)

        # self.root.mainloop()

    def key_press(self, event):
        if self.tracked_button:
            if event.char.isdigit() and event.char != "0":  # 1 - 9
                key = int(event.char)
                self.tracked_button.config(text=key)
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
        self.root.unbind_all("<Key>")
        # Add user input into board
        for row in range(9):
            for col in range(9):
                self.button_grid[row][col].unbind("<Button-1>")
                if self.button_grid[row][col]["text"] and 1 <= self.button_grid[row][col]["text"] <= 9:
                    self.button_grid[row][col].config(bg="#e6e6e6", activebackground="#e6e6e6")
                    self.board[row][col] = int(self.button_grid[row][col]["text"])

        if is_solvable(self.board):  # if puzzle solvable, then display solution
            super().display_solver()
        else:
            messagebox.showerror(parent=self.root, title="Unsolvable Puzzle",
                                 message="The puzzle you provided cannot be solved!")

        self.solve_btn.config(text="Again", command=lambda: [SudokuUserPuzzleUI(), self.root.destroy()])
