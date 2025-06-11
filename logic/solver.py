import random
from logic.validator import SudokuValidator


class SudokuSolver:
    def solve(self, board):
        for r in range(9):
            for c in range(9):
                if board.get_cell(r, c).get_value() == 0:
                    numbers = list(range(1, 10))
                    random.shuffle(numbers)
                    for n in numbers:
                        board.set_cell(r, c, n)
                        if SudokuValidator().is_valid(board) and self.solve(board):
                            return True
                        board.set_cell(r, c, 0)
                    return False
        return True
