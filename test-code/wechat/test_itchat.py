#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@IDE    ：PyCharm
@Author ：LuckyHuibo
@Date   ：2019/7/4 11:46
@Desc   ：练习itchat用的
=================================================='''
import itchat

if __name__ == "__main__":
    itchat.auto_login()

    itchat.send('Hello, filehelper我的小号', toUserName='filehelper')
