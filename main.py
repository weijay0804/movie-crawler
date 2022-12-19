"""
Author: weijay
Date: 2022-12-10 23:17:55
LastEditors: weijay
LastEditTime: 2022-12-17 16:54:48
FilePath: /movie_crawler/main.py
Description: 
"""

import os
import time
import asyncio
from typing import Iterable, List

from dotenv import load_dotenv

from movie_crawler import MovieCrawler


get_time = lambda: time.time()
get_tmdb_id = lambda movie_list: [i["tmdbId"] for i in movie_list]


def get_250():
    """取得 top 250 電影資訊"""

    load_dotenv()
    api_token = os.environ.get("TMDB_API_KEY")

    mc = MovieCrawler(api_token)

    start = get_time()
    print("Fetch IMDB Data ....")
    imdb_movies = mc.get_imdb_top_250()
    print(f"Done!, Take: {get_time() - start}")

    start = get_time()
    print("Fetch TMDB Data ....")
    data = asyncio.run(mc.get_tmdb_id(imdb_movies.keys()))
    print(f"Done!, Take: {get_time() - start}")

    r = []

    for d in data:
        r.append({"imdbId": d[1], "tmdbId": d[0], "title": imdb_movies[d[1]]})

    return r


def get_popular():
    """取得 popular 電影資訊"""

    load_dotenv()
    api_token = os.environ.get("TMDB_API_KEY")

    mc = MovieCrawler(api_token)

    start = get_time()
    print("Fetch IMDB Data ....")
    imdb_movies = mc.get_imdb_popular()
    print(f"Done!, Take: {get_time() - start}")

    start = get_time()
    print("Fetch TMDB Data ....")
    data = asyncio.run(mc.get_tmdb_id(imdb_movies.keys()))
    print(f"Done!, Take: {get_time() - start}")

    r = []

    for d in data:
        r.append({"imdbId": d[1], "tmdbId": d[0], "title": imdb_movies[d[1]]})

    return r


def get_detail(tmdb_id_list: Iterable) -> List[dict]:
    """取得電影詳細資訊

    Args:
        tmdb_id_list (Iterable): 有 TMDB ID 資訊的可迭代物件

    Returns:
        List[dict]: [{movie_detail}, ....]
    """

    load_dotenv()
    api_token = os.environ.get("TMDB_API_KEY")

    mc = MovieCrawler(api_token)

    start = get_time()
    print("Fetch Movie Detail .....")
    movie_detail = asyncio.run(mc.get_movie_detail(tmdb_id_list))
    print(f"Done!, Take: {get_time() - start} s")

    return movie_detail


if __name__ == "__main__":
    get_250()
    get_popular()
