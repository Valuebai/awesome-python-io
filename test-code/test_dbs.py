# pymysql.connect参数中，port传入的是整数！！！而不是字符串！！！

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
