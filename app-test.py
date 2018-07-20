from app import app

import unittest


class BasicTestCase(unittest.TestCase):

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello, World!')


#delete entry endpoint test
    def test_index(self):
        tester = app.test_client(self)
        response = tester.delete('/api/v1/entries/<int:id>', content_type='html/text')
       # self.assertEqual(response.status_code, 200)
        self.assertEquals(response.json, dict(success=True))


if __name__ == '__main__':
    unittest.main()
    