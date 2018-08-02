from app import app

import unittest
import json
import sys
from tests.base import BaseTests




class BasicTestCase(BaseTests):

        
# test for get all entries
    def test_get_all(self):
        response = self.client().get('/api/v1/register', data=data, content_type='application/json')
        self.assertEqual(response.status_code, 200)

# test for get all entries
    def test_get_each(self):
        tester = self.client(self)
        response = self.client().get('/api/v1/entries/1', content_type='application/json')
        self.assertEqual(response.status_code, 200)


# test for post endpoint
    def test_post(self):
        data = json.dumps({
            "id": 1,
			"title":" Article one",
			"body":"This represents the body of the first article",
			"create_date":"04-25-2018"})
        response = self.client().post(
            '/api/v1/entries', data=data,
            content_type='application/json'
            )
        self.assertEqual(response.status_code, 201)
        
        

# test for update an entry
    def test_edit(self):
        data = json.dumps({
			"Body":"This represents the body of the first article"
			})
        response = self.client().put(
            '/api/v1/entries/2', data=data,
            content_type='application/json',
            )
        self.assertEqual(response.status_code, 200)
        


# delete entry endpoint test
    def test_delete(self):
        response = self.client().delete('/api/v1/entries/1', content_type='html/text')
        self.assertEqual(response.status_code, 200)



if __name__ == '__main__':
    unittest.main()
    