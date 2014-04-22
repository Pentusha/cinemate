# coding=utf-8
from functools import partial
from unittest import TestCase

from httpretty import activate, register_uri, GET
from requests.status_codes import codes

from cinemate import Cinemate
from tests.mock import reqresp as rr


class CinemateTestCase(TestCase):
    def setUp(self):
        self.cin = Cinemate(
            username='USERNAME',
            password='PASSWORD',
            passkey='PASSKEY',
            apikey='APIKEY',
        )
        self.register_uri = partial(register_uri, method=GET)

    def test_str(self):
        self.assertEqual(str(self.cin), '<Cinemate: USERNAME>')

    @activate
    def test_api_get(self):
        correct_url = 'stats.new'
        incorect_url = 'stats.wtf'
        wrong_status_url = 'account.wrong_status_code'
        self.register_uri(**rr[correct_url])
        self.register_uri(**rr[incorect_url])
        self.register_uri(**rr[wrong_status_url])
        req = self.cin.api_get(correct_url)
        self.assertEqual(req.status_code, codes.ok)
        self.assertNotIn('error', req.json())
        self.assertRaises(RuntimeError, self.cin.api_get, incorect_url)
        not_found_url = rr[wrong_status_url]['uri']
        self.assertRaises(RuntimeError, self.cin.api_get, not_found_url)
