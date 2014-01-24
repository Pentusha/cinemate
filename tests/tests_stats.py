# coding=utf-8
from httpretty import activate, register_uri, GET
from tests.test_cinemate import CinemateTestCase
from tests.mock import reqresp as rr


class StatsTestCase(CinemateTestCase):
    @activate
    def test_new(self):
        register_uri(GET,
                     rr['stats.new']['req'],
                     body=rr['stats.new']['resp'])
        stats = self.cin.stats.new()
        self.assertIsInstance(stats, dict)
        self.assertEqual(stats['users_count'], 4)
        self.assertEqual(stats['reviews_count'], 0)
        self.assertEqual(stats['comments_count'], 2)
        self.assertEqual(stats['movies_count'], 7)
