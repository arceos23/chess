from pieces import bishop, king, knight, pawn, queen, rook
import constants


class Square:

    def __init__(self):
        self.piece = None
        self._white_check_count = 0
        self._black_check_count = 0

    def __str__(self):
        return "__" if self.piece is None else str(self.piece)

    def is_empty(self):
        return self.piece is None

    @property
    def white_check_count(self):
        return self._white_check_count

    @white_check_count.setter
    def white_check_count(self, change):
        if abs(change) != 1:
            raise ValueError(
                "Chess rules dictate that this value can only change by at most one."
            )
        self._white_check_count += change

    @property
    def black_check_count(self):
        return self._black_check_count

    @black_check_count.setter
    def black_check_count(self, change):
        if abs(change) != 1:
            raise ValueError(
                "Chess rules dictate that this value can only change by at most one."
            )
        self._black_check_count += change
