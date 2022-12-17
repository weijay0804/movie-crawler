"""
Author: weijay
Date: 2022-12-11 17:04:18
LastEditors: weijay
LastEditTime: 2022-12-11 17:19:45
Description: 跑單元測試
"""
import unittest

tests = unittest.TestLoader().discover("tests")
unittest.TextTestRunner(verbosity=2).run(tests)
