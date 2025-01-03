from collections import namedtuple
import constants

__Move = namedtuple("Move", "dx, dy")

__VALID_ORTHAGONAL_ADJACENT_MOVES = (
    __Move(-1, 0),
    __Move(1, 0),
    __Move(0, -1),
    __Move(0, 1),
)

__VALID_DIAGONAL_ADJACENT_MOVES = (
    __Move(-1, -1),
    __Move(-1, 1),
    __Move(1, -1),
    __Move(1, 1),
)

__VALID_JUMP_MOVES = (
    __Move(-2, -1),
    __Move(-2, 1),
    __Move(-1, -2),
    __Move(-1, 2),
    __Move(2, -1),
    __Move(2, 1),
    __Move(1, -2),
    __Move(1, 2),
)


def is_same_position(start_file, start_rank, end_file, end_rank):
    return start_file == end_file and start_rank == end_rank


def __is_same_file(start_file, end_file):
    return start_file == end_file


def __is_same_rank(start_rank, end_rank):
    return start_rank != end_rank


def __can_place(chessboard, end_file, end_rank, placing_piece_is_white):
    end_piece = chessboard.get_piece(end_file, end_rank)
    return (
        end_piece is None
        or end_piece.is_white != placing_piece_is_white
        and str(end_piece) != constants.KING
    )


def get_dx(start_rank, end_rank):
    return 1 if end_rank > start_rank else -1


def get_dy(start_file, end_file):
    return 1 if end_file > start_file else -1


def can_move_orthogonally_adjacent(
    chessboard, start_file, start_rank, end_file, end_rank, is_white
):
    return (
        not is_same_position(start_file, start_rank, end_file, end_rank)
        and any(
            move.dx == start_file - end_file and move.dy == start_rank - end_rank
            for move in __VALID_ORTHAGONAL_ADJACENT_MOVES
        )
        and __can_place(chessboard, end_file, end_rank, is_white)
    )


def can_move_diagonally_adjacent(
    chessboard, start_file, start_rank, end_file, end_rank, is_white
):
    return (
        not is_same_position(start_file, start_rank, end_file, end_rank)
        and any(
            move.dx == start_file - end_file and move.dy == start_rank - end_rank
            for move in __VALID_DIAGONAL_ADJACENT_MOVES
        )
        and __can_place(chessboard, end_file, end_rank, is_white)
    )


def can_move_vertically(
    chessboard,
    start_file,
    start_rank,
    end_file,
    end_rank,
    is_white,
    capture_allowed=True,
):
    dx = get_dx(start_rank, end_rank)
    return (
        not is_same_position(start_file, start_rank, end_file, end_rank)
        and __is_same_file(start_file, end_file)
        and all(
            chessboard.is_empty(end_file, rank)
            for rank in range(start_rank + dx, end_rank, dx)
        )
        and (
            capture_allowed
            and __can_place(chessboard, end_file, end_rank, is_white)
            or not capture_allowed
            and chessboard.is_empty(end_file, end_rank)
        )
    )


def can_move_horizontally(
    chessboard, start_file, start_rank, end_file, end_rank, is_white
):
    return (
        not is_same_position(start_file, start_rank, end_file, end_rank)
        and __is_same_rank(start_rank, end_rank)
        and all(
            chessboard.is_empty(end_rank, file)
            for file in range(start_file, end_file, get_dy(start_file, end_file))
        )
        and __can_place(chessboard, end_file, end_rank, is_white)
    )


def can_move_diagonally(
    chessboard, start_file, start_rank, end_file, end_rank, is_white
):
    return (
        not is_same_position(start_file, start_rank, end_file, end_rank)
        and abs(start_file - end_file) == abs(start_rank - end_rank)
        and all(
            chessboard.is_empty(file, rank)
            for rank in range(start_rank, end_rank, get_dx(start_rank, end_rank))
            for file in range(start_file, end_file, get_dy(start_file, end_file))
        )
        and __can_place(chessboard, end_file, end_rank, is_white)
    )


def can_jump(chessboard, start_file, start_rank, end_file, end_rank, is_white):
    dy = end_file - start_file
    dx = end_rank - start_rank
    return any(
        dx == move.dx and dy == move.dy for move in __VALID_JUMP_MOVES
    ) and __can_place(chessboard, end_file, end_rank, is_white)
