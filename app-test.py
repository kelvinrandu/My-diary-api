from app import app 

import unittest
import json
import sys




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

#test for get all entries
    def test_get_each(self):
        tester = app.test_client(self)
        response = tester.get('/api/v1/entries/1', content_type='application/json')
        self.assertEqual(response.status_code, 200)


# #test for post endpoint
    def test_post(self):
        tester = app.test_client(self)
        data = json.dumps({
            "id": 1,
			"title":" Article one",
			"body":"This represents the body of the first article",
			"create_date":"04-25-2018"})
        response = tester.post(
            '/api/v1/entries', data=data,
            content_type='application/json'
            )
        self.assertEqual(response.status_code, 201)
        
        

# #test for update an entry
    def test_edit(self):
        tester = app.test_client(self)
        data = json.dumps({
			"Body":"This represents the body of the first article"
			})
        response = tester.put(
            '/api/v1/entries/2', data=data,
            content_type='application/json',
            )
        self.assertEqual(response.status_code, 200)
        


#delete entry endpoint test
    def test_delete(self):
        tester = app.test_client(self)
        response = tester.delete('/api/v1/entries/1', content_type='html/text')
        self.assertEqual(response.status_code, 200)



if __name__ == '__main__':
    unittest.main()
    