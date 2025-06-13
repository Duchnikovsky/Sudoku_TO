import random
from model.board import SudokuBoard
from model.cell import Cell
from logic.solver import SudokuSolver


class SudokuGenerator:
    def __init__(self):
        self.solution = None  # dodane

    def generate(self):
        board = SudokuBoard()
        self._fill_board(board)
        self.solution = board.copy()
        self._remove_cells(board, count=10)
        return board

    def get_solution(self):
        return self.solution

    def _fill_board(self, board):
        solver = SudokuSolver()
        solver.solve(board)

    def _remove_cells(self, board, count):
        removed = 0
        while removed < count:
            r, c = random.randint(0, 8), random.randint(0, 8)
            cell = board.get_cell(r, c)
            if cell.get_value() != 0:
                cell.set_value(0)
                cell.fixed = False
                removed += 1
