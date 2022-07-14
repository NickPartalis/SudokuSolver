# SudokuSolver
A Tkinter app that solves Sudoku puzzles. The app can either solve random puzzles (difficulty chosen by the user) or puzzles provided by the user.

The app uses recursion and backtracking to find a valid solution to the provided puzzle and visualizes each step of the solving algorithm. The user can choose to change the speed in which the app displays the steps, or to skip them entirely and just display the solution. 

## First option: Random puzzle
The app receives a random Sudoku puzzle from Roberto Ortega's Sugoku API (https://github.com/bertoort/sugoku) with a difficulty chosen by the user (easy, medium, hard or random).

![mode1](https://user-images.githubusercontent.com/4154061/179052230-02de17d1-af52-4acb-bb1f-877a83fdf10f.gif)

## Second option: User input
The app allows the user to input their own Sudoku puzzle. Each cell is clickable and the user can add and remove any 1-9 number. If the final puzzle provided by the user can be solved, the app will display the algorithm steps like normal (unless skipped by the user), otherwise the user will get an error message.

![mode2](https://user-images.githubusercontent.com/4154061/179052745-e2d5d6fd-367d-4f56-aba3-409f139aecb4.gif)

Note: Since the solving algorithm uses backtracking, and displaying each step with Tkinter delays the algorithm further, the required time to display all steps varies from less than a second to a couple of minutes, depending on the puzzle. Disabling the step display reduces the solving time significantly.
