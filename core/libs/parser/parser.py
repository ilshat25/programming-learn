from core.libs.enums.events import Event
from core.libs.enums.field_type import FieldType

COMMANDS_DATA = [
    ('left;', Event.ROTATE_LEFT),
    ('right;', Event.ROTATE_RIGHT),
    ('move_while_empty;', Event.MOVE_WHILE_EMPTY),
    ('move;', Event.MOVE),
]


class Parser:
    def __init__(self, data, level):
        self._events = self.parse(data)
        self._level = level

    def parse(self, data):
        events = []
        while data:
            to_del = ''
            event = Event.DEFAULT
            data = data.strip()
            for raw_move, move_type in COMMANDS_DATA:
                if data.startswith(raw_move):
                    to_del = raw_move
                    event = move_type

            if Event.DEFAULT == event:
                raise ValueError
            data = data[len(to_del):]
            events.append(event)

        return events

    def get_event(self, x, y, direction):
        if not self._events:
            return Event.DEFAULT
        print(x, y, direction)
        if self._events[0] == Event.MOVE_WHILE_EMPTY:
            player_env = self._level.get_env(x, y)
            if direction not in player_env:
                raise ValueError
            if player_env[direction] != FieldType.EMPTY:
                self._events.pop(0)
                if not self._events:
                    return Event.DEFAULT
            else:
                return Event.MOVE
        event = self._events.pop(0)
        if event == Event.MOVE:
            player_env = self._level.get_env(x, y)
            if direction not in player_env or player_env[direction] != FieldType.EMPTY:
                raise ValueError
        return event
