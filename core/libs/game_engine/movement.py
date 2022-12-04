from core.libs.enums.events import Event


class Movement:

    def __init__(self, x, y, direction):
        self._x = x
        self._y = y
        self._direction = direction

    def _rotate_left(self):
        self._direction = (0 * self._direction[0] - 1 * self._direction[1],
                           1 * self._direction[0] + 0 * self._direction[1])

    def _rotate_right(self):
        self._direction = (0 * self._direction[0] + 1 * self._direction[1],
                           -1 * self._direction[0] + 0 * self._direction[1])

    def _move(self):
        self._x += self._direction[0]
        self._y += self._direction[1]

    def get_current_position(self):
        return self._x, self._y, self._direction

    def get_new_position(self, event):
        direction_manager = {
            Event.ROTATE_LEFT: self._rotate_left,
            Event.ROTATE_RIGHT: self._rotate_right,
            Event.MOVE: self._move,
        }
        direction_manager[event]()
        return self._x, self._y, self._direction
