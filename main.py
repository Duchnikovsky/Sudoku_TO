from controller.game_controller import GameController
from view.sudoku_view import SudokuView

if __name__ == "__main__":
    controller = GameController()
    app = SudokuView(controller)
    app.mainloop()
