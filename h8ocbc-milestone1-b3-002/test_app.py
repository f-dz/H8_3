from config import app
from app import connex_app
import unittest
import json

class MyTestCase(unittest.TestCase):

    def setUp(self):
        connex_app.testing = True
        self.app = app.test_client()


    def test_home(self):
        response = self.app.get('/')
        self.assertIn(b"Data Movies and Directors", response.data)
        self.assertEqual(response.status_code, 200)


    async def test_swagger(self):
        response = await self._async_connection.get("/api/ui")
        self.assertIn(b"Swagger", response.data)
        self.assertEqual(response.status_code, 200)