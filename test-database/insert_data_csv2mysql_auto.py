#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@IDE    ：PyCharm
@Author ：LuckyHuibo
@Date   ：2019/8/23 12:18
@Desc   ：读取csv或者excel文件，并自动生成建表语句，然后将数据插入到数据库中

=================================================='''

import pymysql
import pandas as pd


# Set table type by DataFrame data type
def make_table_sql(df):
    # Get columns in df
    columns = df.columns.tolist()

    # Get data type list of each column
    types = df.ftypes

    # Init pattern list
    make_table = []

    for col in columns:
        # Set table type pattern
        if 'int' in types[col]:
            char = col + ' INT'
        elif 'float' in types[col]:
            char = col + ' FLOAT'
        elif 'object' in types[col]:
            char = col + ' TEXT'
        elif 'datetime' in types[col]:
            char = col + ' DATETIME'
        make_table.append(char)
    return ','.join(make_table)


# Input data from csv file to mysql database
def csv2mysql(db_name, table_name, df):
    # Create database if needed
    cursor.execute('CREATE DATABASE IF NOT EXISTS {}'.format(db_name))

    # connect to database
    conn.select_db(db_name)

    # Create table in database if needed
    cursor.execute('DROP TABLE IF EXISTS {}'.format(table_name))
    cursor.execute('CREATE TABLE {}({})'.format(table_name, make_table_sql(df)))
    print('CREATE TABLE {}({})'.format(table_name, make_table_sql(df)))

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

    # Input data to mysql
    print('Start Input.......')
    csv2mysql(db_name, table_name, df)
    print('End!')


if __name__ == '__main__':
    main()
