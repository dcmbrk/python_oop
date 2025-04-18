from enum import Enum, auto


class Mark(Enum):
    X = 'X'
    O = 'O'


class Status(Enum):
    EMPTY = 'EMPTY'
    X = 'X'
    O = 'O'
