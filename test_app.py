import os
import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_hello_default(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello, Student!', response.data)

    def test_hello_with_env(self):
        with app.test_client() as client:
            with app.app_context():
                os.environ['STUDENT_NAME'] = 'Test Student'
                response = client.get('/')
                self.assertIn(b'Test Student', response.data)

if __name__ == '__main__':
    unittest.main()
