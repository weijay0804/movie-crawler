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
            dict: dict: 其中 key 為 IMDB Id，item 是電影名稱
        """

        movies = self.imdb.get_top_250()

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
