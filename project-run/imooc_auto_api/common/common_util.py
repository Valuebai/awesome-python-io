#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@IDE    ：PyCharm
@Author ：Valuebai
@Date   ：2020/2/2 22:12
@Desc   ：
=================================================='''
import json
import operator


class CommonUtil:

    def is_contain(self, str_one, str_two):
        """
        判断一个字符串是否在另外一个字符串中
        :param str_one:查找的字符串
        :param str_two:被查找的字符串
        :return:
        """
        if str_one in str_two:
            flag = True
        else:
            flag = False
        return flag

    def is_equal_dict(self, dict_one, dict_two):
        if isinstance(dict_one, str):
            dict_one = json.loads(dict_one)
        if isinstance(dict_two, str):
            dict_two = json.loads(dict_two)
        return operator.eq(dict_one, dict_two)


if __name__ == "__main__":
    pass
