# coding=utf-8
from datetime import datetime
from httpretty import activate, register_uri, GET
from tests.test_cinemate import CinemateTestCase
from tests.mock import reqresp as rr
from six import u


class AccountTestCase(CinemateTestCase):
    @activate
    def test_auth(self):
        register_uri(GET,
                     rr['account.auth']['req'],
                     body=rr['account.auth']['resp'])
        self.cin.account.auth()
        self.assertEqual(self.cin.passkey, 'of3k4oasd9498dfvjh5hthhgfgdfy')

    @activate
    def test_profile(self):
        register_uri(GET,
                     rr['account.profile']['req'],
                     body=rr['account.profile']['resp'])
        profile = self.cin.account.profile()
        self.assertIsInstance(profile, dict)
        self.assertEqual(profile['username'], 'UserName')
        self.assertEqual(profile['reputation'], 125)
        self.assertEqual(profile['review_count'], 11)
        self.assertEqual(profile['gold_badges'], 2)
        self.assertEqual(profile['silver_badges'], 14)
        self.assertEqual(profile['bronze_badges'], 21)
        self.assertEqual(profile['unread_pm_count'], 3)
        self.assertEqual(profile['unread_forum_count'], 7)
        self.assertEqual(profile['unread_updatelist_count'], 2)
        self.assertEqual(profile['subscription_count'], 96)

    @activate
    def test_updatelist(self):
        register_uri(GET,
                     rr['account.updatelist']['req'],
                     body=rr['account.updatelist']['resp'])
        lst = self.cin.account.updatelist()
        first = lst[0]
        self.assertIsInstance(lst, list)
        self.assertEqual(len(lst), 4)
        self.assertIsInstance(first, dict)
        self.assertEqual(first['date'], datetime(2011, 4, 9, 15, 38, 30))
        self.assertIsInstance(first['for_object'], self.cin.movie)
        self.assertEqual(first['description'], u('Новая раздача'))
        self.assertEqual(first['url'], 'http://cinemate.cc/watchlist/a415ef22a4b7ebf24bc54d7ad9a92fa4612cb49f/read/400813/')
        self.assertEqual(first['new'], 1)

    @activate
    def test_watchlist(self):
        register_uri(GET,
             rr['account.watchlist']['req'],
             body=rr['account.watchlist']['resp'])
        wlst = self.cin.account.watchlist()
        self.assertIsInstance(wlst, dict)
        self.assertIn('movie', wlst)
        self.assertIn('person', wlst)
        self.assertIsInstance(wlst['movie'], list)
        self.assertIsInstance(wlst['person'], list)
        self.assertEqual(len(wlst['movie']), 2)
        self.assertEqual(len(wlst['person']), 2)
        movie = wlst['movie'][0]
        self.assertIsInstance(movie, self.cin.movie)
        person = wlst['person'][0]
        self.assertIsInstance(person, self.cin.person)
