from enum import Enum


class Event(Enum):
    DEFAULT = 1
    MOVE = 2
    ROTATE_LEFT = 3
    ROTATE_RIGHT = 4
    MOVE_WHILE_EMPTY = 2
