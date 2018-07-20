from app import app

import unittest
import json



class BasicTestCase(unittest.TestCase):
# test for succesful flask set up
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello, World!')
        
#test for get all entries
    def test_get_all(self):
        tester = app.test_client(self)
        response = tester.get('/api/v1/entries', content_type='html/text')
        self.assertEqual(response.status_code, 200)

# #test for post endpoint
    def test_post(self):
        tester = app.test_client(self)
        data = {"id":1,"title":"goal", "description":"Croatia won with 4 goals"}
        response = tester.post("/api/v1/entries", content_type="html/text")
        self.assertEqual(response.status_code, 400)

# #test for update an entry
    def test_edit(self):
        tester = app.test_client(self)
        data = {"id":1,"title":"article ", "body":"this is another one"}
        response = tester.put('/api/v1/entries/1', content_type='html/text')
        self.assertEqual(response.status_code, 400)
        
 


if __name__ == '__main__':
    unittest.main()
    