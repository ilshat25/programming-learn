from enums.field_type import FieldType
from core.models import Level


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
        self.level = Level.objects.get(num=num)
        self.parsed_level = self._parse_level_map(self.level.level_map, self.level.width, self.level.height)

    def get_env(self, x, y):
        y = self.level.height - y - 1
        env = {
            'upper': self.parsed_level[y - 1][x],
            'down': self.parsed_level[y + 1][x],
            'right': self.parsed_level[y][x + 1],
            'left': self.parsed_level[y][x - 1],
        }
        return env
