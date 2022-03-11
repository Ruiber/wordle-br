from enum import Enum

class LetterState(Enum):
    NOT_USED = 0
    NOT_IN_WORD = 1
    WRONG_PLACE = 2
    RIGHT_PLACE = 3

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        if isinstance(int):
            return self.value < other
