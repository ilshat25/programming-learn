from enums.events import Event

COMMANDS_DATA = [
    ('left;', Event.ROTATE_LEFT),
    ('right;', Event.ROTATE_LEFT),
    ('move;', Event.ROTATE_LEFT),
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

            for raw_move, move_type in COMMANDS_DATA:
                if data.startswith(raw_move):
                    to_del = raw_move

            if Event.DEFAULT == event:
                raise ValueError
            data = data[len(to_del):]
            event.append(event)

        return events

    def get_event(self, x, y, direction):
        if not self._events:
            return Event.DEFAULT
        event = self._events.pop(0)
        if event == Event.MOVE:
            raise ValueError
        return self.pop(0)