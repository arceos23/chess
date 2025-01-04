from .piece import Piece
from .moves import can_move_vertically
import constants


class Rook(Piece):

    def __init__(self, is_white, file, rank, is_promotion):
        super().__init__(is_white, file, rank)
        self._is_promotion = is_promotion
        self._has_moved = False

    def __str__(self):
        return constants.WHITE_ROOK if self.is_white else constants.BLACK_ROOK

    def can_move(self, chessboard, file, rank):
        return can_move_vertically(
            chessboard, self.file, self.rank, file, rank, self.is_white
        )

    def __has_castling_rights(self):
        return not self._has_moved and not self.is_promotion

    def can_castle(self):
        return self.__has_castling_rights()

    @property
    def has_moved(self):
        return self._has_moved

    @has_moved.setter
    def has_moved(self, has_moved):
        if self._has_moved and not has_moved:
            raise ValueError(
                "Cannot set rook to not having moved when it already moved."
            )
        self._has_moved = has_moved
