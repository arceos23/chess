from .piece import Piece
from .moves import can_move_orthogonally_adjacent, can_move_diagonally_adjacent
import constants


class King(Piece):

    def __init__(self, is_white, file, rank):
        super().__init__(is_white, file, rank)
        self._has_moved = False

    def __str__(self):
        return constants.WHITE_KING if self.is_white else constants.BLACK_KING

    def can_move(self, chessboard, file, rank):
        return (
            can_move_orthogonally_adjacent(
                chessboard, self.file, self.rank, file, rank, self.is_white
            )
            or can_move_diagonally_adjacent(
                chessboard, self.file, self.rank, file, rank, self.is_white
            )
        ) and not chessboard.is_check(file, rank, self.is_white)

    def __has_castling_rights(self):
        return not self._has_moved

    def __get_castle_direction(self, is_kingside):
        return 1 if is_kingside else -1

    def __get_castle_file(self, is_kingside):
        return 7 if is_kingside else 2

    def __is_castle_piece_obstructed(self, chessboard, is_kingside):
        dx = self.__get_castle_direction(self, is_kingside)
        new_file = self.__get_castle_file(is_kingside)
        return any(
            not chessboard.is_empty(self.rank, file) is not None
            for file in range(self.file + dx, new_file + dx, dx)
        )

    def __is_castle_check_obstructed(self, chessboard, is_kingside):
        dx = self.__get_castle_direction(self, is_kingside)
        new_file = self.__get_castle_file(is_kingside)
        return any(
            not chessboard.is_check(self.rank, file, self.is_white)
            for file in range(self.file, new_file + dx, dx)
        )

    def can_castle(self, move, chessboard):
        if move != "0-0" and move != "0-0-0":
            return False

        is_kingside = True if move == "0-0" else False
        return (
            self.__has_castling_rights()
            and not self.__is_castle_piece_obstructed(chessboard, is_kingside)
            and not self.__is_castle_check_obstructed(chessboard, is_kingside)
        )

    @property
    def has_moved(self):
        return self._has_moved

    @has_moved.setter
    def has_moved(self, has_moved):
        if self._has_moved and not has_moved:
            raise ValueError(
                "Cannot set king to not having moved when it already moved."
            )
        self._has_moved = has_moved
