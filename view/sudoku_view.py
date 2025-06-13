import tkinter as tk
from model.generator import SudokuGenerator
from model.move_history import MoveHistory
from logic.validator import SudokuValidator

class SudokuView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.title("Sudoku GUI")
        self.geometry("400x450")
        self.controller = controller
        self.entries = [[None for _ in range(9)] for _ in range(9)]
        self.draw_board()
        self.add_controls()

    def draw_board(self):
        for r in range(9):
            for c in range(9):
                val = self.controller.board.get_cell(r, c).get_value()
                entry = tk.Entry(self, width=2, font=('Arial', 18), justify='center')

                if self.controller.board.get_cell(r, c).is_fixed():
                    entry.insert(0, str(val))
                    entry.config(state='readonly', readonlybackground='lightgray')
                else:
                    entry.insert(0, "" if val == 0 else str(val))

                    def on_change(event, row=r, col=c, e=entry):
                        input_val = e.get()
                        if input_val.isdigit():
                            num = int(input_val)
                            correct = self.controller.solution.get_cell(row, col).get_value()
                            if num != correct:
                                self.show_message("Niepoprawna wartość!")
                                e.delete(0, tk.END)
                            else:
                                self.controller.history.save(self.controller.board.copy())
                                self.controller.board.set_cell(row, col, num)
                        elif input_val == "":
                            self.controller.board.set_cell(row, col, 0)
                        else:
                            e.delete(0, tk.END)

                    entry.bind("<KeyRelease>", on_change)

                entry.grid(row=r, column=c, padx=(2 if c % 3 == 0 else 0), pady=(2 if r % 3 == 0 else 0))
                self.entries[r][c] = entry

    def add_controls(self):
        tk.Button(self, text="Sprawdź", command=self.check_solution).grid(row=9, column=0, columnspan=3)
        tk.Button(self, text="Cofnij", command=self.undo_move).grid(row=9, column=3, columnspan=3)
        tk.Button(self, text="Nowa gra", command=self.new_game).grid(row=9, column=6, columnspan=3)

    def check_solution(self):
        valid = self.controller.validator.is_valid(self.controller.board)
        if valid and self.controller.board.is_full():
            self.show_message("Gratulacje! Rozwiązano Sudoku.")
        else:
            self.show_message("Błąd: plansza niepoprawna.")

    def undo_move(self):
        if self.controller.history.has_undo():
            self.controller.board = self.controller.history.undo()
            self.refresh()
        else:
            self.show_message("Brak ruchów do cofnięcia.")

    def new_game(self):
        self.controller.new_game()
        self.refresh()

    def refresh(self):
        for r in range(9):
            for c in range(9):
                cell = self.controller.board.get_cell(r, c)
                entry = self.entries[r][c]
                entry.config(state='normal')
                entry.delete(0, tk.END)
                if cell.get_value() != 0:
                    entry.insert(0, str(cell.get_value()))
                    if cell.is_fixed():
                        entry.config(state='readonly', readonlybackground='lightgray')
                else:
                    entry.insert(0, "")

    def show_message(self, message):
        popup = tk.Toplevel(self)
        popup.title("Info")
        tk.Label(popup, text=message).pack(pady=10)
        tk.Button(popup, text="OK", command=popup.destroy).pack(pady=5)

class GameControllerGUI:
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

if __name__ == "__main__":
    controller = GameControllerGUI()
    app = SudokuGUI(controller)
    app.mainloop()
