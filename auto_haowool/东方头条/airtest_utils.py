#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@IDE    ：PyCharm
@Author ：LuckyHuibo
@Date   ：2019/10/22 11:13
@Desc   ：
=================================================='''
from airtest.core.api import *


def back_keyevent():
    """
    按【返回键】
    :return:
    """
    keyevent('BACK')


def home_keyevent():
    keyevent("HOME")
