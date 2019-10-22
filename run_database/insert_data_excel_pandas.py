#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@IDE    ：PyCharm
@Author ：LuckyHuibo
@Date   ：2019/8/9 21:05
@Desc   ：
一、用pymysql进行数据库的连接，库的删除创建，表的删除创建
二、用pandas读取
=================================================='''

import pymysql
import pandas as pd
import pysnooper


# cur 是数据库的游标链接，path 是 excel 文件的路径
def importExcelToMysql_pandas(cur, path):
    # pandas版本
    # 读取excel文件

    df = pd.read_excel(path)
    print(df)

    for i in range(len(df)):
        sqlstr = []
        for j in range(len(df) + 1):
            sqlstr.append(df.values[i][j])
            # print('打印获取的excel每一个值',df.values[i][j])
            # print('打印待插库的数据',sqlstr)
        # 读取每一行的数据，示例的student只有3列，需要根据你的表字段类似和数据进行添加
        valuestr = [str(sqlstr[0]), int(sqlstr[1]), int(sqlstr[2]), int(sqlstr[3])]

        # 将每行数据存到数据库中
        insert_dml_sql = "insert into student(姓名, 语文, 数学, 英语) values(%s, %s, %s, %s)"
        cur.execute(insert_dml_sql, valuestr)


# 输出读取数据库中内容
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
    importExcelToMysql_pandas(cur, "student.xlsx")
    readTable(cur)

    # 关闭游标链接
    cur.close()
    conn.commit()
    # 关闭数据库服务器连接，释放内存
    conn.close()
