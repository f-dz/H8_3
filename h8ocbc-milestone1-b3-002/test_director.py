from config import app
from app import connex_app
import unittest
import json

class MyTestCase(unittest.TestCase):

    def setUp(self):
        connex_app.testing = True
        self.app = app.test_client()


    async def test_get_id_success(self):
        response = await self.app.get('/api/director/4762')
        self.assertIn(b"James Cameron", response.data)


    async def test_get_id_failed(self):
        response = await self.app.get('/api/director/4762')
        self.assertNotIn(b"Gore Verbinski", response.data)


    # Status code 409 ketika id sudah ada di data lain
    async def test_post_failed1(self):
        mock_request_data = {
            "name": "Tom Tom",
            "id": 4836,
            "gender": 2,
            "uid": 99999,
            "department": "Directing"
        }
        response = await self.app.post('/api/director/', data=json.dumps(mock_request_data))
        self.assertEqual(response.status_code, 404)


    # Status code 409 ketika uid sudah ada di data lain
    async def test_post_failed2(self): 
        mock_request_data = {
            "name": "Tom Tom",
            "id": 99999,
            "gender": 2,
            "uid": 81850,
            "department": "Directing"
        }
        response = await self.app.post('/api/director/', data=json.dumps(mock_request_data))
        self.assertEqual(response.status_code, 409)


    # Status code 200 ketika berhasil post data 
    async def test_post_success(self):
        mock_request_data = {
            "name": "Tom Tom",
            "id": 99999,
            "gender": 2,
            "uid": 99999,
            "department": "Directing"
        }
        response = await self.app.post('/api/director/', data=json.dumps(mock_request_data))
        self.assertEqual(response.status_code, 200)
    