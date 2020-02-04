#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@IDE    ：PyCharm
@Author ：Valuebai
@Date   ：2020/2/2 18:08
@Desc   ：
=================================================='''
import json


class OperateJson:

    def __init__(self, file_path=None):
        if file_path == None:
            self.file_path = '../dataconfig/user.json'  # 设置默认json文件路径
        else:
            self.file_path = file_path
        self.data = self.read_json_data()

    # 读取json文件
    def read_json_data(self, json_fpath=None):
        if json_fpath == None:
            json_fpath = self.file_path
        with open(json_fpath) as fp:
            json_data = json.load(fp)
            return json_data

    # 获取json数据，根据关键字
    def get_json_data(self, tag):
        print(type(self.data))
        return self.data[tag]  # 需要先用read_json_data得到数据

    # 写入json数据
    def write_json_data(self, data, json_fpath=None):
        if json_fpath == None:
            json_fpath = '../dataconfig/cookie.json'  # 设置默认json文件路径
        with open(json_fpath, 'w')as fp:
            fp.write(json.dumps(data))


if __name__ == "__main__":
    op_json = OperateJson()
    print(op_json.get_json_data('shop'))
