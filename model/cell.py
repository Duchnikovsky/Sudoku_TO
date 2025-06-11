class Cell:
    def __init__(self, value=0, fixed=False):
        self.value = value
        self.fixed = fixed

    def is_fixed(self):
        return self.fixed

    def set_value(self, value):
        if not self.fixed:
            self.value = value

    def get_value(self):
        return self.value
