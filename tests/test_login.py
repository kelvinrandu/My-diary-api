import unittest
import json
from tests.base import BaseTests

class SignInTests(BaseTests):
    """ Tests validity of the login endpoint """


    def test_empty_email(self):
        """ Test for empty email """
        data = json.dumps({"email": "", "password":"123456"})
        response = self.client().post('/api/v1/login', data=data, content_type='application/json')
        self.assertEqual(response.status_code, 400)


    def test_empty_password(self):
        """ Test successful login """
        data = json.dumps({"email": "test@gmail", "password":""})
        response = self.client().post('/api/v1/login', data=data, content_type='application/json')
        self.assertEqual(response.status_code, 400)


    def test_successful_login(self):
        """ Test successful login """
        data = json.dumps({"email": "randukelvin@gamil", "password":"12345678"})
        response = self.client().post('/api/v1/login', data=data, content_type='application/json')
        self.assertEqual(response.status_code, 200)


    def test_wrong_email(self):
        """ Test for incorrect email"""
        data = json.dumps({"email": "teest@gmail", "password":"123456"})
        response = self.client().post('/api/v1/login', data=data, content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_wrong_password(self):
        """ Test successful login """
        data = json.dumps({"email": "test@gmail", "password":"12346"})
        response = self.client().post('/api/v1/login', data=data, content_type='application/json')
        self.assertEqual(response.status_code, 400)



