class MoveHistory:
    def __init__(self):
        self.history = []

    def save(self, board):
        self.history.append(board.copy())

    def undo(self):
        if self.history:
            return self.history.pop()
        return None

    def has_undo(self):
        return bool(self.history)
