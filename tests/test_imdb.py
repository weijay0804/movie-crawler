"""
Author: weijay
Date: 2022-12-11 18:12:09
LastEditors: weijay
LastEditTime: 2022-12-12 17:27:02
Description: 對 IMDB module 的單元測試
"""

import unittest
from unittest.mock import patch

from movie_crawler import IMDB


class Top250Resp:
    """模擬 top 250 html"""

    FAKE_HTML = """
        <table>
            <tbody class="lister-list">
                <tr>
                    <td class="posterColumn">
                        <span name="rk"></span>
                    </td>
                    <td class="titleColumn">
                        <a href="/title/tt0111161/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=1a264172-ae11-42e4-8ef7-7fed1973bb8f&pf_rd_r=5NM1QC3XKRNH5145B25J&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_1">刺激1995</a>
                    </td>
                </tr>
                <tr>
                    <td class="posterColumn">
                        <span name="rk"></span>
                    </td>
                    <td class="titleColumn">
                        <a href="/title/tt0111160/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=1a264172-ae11-42e4-8ef7-7fed1973bb8f&pf_rd_r=5NM1QC3XKRNH5145B25J&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_1">測試1</a>
                    </td>
                </tr>
                <tr>
                    <td class="posterColumn">
                        <span name="rk"></span>
                    </td>
                    <td class="titleColumn">
                        <a href="/title/tt0111159/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=1a264172-ae11-42e4-8ef7-7fed1973bb8f&pf_rd_r=5NM1QC3XKRNH5145B25J&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_1">測試2</a>
                    </td>
                </tr>
            </tbody>
        </table>
        """


class IMDBTest(unittest.TestCase):
    def setUp(self) -> None:
        self.imdb = IMDB("https://www.imdb.com")

    def test_get_top_250_function(self):

        top250_resp = Top250Resp()
        top250_resp.text = Top250Resp.FAKE_HTML
        top250_resp.status_code = 200
        self.patcher = patch("requests.get", return_value=top250_resp)
        self.patcher.start()

        movie_data = self.imdb.get_top_250()

        self.patcher.stop()

        self.assertEqual(
            movie_data,
            [
                {"id": "tt0111161", "title": "刺激1995"},
                {"id": "tt0111160", "title": "測試1"},
                {"id": "tt0111159", "title": "測試2"},
            ],
        )
