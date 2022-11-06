from django.test import TestCase
from parser import Parser
from core.models import Level
from enums.events import Event
from libs.level_wrapper import LevelWrapper
class ParserTestCase(TestCase):
    def setUp(self):
        """level_map is equel 00000
                              00000
                              00000
                              00000"""
        Level.objects.create(level_map='11111100011010111111', width=5, height=4,
                             x_start=3, y_start=3, x_finish=1, y_finish=2, num=1)
        self.parser = Parser(
            data='move;right;left;move',
            level=LevelWrapper(1)
        )

    def test_level_parser(self):
        self.assertEqual(self.parser.get_event(3, 3, 'upper'), Event.MOVE)
        self.assertEqual(self.parser.get_event(2, 3, 'upper'), Event.ROTATE_RIGHT)
        self.assertEqual(self.parser.get_event(2, 3, 'right'), Event.ROTATE_LEFT)
        self.assertEqual(self.parser.get_event(2, 3, 'upper'), Event.DEFAULT)