import configparser


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
    dbs = {"db_port": myconfig.get("db", 'db_port'),
           "db_user": myconfig.get("db", 'db_user'),
           "db_host": myconfig.get("db", 'db_host'),
           "db_pass": myconfig.get("db", 'db_pass'),
           }
    return dbs


if __name__ == '__main__':
    print(get_dbs())
