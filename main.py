from controller.game_controller import GameController
from view.console_view import ConsoleView


def main():
    view = ConsoleView()
    controller = GameController(view)
    controller.start_game()


if __name__ == "__main__":
    main()
