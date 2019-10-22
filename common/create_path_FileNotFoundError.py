#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@IDE    ：PyCharm
@Author ：LuckyHuibo
@Date   ：2019/7/24 16:09
@Desc   ：常使用的方法是先创建文件夹，然后再创建文件。

使用python保存文件，要保存的路径中有多个文件夹，则需要先判断文件夹路径是否存在，再判断文件是否存在
====================代码示例
    work_rep_init_file_name = './scrip/00_work_rep_init_script.sql'
    with open(work_rep_init_file_name, 'w+') as f:
        f.read()

Traceback (most recent call last):
  File "C:/mycode/awesome-python-io/run_leetcode/run_Gragh_DFS_BFS.py", line 120, in <module>
    with open(work_rep_init_file_name, 'w+') as f:
FileNotFoundError: [Errno 2] No such file or directory: './scrip/00_work_rep_init_script.sql'
====================
=================================================='''

if __name__ == "__main__":
    # 先在网络上没有找到，所以自己动手写出来，如果各位大牛在某处找到类似的例子，请不要吐槽，谢谢！
    # 常使用的方法是先创建文件夹，然后再创建文件。
    import os

    # 先定义一个带路径的文件
    filename = "./home/mydir/test.txt"
    # 将文件路径分割出来
    file_dir = os.path.split(filename)[0]
    # 判断文件路径是否存在，如果不存在，则创建，此处是创建多级目录
    if not os.path.isdir(file_dir):
        os.makedirs(file_dir)
    # 然后再判断文件是否存在，如果不存在，则创建
    if not os.path.exists(filename):
        # os.system(r'touch %s' % filename)
        with open(filename, 'w') as f:
            f.write("hahaha")
