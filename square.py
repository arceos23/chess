from pieces import bishop, king, knight, pawn, queen, rook
import constants


class Square:

    def __init__(self):
        self.piece = None
        self._white_check_count = 0
        self._black_check_count = 0

    def __str__(self):
        if type(self.piece) == bishop.Bishop:
            char = constants.BISHOP
        elif type(self.piece) == king.King:
            char = constants.KING
        elif type(self.piece) == knight.Knight:
            char = constants.KNIGHT
        elif type(self.piece) == pawn.Pawn:
            char = constants.PAWN
        elif type(self.piece) == queen.Queen:
            char = constants.QUEEN
        elif type(self.piece) == rook.Rook:
            char = constants.ROOK
        else:
            char = "--"
        return char

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
