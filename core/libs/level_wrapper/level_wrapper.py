from core.models import Level
from core.libs.enums.field_type import FieldType


class LevelWrapper:
    _field_manager = {'0': FieldType.EMPTY, '1': FieldType.BARRIER}

    def _parse_level_map(self, level_map, width, height):
        level = [[FieldType.EMPTY for i in range(width)] for j in range(height)]
        for i in range(height):
            for j in range(width):
                idx = i * width + j
                level[i][j] = self._field_manager[level_map[idx]]
        return level

    def __init__(self, num):
        self._level = Level.objects.get(num=num)
        self._parsed_level = self._parse_level_map(self._level.level_map, self._level.width, self._level.height)

    def get_env(self, x, y):
        y = self._level.height - y - 1
        env = {
            (0, 1): self._parsed_level[y - 1][x],
            (0, -1): self._parsed_level[y + 1][x],
            (1, 0): self._parsed_level[y][x + 1],
            (-1, 0): self._parsed_level[y][x - 1],
        }
        return env

    def get_x_start(self):
        return self._level.x_start

    def get_y_start(self):
        return self._level.y_start

    def get_x_finish(self):
        return self._level.x_finish

    def get_y_finish(self):
        return self._level.y_finish

    def get_num(self):
        return self._level.num
