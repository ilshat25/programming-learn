from django.test import TestCase

from core.models import Level
from enums.field_type import FieldType
from .level_wrapper import LevelWrapper

CASE1 = {
    'upper': FieldType.BARRIER,
    'down': FieldType.BARRIER,
    'left': FieldType.EMPTY,
    'right': FieldType.EMPTY,
}

CASE2 = {
    'upper': FieldType.BARRIER,
    'down': FieldType.EMPTY,
    'left': FieldType.BARRIER,
    'right': FieldType.EMPTY,
}

CASE3 = {
    'upper': FieldType.EMPTY,
    'down': FieldType.BARRIER,
    'left': FieldType.BARRIER,
    'right': FieldType.BARRIER,
}


class LevelWrapperTestCase(TestCase):
    def setUp(self):
        """level_map is equel 11111
                              10001
                              10101
                              11111"""
        Level.objects.create(level_map='11111100011010111111', width=5, height=4, x_start=1, y_start=1, x_finish=1, y_finish=2, num=1)

    def test_level_wrapper_env(self):
        level = LevelWrapper(1)
        self.assertEqual(level.get_env(2, 2), CASE1)
        self.assertEqual(level.get_env(1, 2), CASE2)
        self.assertEqual(level.get_env(1, 1), CASE3)
