#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@IDE    ：PyCharm
@Author ：Valuebai
@Date   ：2020/2/1 20:48
@Desc   ：
mock即模拟数据，当我们无法实际执行获得数据时可以使用mock方法，
模拟生成我们需要判别的数据，这里mock_test方法同样进行了封装
=================================================='''
# from mock import mock     # Python2.x还是单独的

from unittest import mock  # Python3.x中本身就自带了Mock库


# 注意，不要命名为mock_test，不然在pycharm中会当做单元测试的
def mock_ts(request_data, url, method, response_data):
    mock_method = mock.Mock(return_value=response_data)
    mock_res = mock_method(url, method, request_data)
    return mock_res
