# coding=utf-8
import unittest
from requests.status_codes import codes
from httpretty import activate, register_uri, GET
from cinemate import Cinemate
from tests.mock import reqresp as rr


class CinemateTestCase(unittest.TestCase):
    def setUp(self):
        self.cin = Cinemate(
            username='USERNAME',
            password='PASSWORD',
            passkey='PASSKEY',
            apikey='APIKEY',
        )

    def test_str(self):
        self.assertEqual(str(self.cin), '<Cinemate: USERNAME>')

    @activate
    def test_api_get(self):
        register_uri(GET, rr['stats.new']['req'], body=rr['stats.new']['resp'])
        register_uri(GET, rr['stats.wtf']['req'], body=rr['stats.wtf']['resp'])
        register_uri(GET, rr['account.wrong_status_code']['req'],
                     body=rr['account.wrong_status_code']['resp'],
                     status=rr['account.wrong_status_code']['status'])
        correct_url = 'stats.new'
        incorect_url = 'stats.wtf'
        req = self.cin.api_get(correct_url)
        self.assertEqual(req.status_code, codes.ok)
        self.assertNotIn('error', req.json())
        self.assertRaises(RuntimeError, self.cin.api_get, incorect_url)
        not_found_url = rr['account.wrong_status_code']['req']
        self.assertRaises(RuntimeError, self.cin.api_get, not_found_url)
