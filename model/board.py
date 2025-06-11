from model.cell import Cell

class SudokuBoard:
    def __init__(self):
        self.grid = [[Cell() for _ in range(9)] for _ in range(9)]

    def get_cell(self, row, col):
        return self.grid[row][col]

    def set_cell(self, row, col, value):
        self.grid[row][col].set_value(value)

    def is_full(self):
        return all(cell.get_value() != 0 for row in self.grid for cell in row)

    def copy(self):
        new_board = SudokuBoard()
        for r in range(9):
            for c in range(9):
                val = self.grid[r][c].get_value()
                fixed = self.grid[r][c].is_fixed()
                new_board.grid[r][c] = Cell(val, fixed)
        return new_board
