from .piece import Piece
from .moves import can_move_diagonally
import constants


class Bishop(Piece):

    def __str__(self):
        return constants.WHITE_BISHOP if self.is_white else constants.BLACK_BISHOP

    def can_move(self, chessboard, file, rank):
        return can_move_diagonally(
            chessboard, self.file, self.rank, file, rank, self.is_white
        )
