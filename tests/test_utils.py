# coding=utf-8
from datetime import datetime
from cinemate import utils
from tests.test_cinemate import CinemateTestCase


class UtilsTestCase(CinemateTestCase):
    def test_parse_datetime(self):
        self.assertEqual(
            utils.parse_datetime('2011-04-09T15:38:30'),
            datetime(2011, 4, 9, 15, 38, 30)
        )
        self.assertIsNone(utils.parse_datetime(''))

    def test_parse_date(self):
        self.assertEqual(
            utils.parse_date('2011-04-07'),
            datetime(2011, 4, 7)
        )
        self.assertIsNone(utils.parse_date(''))

    def test_required(self):
        dummy = type('Dummy', (object,), {
            'cinemate': self.cin,
            'decorated': utils.require('test')(lambda: None)
        })
        self.assertRaises(AttributeError, dummy().decorated)
