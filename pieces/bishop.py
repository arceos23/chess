from .piece import Piece
from .moves import can_move_diagonally
import constants


class Bishop(Piece):

    def __str__(self):
        return f"{constants.BISHOP}{self.get_color()}"

    def can_move(self, chessboard, file, rank):
        return can_move_diagonally(
            chessboard, self.file, self.rank, file, rank, self.is_white
        )
