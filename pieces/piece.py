from abc import ABC, abstractmethod
import constants


class Piece(ABC):

    def __init__(self, is_white, file, rank):
        self.is_white = is_white
        self.file = file
        self.rank = rank

    @abstractmethod
    def can_move(self, chessboard, file, rank):
        """Return True if the piece can move to the new file and rank."""
        pass

    def get_color(self):
        return constants.WHITE if self.is_white else constants.BLACK
