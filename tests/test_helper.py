"""
Author: weijay
Date: 2022-12-11 16:55:16
LastEditors: weijay
LastEditTime: 2022-12-12 17:24:00
Description: 對 helper 模組的單元測試
"""

import unittest
from unittest.mock import patch

from movie_crawler.helper import RequestHelper, Bs4Helper


class FakeResp:
    pass


class RequestHeplerTest(unittest.TestCase):
    def test_get_function(self):

        fake_resp = FakeResp()
        fake_resp.status_code = 200
        fake_resp.text = "This is test reponse"
        self.patcher = patch("requests.get", return_value=fake_resp)
        self.patcher.start()

        url1 = "https://google.com"

        response1 = RequestHelper.get(url1)

        self.patcher.stop()

        self.assertTrue("Status Code Error" not in response1.text)

    def test_error_get_function(self):

        fake_resp = FakeResp()
        fake_resp.status_code = 404
        fake_resp.text = "This is test reponse"
        self.patcher = patch("requests.get", return_value=fake_resp)
        self.patcher.start()

        url2 = "https://google.com/test"

        with self.assertRaises(RuntimeError) as cm:
            RequestHelper.get(url2)

        self.patcher.stop()

        self.assertEqual(str(cm.exception), "Status Code Error")


class Bs4HelperTest(unittest.TestCase):
    def setUp(self) -> None:

        self.test_html = "<title>This is a test<title>"

    def test_parse_html_function(self):

        soup = Bs4Helper.parse_html(self.test_html)

        self.assertEqual(soup.title.text, "This is a test")
