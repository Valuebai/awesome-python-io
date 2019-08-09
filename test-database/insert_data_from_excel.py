#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@IDE    ：PyCharm
@Author ：LuckyHuibo
@Date   ：2019/8/9 20:58
@Desc   ：python 解析excel数据并插入数据库（可运行）
应业务要求需要不定期将一些excel数据导入到线上数据库
=================================================='''

import xlrd
from configparser import ConfigParser
import pymysql
import sys

try:
    book = xlrd.open_workbook("xxxxxx.xlsx")  # 文件名，把文件与py文件放在同一目录下
except:
    print("open excel file failed!")
try:
    sheet = book.sheet_by_name("工作表1")  # execl里面的worksheet1
except:
    print("locate worksheet in excel failed!")

    # 连接数据库
try:
    database = pymysql.connect(host="XXXXXXXXXX.mysql.rds.aliyuncs.com", user="xxxxxx_rw", passwd="xxxxxxxxxx",
                               db="xxxxxxxxx", charset='utf8')
except:
    print("could not connect to mysql server(XXXXXXXXXX.mysql.rds.aliyuncs.com)")

cursor = database.cursor()
select = "select count(id) from xxxxx"  # 获取表中xxxxx记录数
cursor.execute(select)  # 执行sql语句
line_count = cursor.fetchone()

# print(line_count[0])

for i in range(1, sheet.nrows):  # 第一行是标题名，对应表中的字段名所以应该从第二行开始，计算机以0开始计数，所以值是1
    intention_type = sheet.cell(i, 0).value  # 取第i行第0列
iphone = sheet.cell(i, 1).value  # 取第i行第1列，下面依次类推
addrs = sheet.cell(i, 2).value
intention_date = sheet.cell(i, 3).value
uname = sheet.cell(i, 4).value
ID_card = sheet.cell(i, 5).value
intention_car = sheet.cell(i, 6).value
comment = sheet.cell(i, 7).value
# create_time = now()
value = (uname, ID_card, iphone, addrs, intention_car, intention_type, intention_date, comment)
insert = "INSERT INTO dm_intention_pool(name,id_card_no,mobile,addr,model_code,type,intention_time,ext)VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
cursor.execute(insert, value)  # 执行sql语句

update = "UPDATE `xxxxx`  SET `create_time` =now(),`update_time` =now() where id > %s"
cursor.execute(update, line_count[0])  # 执行sql语句
database.commit()  # 提交

cursor.close()  # 关闭连接
database.close()  # 关闭数据
print("")
print("Done! ")

print("")
