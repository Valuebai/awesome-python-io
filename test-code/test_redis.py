# 第一步，在windows本地安装redis
# pip install redis包

# import redis   # 导入redis模块，通过python操作redis 也可以直接在redis主机的服务端操作缓存数据库
#
# r = redis.Redis(host='localhost', port=6379, decode_responses=True)   # host是redis主机，需要redis服务端和客户端都启动 redis默认端口是6379
# r.set('name', 'junxi')  # key是"foo" value是"bar" 将键值对存入redis缓存
# print(r['name'])
# print(r.get('name'))  # 取出键name对应的值
# print(type(r.get('name')))


import redis

pool = redis.ConnectionPool(host='127.0.0.1',port=6379)
r = redis.Redis(connection_pool=pool)
class Redis_login():
    def __init__(self,user,pwd):
        # user = input('请输入用户名\n')
        # pwd = input('请输入密码\n')
        r.mset(user1='123',user2='1234',user3='12345')
    def login(self):
        ls = []
        for key in r.keys():
            ls.append(key.decode('utf-8'))
        if user not in ls:
            print('用户名错误请重新输入')
        elif r.get(user).decode('utf-8') == pwd:
            print('登录成功！！！')
        else:
            red.not_login()
    def not_login(self):
        print('输入错误请重新输入')

if __name__ == '__main__':
    while True:
        user = input('请输入用户名\n')
        pwd = input('请输入密码\n')
        red = Redis_login(user,pwd)
        red.login()
