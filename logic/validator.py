class SudokuValidator:
    def is_valid(self, board):
        for i in range(9):
            if not self._is_unit_valid([board.get_cell(i, j).get_value() for j in range(9)]):
                return False
            if not self._is_unit_valid([board.get_cell(j, i).get_value() for j in range(9)]):
                return False

        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                block = [board.get_cell(r + i, c + j).get_value() for i in range(3) for j in range(3)]
                if not self._is_unit_valid(block):
                    return False

        return True

    def is_move_valid(self, board, row, col, value):
        original = board.get_cell(row, col).get_value()
        board.set_cell(row, col, value)
        valid = self.is_valid(board)
        board.set_cell(row, col, original)
        return valid

    def _is_unit_valid(self, unit):
        nums = [x for x in unit if x != 0]
        return len(nums) == len(set(nums))
