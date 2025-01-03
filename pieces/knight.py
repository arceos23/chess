from .piece import Piece
from .moves import can_jump
import constants


class Knight(Piece):

    def __str__(self):
        return f"{constants.KNIGHT}{self.get_color()}"

    def can_move(self, chessboard, file, rank):
        return can_jump(chessboard, self.file, self.rank, file, rank, self.is_white)
