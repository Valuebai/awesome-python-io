#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@IDE    ：PyCharm
@Author ：Valuebai
@Date   ：2020/2/2 21:03
@Desc   ：
=================================================='''
import xlrd
from xlutils.copy import copy


class OperateExcel:

    def __init__(self, file_name=None, sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = '../dataconfig/case1.xls'  # 如果未传递文件路径，默认读取
            self.sheet_id = 0  # 默认是选择excel里面的第一个sheet表
        self.data = self.get_excel_data()

    # 获取excel表的内容
    def get_excel_data(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]

        return tables

    # 获取工作表的总行数
    def get_excel_nrows(self):
        tables = self.data

        return tables.nrows

    # 获取工作表的总列数
    def get_excel_ncols(self):
        tables = self.data

        return tables.ncols

    # 获取一个单元格的内容
    def get_cell_value(self, row, col):
        row = int(row)
        col = int(col)
        return self.data.cell_value(row, col)

    # 写入数据到get_excel_data
    def write_excel_value(self, row, col, value):
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)  # 使用xlutils复制数据
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row, col, value)
        write_data.save(self.file_name)

    # 根据行号，找到该行的内容
    def get_excel_row_values(self, row):
        tables = self.data
        row_data = tables.row_values(row)

        return row_data

    # 获取某一列的内容
    def get_excel_cols_data(self, col_id=None):
        if col_id != None:
            cols = self.data.col_values(col_id)
        else:
            cols = self.data.col_values(0)

        return cols

    # 根据对应的case_id找对对应的行号
    def get_excel_row_num(self, case_id):
        num = 0
        cols_data = self.get_excel_cols_data()
        for i in cols_data:
            if case_id in i:
                return num
            num = num + 1

    # 根据对应的case_id找对对应行的内容
    def get_rows_data(self, case_id):
        row_num = self.get_excel_row_num(case_id)
        row_data = self.get_excel_row_values(row_num)

        return row_data


if __name__ == "__main__":
    op_xl = OperateExcel()

    print('总行数:', op_xl.get_excel_nrows())
    print('总列数:', op_xl.get_excel_ncols())
    print(op_xl.get_cell_value(1, 2))
    # 往表格的第16行，第1列写入数据100
    # op_xl.write_excel_value(15, 0, 100)
    print(op_xl.get_excel_row_values(11))
    print(op_xl.get_excel_cols_data(1))
    print(op_xl.get_excel_row_num('Imooc-5'))
    print(op_xl.get_rows_data('Imooc-5'))
    print(op_xl.get_rows_data('test1'))
