#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2020/6/22 16:23
# @Software: PyCharm
# @Author  : https://github.com/Valuebai/


import os


def get_files_by_suffix(path, suffix_name):
    """
    获取指定路径下所有带有.xxx后缀名的文件
    Args:
        path: 指定的文件夹路径，如 path='./input/'，后面要加/
        suffix_name: 固定格式，为 suffix_name=".apk"

    Returns: files of list

    """

    file_num = 0
    res = []
    # 遍历该文件夹
    # 默认先读取当前文件夹里面的文件，如果存在子文件夹，读完当前再遍历子文件夹里面的
    for root, dirs, files in os.walk(path):
        # print(files)
        for file in files:  # 遍历刚获得的文件名files
            filename, extension = os.path.splitext(file)  # 将文件名拆分为文件名与后缀
            if extension == suffix_name:  # 判断该后缀是否为.X文件
                file_num = file_num + 1  # 文件个数标记
                # print(file_num, os.path.join(root,filename)) #输出文件号以及对应的路径加文件名
                res.append(filename + suffix_name)  # ["a.x","b,x"]格式
                # res.append(root + filename + suffix_name)  # ["C:\\a.x"]格式
    return res


if __name__ == "__main__":
    print(get_files_by_suffix(r"D:\codeMidea\run_matrix\apkChecker\input", ".apk"))
