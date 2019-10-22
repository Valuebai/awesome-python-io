#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@IDE    ：PyCharm
@Author ：LuckyHuibo
@Date   ：2019/10/22 11:26
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


def perform_view_id_click(poco, id, *timeout):
    """
    模拟点击某个页面view
    :param poco:
    :param id:
    :return:
    """
    if timeout:
        poco(id).wait(timeout).click()
    else:
        poco(id).click()


def perform_view_text_click(poco, text):
    """
    :param poco:
    :param text:
    :return:
    """
    # 注意：按钮可能不能点击
    poco(text=text).wait_for_appearance()
    poco(text=text).click()


def perform_view_input(poco, id, text):
    """
    模拟输入内容到输入框
    :param poco:
    :param id:
    :param text:
    :return:
    """
    poco(id).wait_for_appearance()

    poco(id).set_text(text)