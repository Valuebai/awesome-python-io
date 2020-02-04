#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@IDE    ：PyCharm
@Author ：Valuebai
@Date   ：2020/2/2 22:32
@Desc   ：
=================================================='''
import data_config
from util.operation_excel import OperateExcel
from util.operation_json import OperateJson
from util.connect_mysql import OperationMysql


class GetData:
    def __init__(self):
        self.operate_excel = OperateExcel()

    # 获取工作表的总行数（即用例数）
    def get_case_lines(self):
        return self.operate_excel.get_excel_nrows()

    # 2 url 获取工作表的url
    def get_url(self, row):
        url_col = data_config.get_url()
        url = self.operate_excel.get_cell_value(row, url_col)
        return url

    # 3 run 获取是否执行
    def get_is_run(self, row):
        flag = None
        col = int(data_config.get_run())
        run_model = self.operate_excel.get_cell_value(row, col)
        if run_model == 'yes':  # 这里以yes为字段，需要在excel中的“是否运行”填yes
            flag = True
        else:
            flag = False
        return flag

    # 4 request_way 获取请求方式
    def get_request_method(self, row):
        col = int(data_config.get_run_way())
        request_method = self.operate_excel.get_cell_value(row, col)
        return request_method

    # 5 header 判断是否携带header
    def is_header(self, row):
        col = int(data_config.get_header())
        header = self.operate_excel.get_cell_value(row, col)
        if header != '':
            return eval(header)  # ！！！！将取出来的str-dict
        else:
            return None

    # 6 case_depend判断是否有依赖
    def is_depend(self, row):
        col = int(data_config.get_case_depend())
        depend_case_id = self.operate_excel.get_cell_value(row, col)
        if depend_case_id == "":
            return None
        else:
            return depend_case_id

    # 7 data_depend获取依赖数据的key
    def get_depend_key(self, row):
        col = int(data_config.get_data_depend())
        depend_key = self.operate_excel.get_cell_value(row, col)
        if depend_key == "":
            return None
        else:
            return depend_key

    # 8 field_depend获取依赖数据
    def get_depend_field(self, row):
        col = int(data_config.get_field_depend())
        data = self.operate_excel.get_cell_value(row, col)
        if data == "":
            return None
        else:
            return data

    # 9 data获取请求数据
    def get_request_data(self, row):
        col = int(data_config.get_data())
        data = self.operate_excel.get_cell_value(row, col)  # 从excel中获得请求data数据
        # data = self.get_data_from_json(row)  # 从json中获得请求data数据
        if data == '':
            return None
        return data

    # 通过获取关键字拿到json data数据，如：op_json.get_json_data('shop')
    def get_data_from_json(self, tag):
        op_json = OperateJson()
        request_data = op_json.get_json_data(tag)
        return request_data

    # 10 expect获取预期结果
    def get_expect_data(self, row):
        col = int(data_config.get_expect())
        exp = self.operate_excel.get_cell_value(row, col)
        if exp == '':
            return None
        return exp

    # 11 result写入数据
    def write_result(self, row, value):
        col = int(data_config.get_result())
        self.operate_excel.write_excel_value(row, col, value)

    # 通过sql获取预期结果
    def get_expect_data_from_mysql(self, row):
        op_mysql = OperationMysql()
        sql = self.get_expect_data(row)
        res = op_mysql.search_one(sql)
        return res.decode('unicode-escape')
