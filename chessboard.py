from square import Square
from pieces import bishop, king, knight, pawn, queen, rook
import constants


class Chessboard:

    __END_RANK_ORDER = (
        constants.ROOK,
        constants.KNIGHT,
        constants.BISHOP,
        constants.QUEEN,
        constants.KING,
        constants.BISHOP,
        constants.KNIGHT,
        constants.ROOK,
    )

    def __init__(self):
        self.board = [[Square()] * 8 for _ in range(8)]
        for file, char in enumerate(self.__END_RANK_ORDER):
            match char:
                case constants.ROOK:
                    black = rook.Rook(False, file, constants.BLACK_START_RANK, False)
                    white = rook.Rook(True, file, constants.WHITE_START_RANK, False)
                case constants.KNIGHT:
                    black = knight.Knight(False, file, constants.BLACK_START_RANK)
                    white = knight.Knight(True, file, constants.WHITE_START_RANK)
                case constants.BISHOP:
                    black = bishop.Bishop(False, file, constants.BLACK_START_RANK)
                    white = bishop.Bishop(True, file, constants.WHITE_START_RANK)
                case constants.QUEEN:
                    black = queen.Queen(False, file, constants.BLACK_START_RANK)
                    white = queen.Queen(True, file, constants.WHITE_START_RANK)
                case constants.KING:
                    black = king.King(False, file, constants.BLACK_START_RANK)
                    white = king.King(True, file, constants.WHITE_START_RANK)
            self.board[constants.BLACK_START_RANK][file] = black
            self.board[constants.WHITE_START_RANK][file] = white

            self.board[constants.BLACK_START_RANK + 1][file] = pawn.Pawn(
                False, file, constants.BLACK_START_RANK + 1
            )
            self.board[constants.WHITE_START_RANK - 1][file] = pawn.Pawn(
                True, file, constants.WHITE_START_RANK - 1
            )

    def __str__(self):
        files = f'  {"  ".join(constants.FILES)}  '
        board_rep = []
        board_rep.append(files)
        for rank, row in enumerate(self.board):
            current_rank = str(constants.RANKS[rank])
            board_rep.append(
                f'{current_rank} {" ".join(str(piece) for piece in row)} {current_rank}'
            )
        board_rep.append(files)
        return "\n".join(board_rep)

    def is_check(self, file, rank, is_white):
        pass

    def is_empty(self, rank, file):
        return self.board[rank][file].is_empty()

    def get_piece(self, rank, file):
        return self.board[rank][file].piece
