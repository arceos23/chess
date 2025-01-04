from chessboard import Chessboard
from loggger import Logger
from pieces import pawn
import constants


RANK_TO_ROW = {"8": 0, "7": 1, "6": 2, "5": 3, "4": 4, "3": 5, "2": 6, "1": 7}


def get_col(file):
    return ord(file) - ord("a")


def get_row(rank):
    return RANK_TO_ROW[rank]


def convert_rank_to_row(rank):
    return (rank - 1 + 5) % 8 - 1


def main():
    print(
        "\n\nWelcome to chess. Enter your moves in the format of source square and destination square separated by a dash. For example: a5-b6.\n"
    )
    reprompt_message = "Try again.\n"
    chessboard = Chessboard()
    logger = Logger()
    is_white = True
    while not chessboard.is_game_over():
        print(chessboard)
        move = input(f"\n{"White" if is_white else "Black"} to move: ")
        print()

        if "-" not in move:
            print(f"Missing dash. {reprompt_message}")
            continue

        source, destination = move.split("-")
        if (
            len(source) != 2
            or source[0] not in constants.FILES
            or int(source[1]) not in constants.RANKS
        ):
            print(f"Invalid source square. {reprompt_message}")
            continue
        elif (
            len(destination) != 2
            or destination[0] not in constants.FILES
            or int(destination[1]) not in constants.RANKS
        ):
            print(f"Invalid destination square. {reprompt_message}")
            continue

        source_row, source_col = get_row(source[1]), get_col(source[0])
        destination_row, destination_col = get_row(destination[1]), get_col(
            destination[0]
        )
        piece = chessboard.get_piece(source_col, source_row)
        if piece is None:
            print(f"A piece does not exist on the source square. {reprompt_message}")
            continue
        elif piece.is_white != is_white:
            print(f"You cannot move your opponent's piece. {reprompt_message}")
            continue

        if (
            type(piece) == pawn.Pawn
            and not piece.can_move(chessboard, destination_col, destination_row, logger)
            or type(piece) != pawn.Pawn
            and not piece.can_move(chessboard, destination_col, destination_row)
        ):
            print(f"{piece} cannot move to {destination}. {reprompt_message}")
            continue

        chessboard.move_piece(source_col, source_row, destination_col, destination_row)
        piece.file = destination_col
        piece.rank = destination_row

        is_white = not is_white

        logger.add_move(move)

    print(chessboard)
    print(chessboard.get_result())


if __name__ == "__main__":
    main()
