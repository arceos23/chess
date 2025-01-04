from .piece import Piece
from .moves import can_jump
import constants


class Knight(Piece):

    def __str__(self):
        return constants.WHITE_KNIGHT if self.is_white else constants.BLACK_KNIGHT

    def can_move(self, chessboard, file, rank):
        return can_jump(chessboard, self.file, self.rank, file, rank, self.is_white)
