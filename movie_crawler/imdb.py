"""
Author: weijay
Date: 2022-12-11 15:57:36
LastEditors: weijay
LastEditTime: 2022-12-12 16:38:02
FilePath: /movie_crawler/movie_crawler/imdb.py
Description: IMDB 電影模組
"""

import bs4

from .helper import RequestHelper, Bs4Helper


class IMDB:
    def __init__(self, root_url: str):

        self.root_url = root_url

    def __init_bs4(self, url: str) -> bs4.BeautifulSoup:
        """將 reponse.text 轉換成 BeautifulSoup 實例

        Args:
            url (str): 網站 url

        Returns:
            bs4.BeautifulSoup: BeautifulSoup 實例
        """

        response = RequestHelper.get(url)
        soup = Bs4Helper.parse_html(response.text)

        return soup

    def __parse_top_250(self, soup: bs4.BeautifulSoup) -> dict:
        """從 html 中解析出 movie id 和 movie title

        Args:
            soup (bs4.BeautifulSoup): BeautifulSoup 實例

        Returns:
            dict: 其中 key 為 IMDB Id，item 是電影名稱
        """

        r = {}

        movie_items = soup.find("tbody", class_="lister-list").find_all("tr")

        for movie_item in movie_items:
            title = movie_item.find("td", class_="titleColumn").find("a").text
            imdb_id = (
                movie_item.find("td", class_="titleColumn")
                .find("a")
                .get("href")
                .split("/")[2]
            )

            r[imdb_id] = title

        return r

    def get_top_250(self) -> dict:
        """取得 top 250 的電影 id 和名稱

        Returns:
            dict: 其中 key 為 IMDB Id，item 是電影名稱
        """

        url = self.root_url + "/chart/top/?ref_=nv_mv_250"

        soup = self.__init_bs4(url)

        r = self.__parse_top_250(soup)

        return r
