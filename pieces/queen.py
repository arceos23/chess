from .piece import Piece
from .moves import can_move_vertically, can_move_horizontally, can_move_diagonally
import constants


class Queen(Piece):

    def __str__(self):
        return f"{constants.QUEEN}{self.get_color()}"

    def can_move(self, chessboard, file, rank):
        return (
            can_move_vertically(
                chessboard, self.file, self.rank, file, rank, self.is_white
            )
            or can_move_horizontally(
                chessboard, self.file, self.rank, file, rank, self.is_white
            )
            or can_move_diagonally(
                chessboard, self.file, self.rank, file, rank, self.is_white
            )
        )
