from model.generator import SudokuGenerator
from logic.validator import SudokuValidator
from model.move_history import MoveHistory


class GameController:
    def __init__(self, view):
        self.view = view
        self.validator = SudokuValidator()
        self.history = MoveHistory()
        self.generator = SudokuGenerator()
        self.board = self.generator.generate()
        self.solution = self.generator.get_solution()

    def start_game(self):
        self.view.show_message("Witamy w Sudoku!")
        while not self.board.is_full():
            self.view.display(self.board)

            if self.view.prompt_undo() and self.history.has_undo():
                self.board = self.history.undo()
                self.view.show_message("Cofnięto ruch.")
                continue

            move = self.view.prompt_move()
            if move is None:
                continue

            row, col, value = move
            cell = self.board.get_cell(row, col)

            if cell.is_fixed():
                self.view.show_message("Nie można modyfikować tej komórki.")
                continue

            if not (1 <= value <= 9):
                self.view.show_message("Nieprawidłowa wartość. Podaj liczbę 1-9.")
                continue

            correct_value = self.solution.get_cell(row, col).get_value()
            if value != correct_value:
                self.view.show_message("Ruch niepoprawny")
                continue

            if not self.validator.is_move_valid(self.board, row, col, value):
                self.view.show_message("Ruch niepoprawny")
                continue

            self.history.save(self.board)
            self.board.set_cell(row, col, value)

        self.view.display(self.board)
        self.view.show_message("Gratulacje! Rozwiązałeś Sudoku.")
