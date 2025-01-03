from .piece import Piece
from .king import King
from .moves import can_move_vertically, get_dx, get_dy
import constants


class Pawn(Piece):

    def __init__(self, is_white, file, rank):
        super().__init__(is_white, file, rank)
        self._has_moved = False

    def __str__(self):
        return f"{constants.PAWN}{self.get_color()}"

    def __is_valid_vertical_direction(self, start_rank, end_rank):
        dx = get_dx(start_rank, end_rank)
        return dx < 0 and self.is_white or dx > 0 and not self.is_white

    def __can_capture(self, chessboard, file, rank):
        capturing_piece = chessboard.get_piece(rank, file)
        return (
            capturing_piece is not None
            and type(capturing_piece) != King
            and capturing_piece.is_white != self.is_white
            and abs(get_dx(self.rank, rank)) == 1
            and abs(get_dy(self.file, file)) == 1
        )

    def __can_en_passant(self, chessboard, file, logger):
        expected_opposing_pawn_rank = 3 if self.is_white else 4
        if self.rank != expected_opposing_pawn_rank:
            return False

        piece = chessboard.get_piece(file, self.rank)
        if type(piece) != Pawn or piece.is_white == self.is_white:
            return False

        last_move = logger.get_last_move()
        return last_move[-1] == 2

    def __get_starting_rank(self):
        return 6 if self.is_white else 1

    def __has_moved(self):
        return self.rank != self.__get_starting_rank()

    def can_move(self, chessboard, file, rank, logger):
        if not self.__is_valid_vertical_direction(self.rank, rank):
            return False

        moves_forward = abs(rank - self.rank)
        if moves_forward == 1:
            return (
                self.__can_capture(chessboard, file, rank)
                or can_move_vertically(
                    chessboard, self.file, self.rank, file, rank, self.is_white, False
                )
                or self.__can_en_passant(chessboard, file, logger)
            )
        elif moves_forward == 2:
            return not self.__has_moved() and can_move_vertically(
                chessboard, self.file, self.rank, file, rank, self.is_white, False
            )
        return False

    @property
    def has_moved(self):
        return self._has_moved

    @has_moved.setter
    def has_moved(self, has_moved):
        if self._has_moved and not has_moved:
            raise ValueError(
                "Cannot set pawn to not having moved when it already moved."
            )
        self._has_moved = has_moved
