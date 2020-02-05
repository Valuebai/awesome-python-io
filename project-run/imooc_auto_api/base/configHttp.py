#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@IDE    ：PyCharm
@Author ：Valuebai
@Date   ：2020/2/1 18:21
@Desc   ：封装requests请求get和post
使用from runmethod import RunMethod 来实例化对象进行使用



# 不同：get用于获取数据，post用于修改数据

两者传递参数的方式也有不一样
- get是直接在url里通过?来连接参数
- post则是把数据放在HTTP的包体内(request body)

# 相同：两者的本质就是TCP链接，并无差别
=================================================='''
import requests
import json


# from common.logConf import logger


class RunMethod:

    # 定义requests的post函数
    def send_post(self, url, data, header=None):
        res = None
        if header != None:
            res = requests.post(url=url, data=data, headers=header)
        else:
            res = requests.post(url=url, data=data)
        return res.json()

    # 定义requests的get函数
    def send_get(self, url, data=None, header=None):
        res = None
        if header != None:
            res = requests.get(url=url, data=data, headers=header, verify=False)  # 忽略对 SSL 证书的验证
        else:
            res = requests.get(url=url, data=data, verify=False)  # 忽略对 SSL 证书的验证
        return res.json()

    # 封装requests执行主函数
    def run_main(self, method, url, data=None, header=None):
        res = None
        method = method.upper()  # 将请求方式转为大写，防止写错为get

        if method == 'POST':
            res = self.send_post(url, data, header)
        elif method == 'GET':
            res = self.send_get(url, data, header)
        else:
            print('您输入的method不对，只能处理GET和POST的')
        return json.dumps(res, ensure_ascii=False)


if __name__ == "__main__":
    # logger.info('INFO日志打印...')
    test = RunMethod()
    test = RunMethod()
    url = 'http://httpbin.org/post'
    data = {'key': 'value'}
    result = test.run_main('POST', url, data=data)
    print('POST:', result)
    print('GET:', test.run_main('GET', 'http://httpbin.org/get'))

