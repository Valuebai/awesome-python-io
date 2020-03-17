#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2020/2/10 23:42
# @Software: PyCharm
# @Author  : https://github.com/Valuebai/
"""
    ddt.test
    ~~~~~~~~~~~~~~~

    测试ddt模块

"""

import unittest
from ddt import ddt, data, unpack

@ddt
class MyTest(unittest.TestCase):

    @data((8, 6), (4, 0), (15, 6))
    @unpack
    def test_tuples(self, first, second):
        self.assertTrue(first > second)

    @data([30, 29], [40, 30], [5, 3])
    @unpack
    def test_list(self, first, second):
        self.assertTrue(first > second)


    @data({'first': 1, 'second': 3, 'third': 5},
          {'first': 4, 'second': 7, 'third': 8})
    @unpack
    def test_dicts(self, first, second, third):
        self.assertTrue(first < second < third)


if __name__ == '__main__':
    unittest.main(verbosity=2)