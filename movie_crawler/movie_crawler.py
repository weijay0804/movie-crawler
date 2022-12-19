"""
Author: weijay
Date: 2022-12-17 17:27:50
LastEditors: weijay
LastEditTime: 2022-12-17 17:27:51
Description: movie crawler 主模組
"""

import asyncio
from typing import List, Iterable

import aiohttp

from .imdb import IMDB
from .tmdb import TMDB


class MovieCrawler:
    def __init__(self, tmdb_api_key: str):

        self.imdb = IMDB("https://www.imdb.com")
        self.tmdb = TMDB("https://api.themoviedb.org/3", tmdb_api_key)

    def get_imdb_top_250(self) -> dict:
        """取得 IMDB Top 250 電影資料

        Returns:
            dict: 其中 key 為 IMDB Id，item 是電影名稱
        """

        movies = self.imdb.get_top_250()

        return movies

    def get_imdb_popular(self) -> dict:
        """取得 IMDB Popular 電影資料

        Returns:
            dict: 其中 key 為 IMDB Id，item 是電影名稱
        """

        movies = self.imdb.get_popular()

        return movies

    async def get_tmdb_id(self, imdb_id_list: Iterable) -> List[tuple]:
        """使用非同步的方式取得 top 250 電影 id

        Args:
            imdb_id_list (Iterable): 有 IMDB Id 資訊的迭代物件

        Returns:
            List[tuple]: [(tmdb id, imdb id), ...]
        """

        async with aiohttp.ClientSession() as session:

            tasks = []

            for imdb_id in imdb_id_list:

                tasks.append(
                    asyncio.create_task(self.tmdb.get_tmdb_id_async(session, imdb_id))
                )

            r = await asyncio.gather(*tasks)

        return r

    async def get_movie_detail(self, tmdb_id_list: Iterable) -> List[dict]:
        """使用非同步的方式取得電影詳細資訊

        Args:
            tmdb_id_list (Iterable): 有 TMDB ID 資訊的可迭代物件

        Returns:
            List[dict]: [{movie_detail}, ....]
        """

        async with aiohttp.ClientSession() as session:

            tasks = []

            for tmdb_id in tmdb_id_list:

                tasks.append(
                    asyncio.create_task(self.tmdb.get_detail(session, tmdb_id))
                )

            r = await asyncio.gather(*tasks)

        return r
