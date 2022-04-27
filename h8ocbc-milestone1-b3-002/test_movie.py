from config import app
from app import connex_app
import unittest
import json

class MyTestCase(unittest.TestCase):

    def setUp(self):
        connex_app.testing = True
        self.app = app.test_client()


    async def test_get_id_success(self):
        response = await self.app.get('/api/movie/43597')
        self.assertIn(b"Avatar", response.data)


    async def test_get_id_failed(self):
        response = await self.app.get('/api/movie/43598')
        self.assertNotIn(b"Avatar", response.data)


    # Status code 404 ketika id director tidak ditemukan
    async def test_post_failed1(self):
        mock_request_data = {
            "id": 1000,
            "original_title": "Untitle",
            "budget": 199999,
            "popularity": 11,
            "release_date": "2022-03-04",
            "revenue": 299999,
            "title": "Untitle",
            "vote_average": 6.2,
            "vote_count": 208,
            "overview": "This movie has no title",
            "tagline": "Just untitle movie",
            "uid": 1001,
            "director_id": 1111
        }
        response = await self.app.post('/api/movie/', data=json.dumps(mock_request_data))
        self.assertEqual(response.status_code, 404)


    # Status code 409 ketika id sudah ada di data lain
    async def test_post_failed2(self):
        mock_request_data = {
            "id": 43597,
            "original_title": "Untitle",
            "budget": 199999,
            "popularity": 11,
            "release_date": "2022-03-04",
            "revenue": 299999,
            "title": "Untitle",
            "vote_average": 6.2,
            "vote_count": 208,
            "overview": "This movie has no title",
            "tagline": "Just untitle movie",
            "uid": 999,
            "director_id": 4762
        }
        response = await self.app.post('/api/movie/', data=json.dumps(mock_request_data))
        self.assertEqual(response.status_code, 409)


    # Status code 409 ketika uid sudah ada di data lain
    async def test_post_failed3(self):
        mock_request_data = {
            "id": 99999,
            "original_title": "Untitle",
            "budget": 199999,
            "popularity": 11,
            "release_date": "2022-03-04",
            "revenue": 299999,
            "title": "Untitle",
            "vote_average": 6.2,
            "vote_count": 208,
            "overview": "This movie has no title",
            "tagline": "Just untitle movie",
            "uid": 44912,
            "director_id": 4762
        }
        response = await self.app.post('/api/movie/', data=json.dumps(mock_request_data))
        self.assertEqual(response.status_code, 409)


    # Status code 200 ketika berhasil post data 
    async def test_post_success(self):
        mock_request_data = {
            "id": 99999,
            "original_title": "Untitle",
            "budget": 199999,
            "popularity": 11,
            "release_date": "2022-03-04",
            "revenue": 299999,
            "title": "Untitle",
            "vote_average": 6.2,
            "vote_count": 208,
            "overview": "This movie has no title",
            "tagline": "Just untitle movie",
            "uid": 99999,
            "director_id": 4762
        }
        response = await self.app.post('/api/movie/', data=json.dumps(mock_request_data))
        self.assertEqual(response.status_code, 200)
    