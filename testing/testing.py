import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to My Website', response.data)

    def test_messages_page(self):
        response = self.app.get('/messages')
        self.assertEqual(response.status_code, 200)

    def test_form_submission(self):
        response = self.app.post('/form', data=dict(
            name='Test User',
            email='test@example.com',
            message='This is a test message'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Message sent successfully', response.data)
