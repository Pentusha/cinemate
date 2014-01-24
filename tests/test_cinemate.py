# coding=utf-8
import unittest
from cinemate import Cinemate


class CinemateTestCase(unittest.TestCase):
    def setUp(self):
        self.cin = Cinemate(
            username='USERNAME',
            password='PASSWORD',
            passkey='PASSKEY',
            apikey='APIKEY',
        )
