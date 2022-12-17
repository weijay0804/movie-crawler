"""
Author: weijay
Date: 2022-12-11 18:19:23
LastEditors: weijay
LastEditTime: 2022-12-12 17:41:10
FilePath: /movie_crawler/movie_crawler/tmdb.py
Description: TMDB 電影模組
"""

import aiohttp

from .helper import RequestHelper


class TMDB:
    def __init__(self, root_url: str, api_key: str) -> None:

        self.root_url = root_url
        self.api_key = api_key

    def __tmdb_id_url(self, imdb_id: str) -> str:
        """取得 tmdb id api url

        Args:
            imdb_id (str): IMDB 電影 id

        Returns:
            str: tmdb id url
        """

        return f"{self.root_url}/movie/{imdb_id}/external_ids?api_key={self.api_key}"

    def get_tmdb_id(self, imdb_id: str) -> int:
        """取得 tmdb 電影 id

        Args:
            imdb_id (str): IMDB 電影 id

        Returns:
            int: TMDB 電影 id
        """

        url = self.__tmdb_id_url(imdb_id)

        response = RequestHelper.get(url)

        try:
            r = response.json()["id"]

        except Exception as e:
            raise e

        return r

    async def get_tmdb_id_async(
        self, session: aiohttp.ClientSession, imdb_id: str
    ) -> int:
        """使用非同步方式取得 tmdb 電影 id

        Args:
            session (aiohttp.ClientSession): ClientSession 實例
            imdb_id (str): IMDB 電影 id

        Returns:
            int: TMDB 電影 id
        """

        url = self.__tmdb_id_url(imdb_id)

        async with session.get(url, ssl=False) as response:

            data = await response.json()

            return data["id"]
