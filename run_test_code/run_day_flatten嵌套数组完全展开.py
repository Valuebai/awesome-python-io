#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@IDE    ：PyCharm
@Author ：Valuebai
@Date   ：2019/11/20 7:47
@Desc   ：
例子卡片7：嵌套数组完全展开

对于如下数组：

[[[1,2,3],[4,5]]]
如何完全展开成一维的。这个小例子实现的flatten是递归版，
两个参数分别表示带展开的数组，输出数组。
=================================================='''
from collections import *


# 返回list
def flatten(input_arr, output_arr=None):
    if output_arr is None:
        output_arr = []
    for ele in input_arr:
        if isinstance(ele, Iterable):  # 判断ele是否可迭代
            flatten(ele, output_arr)  # 尾数递归
        else:
            output_arr.append(ele)  # 产生结果
    return output_arr


if __name__ == "__main__":
    print(flatten([[1, 2, 3], [4, 5]]))
    print(flatten([[1, 2, 3], [4, 5], [6, 7]]))
    print(flatten([[1, 2, 3], [4, 5, 6]]))
    print('-' * 20)
    # 跟numpy的flatten进行比较
    import numpy

    b = numpy.array([[1, 2, 3], [4, 5]])
    b.flatten()

    print(b.flatten())
    print(type(b))
