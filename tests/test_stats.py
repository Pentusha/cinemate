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
        self.assertIn('users_count', stats)
        self.assertIsInstance(stats['users_count'], int)
        self.assertEqual(stats['users_count'], 4)
        self.assertIn('reviews_count', stats)
        self.assertIsInstance(stats['reviews_count'], int)
        self.assertEqual(stats['reviews_count'], 0)
        self.assertIn('comments_count', stats)
        self.assertIsInstance(stats['comments_count'], int)
        self.assertEqual(stats['comments_count'], 2)
        self.assertIn('movies_count', stats)
        self.assertIsInstance(stats['movies_count'], int)
        self.assertEqual(stats['movies_count'], 7)
