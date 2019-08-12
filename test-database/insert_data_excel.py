#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@IDE    ：PyCharm
@Author ：LuckyHuibo
@Date   ：2019/8/9 21:05
@Desc   ：
一、用pymysql进行数据库的连接，库的删除创建，表的删除创建
二、用xlrd读取
=================================================='''

import pymysql
# xlrd 为 python 中读取 excel 的库，支持.xls 和 .xlsx 文件
import xlrd

# openpyxl 库支持 .xlsx 文件的读写
from openpyxl.reader.excel import load_workbook
from builtins import int


# cur 是数据库的游标链接，path 是 excel 文件的路径
def importExcelToMysql_xlrd(cur, path):
    ## xlrd版本
    ## 读取excel文件
    workbook = xlrd.open_workbook(path)
    sheets = workbook.sheet_names()
    print('sheets:', sheets)
    worksheet = workbook.sheet_by_name(sheets[0])
    print('worksheet:', worksheet)

    ## xlrd版本
    ## 将表中数据读到 sqlstr 数组中
    for i in range(1, worksheet.nrows):
        row = worksheet.row(i)

        sqlstr = []

        for j in range(0, worksheet.ncols):
            sqlstr.append(worksheet.cell_value(i, j))
        ###
        # 读取每一行的数据，示例的student只有3列，需要根据你的表字段类似和数据进行添加
        valuestr = [str(sqlstr[0]), int(sqlstr[1]), int(sqlstr[2]), int(sqlstr[3])]

        # 将每行数据存到数据库中
        insert_dml_sql = "insert into student(姓名, 语文, 数学, 英语) values(%s, %s, %s, %s)"
        cur.execute(insert_dml_sql, valuestr)


# cur 是数据库的游标链接，path 是 excel 文件的路径
def importExcelToMysql_openpyxl(cur, path):
    ### openpyxl版本
    # 读取excel文件
    workbook = load_workbook(path)
    # 获得所有工作表的名字
    sheets = workbook.get_sheet_names()
    # 获得第一张表
    worksheet = workbook.get_sheet_by_name(sheets[0])
    ###

    ### openpyxl版本
    # 将表中每一行数据读到 sqlstr 数组中
    for row in worksheet.rows:

        sqlstr = []

        for cell in row:
            sqlstr.append(cell.value)
        ###
        # 读取每一行的数据，示例的student只有3列，需要根据你的表字段类似和数据进行添加
        valuestr = [str(sqlstr[0]), int(sqlstr[1]), int(sqlstr[2]), int(sqlstr[3])]

        # 将每行数据存到数据库中
        insert_dml_sql = "insert into student(姓名, 语文, 数学, 英语) values(%s, %s, %s, %s)"
        cur.execute(insert_dml_sql, valuestr)


# 输出数据库中内容
def readTable(cursor):
    # 选择全部
    cursor.execute("select * from student")
    # 获得返回值，返回多条记录，若没有结果则返回()
    results = cursor.fetchall()

    for i in range(0, results.__len__()):
        for j in range(0, 4):
            print(results[i][j], end='\t')

        print('\n')


if __name__ == '__main__':
    # 和数据库建立连接
    conn = pymysql.connect('localhost', 'root', 'luhuibo123', charset='utf8')
    # 创建游标链接
    cur = conn.cursor()

    # 新建一个database
    cur.execute("drop database if exists students")
    cur.execute("create database students")
    # 选择 students 这个数据库
    cur.execute("use students")

    # sql中的内容为创建一个名为student的表
    sql = """CREATE TABLE IF NOT EXISTS `student` (
                `姓名` VARCHAR (20),
                `语文` INT,
                `数学` INT,
                `英语` INT
              )"""
    # 如果存在student这个表则删除
    cur.execute("drop table if exists student")
    # 创建表
    cur.execute(sql)

    # 将 excel 中的数据导入 数据库中
    # importExcelToMysql_xlrd(cur, "student.xlsx")
    importExcelToMysql_openpyxl(cur, "student.xlsx")
    readTable(cur)

    # 关闭游标链接
    cur.close()
    conn.commit()
    # 关闭数据库服务器连接，释放内存
    conn.close()
