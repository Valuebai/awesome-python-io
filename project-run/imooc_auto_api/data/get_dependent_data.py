#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@IDE    ：PyCharm
@Author ：Valuebai
@Date   ：2020/2/3 17:59
@Desc   ：

当我们要执行的某个case的相应数据依赖于前面某个case的返回数据时，我们需要对相应数据进行更新，
比如case12的相应数据request_data[数据依赖字段]的值应该更新于case11的返回数据response_data[依赖的返回字段] 。
那么我们就需要先执行case11拿到返回数据，再写入case12的相应数据

即我们通过依赖的caseId找到对应的行号，拿到整行的内容。
我们默认拿到列0的内容（即caseId）循环整列找到依赖的caseId在第几行，然后返回整行数据，即实现方法get_rows_data(case_id) 。
然后再去执行和更新，我们编写一个专门处理依赖数据的模块，同时，为了获取依赖数据，还需要对获取数据模块进行更新

=================================================='''
import json
from util.operation_excel import OperateExcel
from base.runmethod import RunMethod
from data.get_data import GetData
from jsonpath_rw import jsonpath, parse


class DependentData():
    def __init__(self, case_id):
        self.case_id = case_id
        self.opera_excel = OperateExcel()
        self.data = GetData()

    # 通过case_id获取对应行数据
    def get_case_line_data(self):
        rows_data = self.opera_excel.get_rows_data(self.case_id)

        return rows_data

    # 执行依赖测试，获取结果
    def run_dependent(self):
        row_num = self.opera_excel.get_excel_row_num(self.case_id)  # 获取case_id对应的行号
        request_data = self.data.is_header(row_num)  # 判断是否携带header
        # 获取用例的请求方式,url,
        method = self.data.get_request_method(row_num)
        url = self.data.get_url(row_num)
        res = RunMethod().run_main(method, url, request_data)

        return json.loads(res)

    # 根据依赖的key获取case依赖字段的相应后返回
    def get_data_from_key(self, row):
        depend_key = GetData().get_depend_key(row)
        print(depend_key)
        print(type(depend_key))
        response_data = self.run_dependent()
        print('222:',response_data)
        print(type(response_data))
        # json_exe = parse(depend_key)
        # madle = json_exe.find(response_data)
        #
        # return [math.value for math in madle][0]
        list = [item for item in response_data]
        return list[0].get(depend_key)


if __name__ == "__main__":
    order = {
        "data": {
            "_input_charset": "utf-8",
            "body": "慕课网订单-1710141907182334",
            "it_b_pay": "1d",
            "notify_url": "http://order.imooc.com/pay/notifyalipay",
            "out_trade_no": "1710141907182334",
            "partner": "2088002966755334",
            "payment_type": "1",
            "seller_id": "yangyan01@tcl.com",
            "service": "mobile.securitypay.pay",
            "sign": "kZBV53KuiUf5HIrVLBCcBpWDg%2FnzO%2BtyEnBqgVYwwBtDU66Xk8VQUTbVOqDjrNymCupkVhlI%2BkFZq1jOr8C554KsZ7Gk7orC9dDbQlpr%2BaMmdjO30JBgjqjj4mmM%2Flphy9Xwr0Xrv46uSkDKdlQqLDdGAOP7YwOM2dSLyUQX%2Bo4%3D",
            "sign_type": "RSA",
            "string": "_input_charset=utf-8&body=慕课网订单-1710141907182334&it_b_pay=1d&notify_url=http://order.imooc.com/pay/notifyalipay&out_trade_no=1710141907182334&partner=2088002966755334&payment_type=1&seller_id=yangyan01@tcl.com&service=mobile.securitypay.pay&subject=慕课网订单-1710141907182334&total_fee=299&sign=kZBV53KuiUf5HIrVLBCcBpWDg%2FnzO%2BtyEnBqgVYwwBtDU66Xk8VQUTbVOqDjrNymCupkVhlI%2BkFZq1jOr8C554KsZ7Gk7orC9dDbQlpr%2BaMmdjO30JBgjqjj4mmM%2Flphy9Xwr0Xrv46uSkDKdlQqLDdGAOP7YwOM2dSLyUQX%2Bo4%3D&sign_type=RSA",
            "subject": "慕课网订单-1710141907182334",
            "total_fee": 299
        },
        "errorCode": 1000,
        "errorDesc": "成功",
        "status": 1,
        "timestamp": 1507979239100
    }
    res = "data.out_trade_no"
    json_exe = parse(res)
    madle = json_exe.find(order)
    print(madle)
    print([math.value for math in madle][0])
