# pymysql.connect参数中，port传入的是整数！！！而不是字符串！！！
# 需要在本地创建ease_lite库，不然改为自己已经创建的库

import configparser
import pymysql
import mysql
from mysql import connector


def get_dbs():
    """
    获取config文件夹配置下的local_config.ini数据库配置
    :return: 返回获取到的数据库，以字典形式返回
    """
    # 实例化一个获取配置对象
    myconfig = configparser.ConfigParser()
    # 读取本地mysql配置文件
    myconfig.read('../config/dbs_local_config.ini')

    # 获取local_config.ini数据库配置的数据，存储到字典中
    dbs_local = {
        "host": myconfig.get("db_local", 'host'),
        "port": myconfig.get("db_local", 'port'),
        "user": myconfig.get("db_local", 'user'),
        "password": myconfig.get("db_local", 'password'),
        "database": myconfig.get("db_local", 'database'),
        "charset": myconfig.get("db_local", 'charset'),
        # "cursorclass": myconfig.get("db_local", 'cursorclass'),
        # 结束有没有逗号都是可以的
    }
    # 返回dbs_local的字典形式
    return dbs_local


if __name__ == '__main__':
    # 打印获取到的数据库
    print(get_dbs())
    a = get_dbs()
    # 打开数据库连接
    # pymysql的connect中的第一个参数必须是字符串，直接传入字典会报错的
    # 怎么将字典形式转化为字符串呢？？
    # 字符串转为字典：myDict = eval(myStr)
    # 字典转为字符串：myStr = str(myDict)

    # connect = pymysql.connect()

    conn = pymysql.connect(
        host=a["host"],
        port=int(a["port"]),  # port传入的是整数！！！而不是字符创！！！
        user=a["user"],
        passwd=a["password"],
        db=a["database"],
        charset=a["charset"]
    )

    # 得到一个可以执行SQL语句的光标对象
    cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示
    # 得到一个可以执行SQL语句并且将结果作为字典返回的游标
    # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 定义要执行的SQL语句
    sql = """
    CREATE TABLE USER1 (
    id INT auto_increment PRIMARY KEY ,
    name CHAR(10) NOT NULL UNIQUE,
    age TINYINT NOT NULL
    )ENGINE=innodb DEFAULT CHARSET=utf8;  #注意：charset='utf8' 不能写成utf-8
    """

    # 执行SQL语句
    cursor.execute(sql)

    # 关闭光标对象
    cursor.close()

    # 关闭数据库连接
    conn.close()
