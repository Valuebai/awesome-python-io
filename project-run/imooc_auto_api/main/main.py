#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@IDE    ：PyCharm
@Author ：Valuebai
@Date   ：2020/2/3 19:31
@Desc   ：主函数
=================================================='''

import os, sys

# 解决在命令行窗口报错No module named 'base'，需要放在最前面
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from base.configHttp import RunMethod
from data.get_data import GetData
from data.get_dependent_data import DependentData
from common.common_util import CommonUtil
from common.logConf import logger


class Main():

    def __init__(self):
        self.run_method = RunMethod()
        self.get_data = GetData()
        self.common_util = CommonUtil()

    def run(self):
        result = None
        # 获取工作表的总行数（即用例数）
        rows = self.get_data.get_case_lines()
        print('获取工作表的总行数（即用例数）:', rows)

        # 读取测试用例excel表，第一行标题不读取
        for i in range(1, rows):
            # 检查用例的运行字段,True
            is_run = self.get_data.get_is_run(i)

            # 根据是否运行yes来执行用例
            if is_run:
                url = self.get_data.get_url(i)
                method = self.get_data.get_request_method(i)
                expect_data = self.get_data.get_expect_data(i)  # 获取期望值
                header = self.get_data.is_header(i)

                # 判断是否存在用例依赖
                depend_case = self.get_data.is_depend(i)
                if depend_case != None:
                    self.depend_data = DependentData(depend_case)
                    # 获取依赖相应数据
                    depend_response_data = self.depend_data.get_data_from_key(i)
                    # 获取依赖的key
                    depend_key = self.get_data.get_depend_field(i)
                    depend_response_data[depend_key] = depend_response_data

                # 用封装的requests请求
                result = self.run_method.run_main(method, url, expect_data, header)

                # !!!这里有个header的异常需要处理，用Imooc-11作为header依赖，会有报错，需要处理后提醒传入{}或者其他类型数据

                # 判断期望结果是否存在真实结果中
                if self.common_util.is_contain(expect_data, result):
                    self.get_data.write_result(i, 'pass')  # 测试通过
                    print('第%d个测试，结果pass' % i)
                else:
                    self.get_data.write_result(i, 'fail')  # 测试失败
                    print('第%d测试，结果fail' % i)


if __name__ == "__main__":
    logger.info('INFO日志打印...')
    result = Main().run()
    print(result)
