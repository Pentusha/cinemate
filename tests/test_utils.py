# coding=utf-8
from datetime import datetime
from cinemate import utils
from tests.test_cinemate import CinemateTestCase


class UtilsTestCase(CinemateTestCase):
    def test_parse_date(self):
         self.assertEqual(
             utils.parse_datetime('2011-04-09T15:38:30'),
             datetime(2011, 4, 9, 15, 38, 30)
         )