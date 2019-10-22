#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@IDE    ：PyCharm
@Author ：LuckyHuibo
@Date   ：2019/10/22 11:17
@Desc   ：
=================================================='''

import re
import random
import string


def filter_emoji(desstr, restr=''):
    """
    过滤特殊表情,只保留中文、英文、数字
    """

    # 一个网名为【......】的网友，随机生成为6位的字符
    if desstr == r'......':
        return make_random_string(6)

    cop = re.compile("[^\u4e00-\u9fa5^.^a-z^A-Z^0-9]")

    return cop.sub(restr, desstr)


def make_random_string(num):
    """
    生成随机字符串
    :param num:
    :return:
    """
    return ''.join(random.sample(string.ascii_letters + string.digits, num))
