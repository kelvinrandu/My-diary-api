from app import app
import unittest
import json


class BaseTests(unittest.TestCase):
    """ Tests validity of the login endpoint """

    def setUp(self):
        self.app = app
        self.client=self.app.test_client

    def tearDown(self):
        pass