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

from dotenv import load_dotenv

from movie_crawler import MovieCrawler


get_time = lambda : time.time()

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
    r = asyncio.run(mc.get_tmdb_id(imdb_movies.keys()))
    print(f"Done!, Take: {get_time() - start}")

    print(r)

    return

if __name__ == "__main__":
    get_250()
