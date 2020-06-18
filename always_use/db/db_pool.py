#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2020/6/8 16:40
# @Software: PyCharm
# @Author  : https://github.com/Valuebai/
"""
    <mysql>.$ {数据库连接池}
    ~~~~~~~~~~~~~~~
    用pymysql + DBUtils.PooledDB 数据库连接池来实现
"""
import pymysql
from DBUtils.PooledDB import PooledDB
from always_use.db.db_config import *

POOL = PooledDB(
    creator=pymysql,  # 使用链接数据库的模块
    maxconnections=6,  # 连接池允许的最大连接数，0和None表示不限制连接数
    mincached=2,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
    maxcached=5,  # 链接池中最多闲置的链接，0和None不限制
    maxshared=3,
    # 链接池中最多共享的链接数量，0和None表示全部共享。PS: 无用，因为pymysql和MySQLdb等模块的 threadsafety都为1，所有值无论设置为多少，
    # _maxcached永远为0，所以永远是所有链接都共享。
    blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
    maxusage=None,  # 一个链接最多被重复使用的次数，None表示无限制
    setsession=[],  # 开始会话前执行的命令列表。如：["set datestyle to ...", "set time zone ..."]
    ping=0,
    # ping MySQL服务端，检查是否服务可用。# 如：0 = None = never, 1 = default = whenever it is requested,
    # 2 = when a cursor iscreated, 4 = when a query is executed, 7 = always
    host=db_mysql_host,
    port=db_mysql_port,
    user=db_mysql_user,
    password=db_mysql_password,
    database=db_mysql_database,
    charset=db_mysql_charset,
    autocommit='True'
)


class MySQLHelper(object):
    """
    实现方式1，实例化调用 MySQLHelper().insert
    """

    def __init__(self):
        self.conn = POOL.connection()
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)

    def closed_db(self):
        """
        关闭数据库cursor连接
        """
        self.cursor.close()
        self.conn.close()

    def fetch_one(self, sql, args=None):
        """
        查询获取一条数据
        """
        if not sql:
            print('传入的sql为空，请检查sql')
            return None
        res_one = None
        try:
            self.cursor.execute(sql, args)
            res_one = self.cursor.fetchone()
        except Exception as e:
            print("查询一条数据报错:{}".format(e))
        finally:
            self.closed_db()
        return res_one

    def fetch_all(self, sql, args=None):
        """
        查询获取全部数据
        """
        if not sql:
            print('传入的sql为空，请检查sql')
            return None
        res_all = None
        try:
            self.cursor.execute(sql, args)
            res_all = self.cursor.fetchall()
        except Exception as e:
            print("MySQL查询多条数据报错:{}".format(e))
        finally:
            self.closed_db()
        return res_all

    def execute(self, sql, args=None):
        """
        执行sql
        """
        if not sql:
            print('传入的sql为空，请检查sql')
            return None
        try:
            self.cursor.execute(sql, args)
        except BaseException as e:
            print("MySQL执行语句报错:{}".format(e))
        finally:
            self.closed_db()

    def insert(self, sql, args=None):
        """
        插入一条数据
        """
        if not sql:
            print('传入的sql为空，请检查sql')
            return None
        try:
            self.cursor.execute(sql, args)
            self.conn.commit()
            _id = self.cursor.lastrowid
            # 防止表中没有id返回0
            if _id == 0:
                return True
            return _id
        except Exception as e:
            print("MySQL插入数据报错:{}".format(e))
            self.conn.rollback()
            return False
        finally:
            self.closed_db()

    def delete(self, sql, args=None):
        """
        删除数据
        """
        if not sql:
            print('传入的sql为空，请检查sql')
            return None
        try:
            self.cursor.execute(sql, args)
            self.conn.commit()
        except Exception as e:
            print("MySQL删除数据报错:{}".format(e))
            self.conn.rollback()
        finally:
            self.closed_db()

    def update(self, sql, args=None):
        """
        更新数据
        """
        if not sql:
            print('传入的sql为空，请检查sql')
            return None
        try:
            self.cursor.execute(sql, args)
            self.conn.commit()
        except Exception as e:
            print("MySQL更新数据报错:{}".format(e))
            self.conn.rollback()
        finally:
            self.closed_db()


if __name__ == "__main__":
    print(MySQLHelper().fetch_one(sql="SELECT * FROM test;"))
    print(MySQLHelper().fetch_all(sql="SELECT * FROM test;"))

    sql_insert_cmd1 = """
    insert into matrix_startup(tag, machine, cpu_app, mem, mem_free, application_create, application_create_scene,
                               first_activity_create, startup_duration, is_warm_start_up, phone_time)
    values ('Trace_StartUp', 'BEST', '0.18021196474419685', 1938931712, 551144, 2892, 100, 10926, 10926, 'false',
            '1591161138851');
        """
    print(MySQLHelper().insert(sql=sql_insert_cmd1))
    print(MySQLHelper().fetch_all(sql="SELECT * FROM matrix_startup"))
