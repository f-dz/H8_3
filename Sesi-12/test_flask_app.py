from turtle import home
import app
import unittest

class MyTestCase(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def test_home(self):
        result = self.app.get('/')
        self.assertEqual(result, '/', "Should run")