#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@IDE    ：PyCharm
@Author ：LuckyHuibo
@Date   ：2019/8/9 21:05
@Desc   ：
一、用pymysql进行数据库的连接，库的删除创建，表的删除创建
二、用xlrd读取

##修改位置1-表
##修改位置2字段的数据类型

# xlrd 为 python 中读取 excel 的库，支持.xls 和 .xlsx 文件
=================================================='''

import pymysql
import xlrd
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
        # 读取每一行的数据，示例的student只有4列，需要根据你的表字段类似和数据进行添加
        valuestr = [int(sqlstr[0]), str(sqlstr[1]), str(sqlstr[2]), str(sqlstr[3])]  ##修改位置2字段的数据类型

        # 将每行数据存到数据库中   ##修改位置1-表
        insert_dml_sql = "insert into qa_user_illegal(id,user_id, object_id, morph_label) values(%s, %s, %s, %s)"
        cur.execute(insert_dml_sql, valuestr)


# 输出数据库中内容
def readTable(cursor):
    # 选择全部
    cursor.execute("select * from qa_user_illegal")  ##修改位置1-表
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

    # 新建一个database，已存在的话可以注释掉的
    # cur.execute("drop database if exists students")
    # cur.execute("create database students")
    # 选择 students 这个数据库
    cur.execute("use students")

    # sql中的内容为创建一个名为student的表   ##修改位置1-表
    sql = """
    # 新增问答用户违规表
CREATE TABLE IF NOT EXISTS `qa_user_illegal` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `user_id` int(11) unsigned NOT NULL COMMENT '用户ID',
  `object_id` int(11) unsigned NOT NULL COMMENT '违规ID',
  `morph_label` varchar(20) NOT NULL DEFAULT '' COMMENT '多态标记',
  `created` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`object_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='问答用户违规表';
    """
    # 如果存在student这个表则删除
    cur.execute("drop table if exists qa_user_illegal")  ##修改位置1-表
    # 创建表
    cur.execute(sql)

    # 将 excel 中的数据导入 数据库中
    importExcelToMysql_xlrd(cur, "qa_user_data.xlsx")
    readTable(cur)

    # 关闭游标链接
    cur.close()
    conn.commit()
    # 关闭数据库服务器连接，释放内存
    conn.close()
