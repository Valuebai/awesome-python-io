#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@IDE    ：PyCharm
@Author ：LuckyHuibo
@Date   ：2019/8/30 16:51
@Desc   ：
=================================================='''
import os
import yaml


def _get_yaml():
    """
    解析yaml
    :return: s  字典
    """
    # 这里填下同一文件夹下的.yaml文件
    path = os.path.join(os.path.dirname(__file__) + '/ticket_config.yaml')
    try:  # 兼容2和3版本
        with open(path, encoding="utf-8") as f:
            s = yaml.load(f, Loader=yaml.FullLoader)
    except Exception:
        with open(path) as f:
            s = yaml.load(f, Loader=yaml.FullLoader)
    return s.decode() if isinstance(s, bytes) else s


if __name__ == "__main__":
    print(_get_yaml())
