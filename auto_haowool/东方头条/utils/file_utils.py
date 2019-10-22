#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@IDE    ：PyCharm
@Author ：LuckyHuibo
@Date   ：2019/10/22 11:15
@Desc   ：
=================================================='''

import os
import csv

headers = ['nickname', 'msg', 'pub_time']


def del_files(path):
    """
    删除某个文件夹下的所有文件
    :param path:
    :return:
    """
    os.popen('adb shell rm -r %s*' % path)


def del_folder(path):
    """
    删除某个文件夹及下面的所有文件
    :param path:
    :return:
    """
    os.popen('adb shell rm -r %s' % path)


# 注意：使用adb没法排序文件，为了准确获取文件，下载文件之前，需要提前删除微信文件夹
def copy_last_pic_to_local(path, folder):
    """
     从移动端获取到最新的一个图片
    :param path: 手机上的文件目录
    :param folder:PC端文件保存的目录
    :return:
    """
    # 读取目录下的所有文件
    r = os.popen('adb shell ls %s' % path)
    # 读取命令行的输出到一个list
    infos = r.readlines()

    # 文件名称
    last_file_name = infos[0].strip('\r\n')

    print(path + last_file_name)
    print(folder)

    if not os.path.exists(folder):
        os.makedirs(folder)

    # 加上绝对路径，把文件复制到本地文件夹中
    os.popen('adb pull %s %s' % (path + last_file_name, folder))


def write_to_csv(first, format_values):
    """
    写入到csv文件中
    :return:
    """
    with open('firends_circle.csv', 'a', encoding='utf-8', newline='') as fp:
        # 1.创建一个dictwriter对象
        writer_dict = csv.DictWriter(fp, headers)

        # 2.手动写入标题
        if first:
            writer_dict.writeheader()
        else:
            # 3.写入数据
            writer_dict.writerows(format_values)
