'''
Author: weijay
Date: 2022-12-12 17:32:14
LastEditors: weijay
LastEditTime: 2022-12-12 17:43:58
FilePath: /movie_crawler/tests/test_tmdb.py
Description: 對 TMDB module 的單元測試
'''

import unittest
from unittest.mock import patch

from movie_crawler import TMDB

class FakeTMDBIdResp:
    
    FAKE_DATA = {"id" : 1, "imdbId": "tt20021", "fbToken" : "test"}

    def json(self):
        return FakeTMDBIdResp.FAKE_DATA

class TMDBTest(unittest.TestCase):

    def setUp(self) -> None:
        self.tmdb = TMDB("https://tmdb_test", "test_api_key")

    def test_get_tmdb_id(self):

        fake_resp = FakeTMDBIdResp()
        fake_resp.status_code = 200

        self.patcher = patch('requests.get', return_value = fake_resp)
        self.patcher.start()

        tmdb_id = self.tmdb.get_tmdb_id("tt20021")

        self.assertEqual(1, tmdb_id)

        self.patcher.stop()
