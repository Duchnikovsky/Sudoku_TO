class ConsoleView:
    def display(self, board):
        print("    " + " ".join(f"{i + 1}" for i in range(9)))
        print("   " + "-" * 21)
        for i, row in enumerate(board.grid):
            row_str = f"{i + 1:<2} | "
            for j, cell in enumerate(row):
                val = cell.get_value()
                row_str += str(val) if val != 0 else "."
                if (j + 1) % 3 == 0 and j < 8:
                    row_str += " | "
                else:
                    row_str += " "
            print(row_str)
            if (i + 1) % 3 == 0 and i < 8:
                print("   " + "-" * 21)

    def prompt_move(self):
        try:
            row = int(input("Podaj wiersz (1-9): ")) - 1
            col = int(input("Podaj kolumnę (1-9): ")) - 1
            value = int(input("Podaj wartość (1-9): "))
            return row, col, value
        except ValueError:
            print("Błędne dane wejściowe!")
            return None

    def show_message(self, msg):
        print(msg)

    def prompt_undo(self):
        choice = input("Cofnąć ostatni ruch? (t/n): ")
        return choice.lower().startswith("t")
