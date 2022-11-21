from core.libs.level_wrapper.level_wrapper import LevelWrapper
from .movement import Movement
from .results import ExecuteResult
from core.libs.enums.events import Event
from core.libs.parser.parser import Parser


class GameEngine:

    def __init__(self, level_number, code):
        self._level = LevelWrapper(level_number)
        self._parser = Parser(code, self._level)

    def execute(self):
        geo = Movement(self._level.get_x_start(), self._level.get_y_start(), (0, 1))
        positions = [geo.get_current_position()]
        while True:
            try:
                event = self._parser.get_event(*geo.get_current_position())
            except ValueError:
                return ExecuteResult(positions, self._level)
            if event == Event.DEFAULT:
                break
            positions.append(geo.get_new_position(event))
        return ExecuteResult(positions, self._level)
