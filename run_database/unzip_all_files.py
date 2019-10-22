#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@IDE    ：PyCharm
@Author ：LuckyHuibo
@Date   ：2019/8/12 10:03
@Desc   ：批量解压压缩文件到指定路径，代码默认是zip，其他的需要添加下
=================================================='''

import zipfile
import os
import pysnooper

# 设置源文件路径，以及需要解压到的指定路径
input_file_a = r"C:\testdata"  # 填写 zip file 的路径
output_file_b = r"C:\testdata"  # 填写 解压的路径



def unzip_file(zip_file_name, destination_path):
    """
    # 将zip文件解压处理，并放到指定的文件夹里面去
    :param zip_file_name: 需要解压文件的名字
    :param destination_path: 解压后保存的路径
    :return:
    """
    archive = zipfile.ZipFile(zip_file_name, mode='r')
    for file in archive.namelist():
        archive.extract(file, destination_path)



def zipfile_name(file_dir):
    """
    定义解压函数，将指定的zip文件里面的内容解压到指定路径里面去。
    1.获取文件路径    2.返回路径下所有的.zip文件，list
    :param file_dir:
    :return:
    """
    # 读取文件夹下面的文件名.zip
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.zip':  # 读取带zip 文件
                L.append(os.path.join(root, file))
                print(L)
    return L


@pysnooper.snoop()
def main():
    # 获取文件路径下所有.zip文件
    fn = zipfile_name(input_file_a)
    # 用for 循环，解压所有zip文件
    for file in fn:
        unzip_file(file, output_file_b)


if __name__ == "__main__":
    main()
