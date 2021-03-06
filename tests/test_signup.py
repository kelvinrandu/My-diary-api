from app import app
import unittest
import json

from tests.base import BaseTests

class SignUpTests(BaseTests):
    """ Tests validity of the login endpoint """

    def test_empty_email(self):
        """ Test for empty email """
        data = json.dumps({"email": "", "username":"testre",
        "password": "1234564789", "confirm_password":"1234564789"})
        response = self.client().post('/api/v1/register', data=data, content_type='application/json')
        self.assertEqual(response.status_code, 400)


    def test_empty_password(self):
        """ Test for empty password """
        data = json.dumps({"email": "tetet@gmail.com", "username":"tetet",
        "password": "", "confirm_password":"1234564789"})
        response = self.client().post('/api/v1/register', data=data, content_type='application/json')
        self.assertEqual(response.status_code, 400)


    def test_empty_username(self):
        """ Test for empty username """
        data = json.dumps({"email": "hgdjek@gmail.com", "username":"",
        "password": "1234564789", "confirm_password":"1234564789"})
        response = self.client().post('/api/v1/register', data=data, content_type='application/json')
        self.assertEqual(response.status_code, 400)


    def test_successful_register(self):
        """ Test successful registration """
        data = json.dumps({"email": "randukelvin@gmail.com", "username":"kevo",
        "password": "1234564789", "confirm_password":"1234564789"})
        response = self.client().post('/api/v1/register', data=data, content_type='application/json')
        self.assertEqual(response.status_code, 200)


    def test_invalid_email(self):
        """ Test for wrong email format """
        data = json.dumps({"email": "hffjgmail.com", "username":"1234564789",
        "password": "1234564789", "confirm_password":"1234564789"})
        response = self.client().post('/api/v1/register', data=data, content_type='application/json')
        self.assertEqual(response.status_code, 400)

