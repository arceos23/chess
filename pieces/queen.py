from .piece import Piece
from .moves import (
    get_dx,
    get_dy,
    can_move_vertically,
    can_move_horizontally,
    can_move_diagonally,
)
import constants


class Queen(Piece):

    def __str__(self):
        return constants.WHITE_QUEEN if self.is_white else constants.BLACK_QUEEN

    def __is_vertical_move(self, file, rank):
        return get_dx(self.rank, rank) != 0 and get_dy(self.file, file) == 0

    def __is_horizontal_move(self, file, rank):
        return get_dx(self.rank, rank) == 0 and get_dy(self.file, file) != 0

    def __is_diagonal_move(self, file, rank):
        return abs(self.file - file) == abs(self.rank - rank)

    def can_move(self, chessboard, file, rank):
        return (
            self.__is_vertical_move(file, rank)
            and can_move_vertically(
                chessboard, self.file, self.rank, file, rank, self.is_white
            )
            or self.__is_horizontal_move(file, rank)
            and can_move_horizontally(
                chessboard, self.file, self.rank, file, rank, self.is_white
            )
            or self.__is_diagonal_move(file, rank)
            and can_move_diagonally(
                chessboard, self.file, self.rank, file, rank, self.is_white
            )
        )
