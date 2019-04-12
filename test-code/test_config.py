import configparser  # 导入模块

myconfig = configparser.ConfigParser()  # 创建对象
myconfig.read("../config/dbs_local_config.ini")  # 读取配置文件，如果配置文件不存在则创建

a = myconfig.get('db', 'db_port')
print(a)

# secs = myconfig.sections()  # 获取所有的节点名称
# print(secs)
