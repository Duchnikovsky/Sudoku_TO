from model.generator import SudokuGenerator
from logic.validator import SudokuValidator
from model.move_history import MoveHistory


class GameController:
    def __init__(self):
        self.validator = SudokuValidator()
        self.history = MoveHistory()
        self.generator = SudokuGenerator()
        self.board = self.generator.generate()
        self.solution = self.generator.get_solution()

    def new_game(self):
        self.board = self.generator.generate()
        self.solution = self.generator.get_solution()
        self.history = MoveHistory()