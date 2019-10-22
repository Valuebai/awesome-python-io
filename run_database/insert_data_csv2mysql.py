#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@IDE    ：PyCharm
@Author ：LuckyHuibo
@Date   ：2019/8/23 12:18
@Desc   ：读取csv或者excel文件，需要手动复制建表sql和调整数据(数据按照table格式填写)

=================================================='''

import pymysql
import pandas as pd


# Input data from csv file to mysql database
def csv2mysql(db_name, table_name, df, create_sql):
    # Create database if needed
    cursor.execute('CREATE DATABASE IF NOT EXISTS {}'.format(db_name))

    # connect to database
    conn.select_db(db_name)

    # Create table in database if needed
    cursor.execute('DROP TABLE IF EXISTS {}'.format(table_name))
    cursor.execute(create_sql)

    # Change timestamp type to string if needed
    # df['time'] = df['time'].astype('str')

    # Get df values
    values = df.values.tolist()

    # Get columns number
    s = ','.join(['%s' for _ in range(len(df.columns))])

    # executemany insert data
    cursor.executemany('INSERT INTO {} VALUES ({})'.format(table_name, s), values)


def main():
    # Set configuration
    config = {'host': 'localhost', 'user': 'root', 'password': 'luhuibo123',
              'port': 3306, 'charset': 'utf8'}

    # Init connection
    global conn
    conn = pymysql.Connect(**config)

    # Confirm commit True
    conn.autocommit(1)

    # Init cursor
    global cursor
    cursor = conn.cursor()

    # Set input file path
    file_path = 'student.xlsx'

    # Load file to df
    df = pd.read_excel(file_path)

    # Init database name
    db_name = 'testABC'

    # Init table name
    table_name = 'student'

    # Init table crete sql
    create_sql = """CREATE TABLE IF NOT EXISTS `student` (
                `姓名` VARCHAR (20),
                `语文` INT,
                `数学` INT,
                `英语` INT
              )"""

    # Input data to mysql
    print('Start Input.......')
    csv2mysql(db_name, table_name, df, create_sql)
    print('End!')


if __name__ == '__main__':
    main()
