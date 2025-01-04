class Logger:

    def __init__(self):
        self.moves = []

    def add_move(self, move):
        self.moves.append(move)

    def get_last_move(self):
        self.moves[-1]
