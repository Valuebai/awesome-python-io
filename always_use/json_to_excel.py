#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2020/9/6 1:08
# @Software: PyCharm
# @Author  : https://github.com/Valuebai/
"""
    json 数据存储到excel中
    ~~~~~~~~~~~~~~~

"""
import xlwt

json = [
    {
        "student_no": 1001,
        "name": "James",
        "score": 10,
        "class": "A-1",
        "rank": 1
    },
    {
        "student_no": 1002,
        "name": "Tome",
        "score": 91,
        "class": "A-1",
        "rank": 2
    },
    {
        "student_no": 1003,
        "name": "Jane",
        "score": 100,
        "class": "A-3",
        "rank": 3
    },
    {
        "student_no": 1004,
        "name": "Rone",
        "score": 50,
        "class": "A-3",
        "rank": 4
    },
    {
        "student_no": 1005,
        "name": "Bill",
        "score": 44,
        "class": "A-3",
        "rank": 5
    },
    {
        "student_no": 1006,
        "name": "Lily",
        "score": 81,
        "class": "A-2",
        "rank": 6
    }

]


def json_to_excel(json_data):
    """
    读取json数据并存到excel中
    json_data: 数据格式为：[{},{},{}]
    """
    json_file = json_data
    print(json_file)
    workbook = xlwt.Workbook()
    sheet1 = workbook.add_sheet('save_data')
    ll = list(json_file[0].keys())
    for i in range(0, len(ll)):
        sheet1.write(0, i, ll[i])
    for j in range(0, len(json_file)):
        m = 0
        ls = list(json_file[j].values())
        for k in ls:
            sheet1.write(j + 1, m, k)
            m += 1
    workbook.save('save_data.xls')


def main():
    """主函数"""
    print('test')
    json_to_excel(json)


if __name__ == "__main__":
    main()
