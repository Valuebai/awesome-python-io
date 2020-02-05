#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@IDE    ：PyCharm
@Author ：Valuebai
@Date   ：2020/2/1 20:23
@Desc   ：

使用unittest来组织测试、添加测试用例和断言，
测试报告可以下载HTMLTestRunner.py并放在python安装路径lib下即可
=================================================='''
import json
import unittest
import HTMLTestRunner

from configHttp import RunMethod
from mock_demo import mock_run
from datetime import datetime


class TestMethod(unittest.TestCase):

    def setUp(self):
        print('用例执开始前执行')
        # self.run = RunMain()

    # 使用requests的post请求，断言成功
    # @unittest.skip('test_01')
    def test_01(self):
        url = 'http://httpbin.org/post'
        data = {'key': 'value'}
        go = RunMethod()
        res = go.run_main(method='POST', url=url, data=data)  # 返回的是json格式
        res = json.loads(res)  # 需要将json解码为字典
        print('test_01:', type(res))
        print('url is:', res['url'])

        self.assertEqual(res['url'], "http://httpbin.org/post")

    # 忽略不执行
    # @unittest.skip('test_02')
    def test_02(self):
        url = 'http://coding.imooc.com/api/cate'
        data = {
            'timestamp': '1507034803124',
            'uid': '5249191',
            'uuid': '5ae7d1a22c82fb89c78f603420870ad7',
            'secrect': '078474b41dd37ddd5efeb04aa591ec12',
            'token': '7d6f14f21ec96d755de41e6c076758dd',
            'cid': '0',
            'errorCode': 1001
        }
        go = RunMethod()
        res = go.run_main('GET', url, data)
        res = json.loads(res)
        self.assertEqual(res['errorCode'], 1006, "测试失败")

    # 使用mock进行测试，断言成功
    # @unittest.skip('test_03')
    def test_03(self):
        url = 'http://coding.imooc.com/api/cate'
        data = {
            'timestamp': '1507034803124',
            'uid': '5249191',
            'uuid': '5ae7d1a22c82fb89c78f603420870ad7',
            'secrect': '078474b41dd37ddd5efeb04aa591ec12',
            'token': '7d6f14f21ec96d755de41e6c076758dd',
            'cid': '0',
            'errorCode': 1001
        }

        res = mock_run(data, url, 'POST', data)
        print('test_03:', res)
        print(type(res['errorCode']), ' and ', res['errorCode'])
        self.assertEqual(res['errorCode'], 1001, "测试成功")

    def tearDown(self):
        print('用例执行后才执行')


if __name__ == "__main__":
    # #使用TestSuite则将此句屏蔽掉
    # unittest.main() #按照test开头默认执行属性按0-9，A-Z，a-z 执行，可使用TestSuite类的addTest方法改变执行顺序

    my_test_suite = unittest.TestSuite()
    my_test_suite.addTest(TestMethod('test_01'))
    my_test_suite.addTest(TestMethod('test_02'))
    my_test_suite.addTest(TestMethod('test_03'))

    now = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    file_path = '../output/' + 'report/' + now + '.html'
    fp = open(file_path, 'wb+')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='我的自动化测试报告',
        description='This demonstrates the report output by HTMLTestRunner.'
    )
    runner.run(my_test_suite)
