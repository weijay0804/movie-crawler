"""
Author: weijay
Date: 2022-12-11 15:59:21
LastEditors: weijay
LastEditTime: 2022-12-12 17:28:57
Description: 一些通用的模組
"""
import requests
from bs4 import BeautifulSoup


class RequestHelper:
    """封裝 requests"""

    def within_request(func):
        """使用裝飾器將每次檢查回傳狀態的動作封裝起來"""

        def wrap(*args, **kwargs):

            response = func(*args, **kwargs)

            if response.status_code != 200:
                raise RuntimeError("Status Code Error")

            return response

        return wrap

    @within_request
    @staticmethod
    def get(url, *args, **kwargs) -> requests.Response:
        """封裝 request.get()"""

        response = requests.get(url, *args, **kwargs)

        return response


class Bs4Helper:
    """封裝 BeautifulSoup"""

    @staticmethod
    def parse_html(html_text: str) -> BeautifulSoup:
        """封裝實例化 BeautifulSoup"""

        if not isinstance(html_text, str):
            raise TypeError("Type Must Be str")

        soup = BeautifulSoup(html_text, "html.parser")

        return soup
