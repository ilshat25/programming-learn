from django.test import TestCase

from core.models import Level
from .game_engine import GameEngine
from .results import ExecuteResult

CASE1 = "move;right;move;move;right;move;"
WAY1 = [
    (1, 1, (0, 1)),
    (1, 2, (0, 1)),
    (1, 2, (1, 0)),
    (2, 2, (1, 0)),
    (3, 2, (1, 0)),
    (3, 2, (0, -1)),
    (3, 1, (0, -1)),
]

CASE2 = "left;move;"
WAY2 = [
    (1, 1, (0, 1)),
    (1, 1, (-1, 0)),
]


class GameEngineTestCase(TestCase):
    def setUp(self):
        """level_map is equel 11111
                              10001
                              10101
                              11111"""
        Level.objects.create(level_map='11111100011010111111', width=5, height=4, x_start=1, y_start=1,
                             x_finish=3, y_finish=1, num=1)

    def eq(self, lhs, rhs):
        return lhs.win == rhs.win and lhs.way == rhs.way and lhs.num == rhs.num

    def test_game_engine_env(self):
        game_engine = GameEngine(1, CASE1)
        assert self.eq(game_engine.execute(), ExecuteResult(WAY1, game_engine._level))
        game_engine = GameEngine(1, CASE2)
        assert self.eq(game_engine.execute(), ExecuteResult(WAY2, game_engine._level))
