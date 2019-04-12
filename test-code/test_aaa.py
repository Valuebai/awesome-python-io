import pymysql


def getConnection():
    config = {
        'host': '127.0.0.1',
        'port': 3306,  # 这里是整数，请注意！！！
        'user': 'root',
        'password': 'luhuibo123',
        'database': 'ease_lite',
        'charset': 'utf8',
        'cursorclass': pymysql.cursors.DictCursor,
    }
    print(config)
    connection = pymysql.connect(**config)
    return connection


if __name__ == '__main__':
    print(getConnection())

# # 加了2个星号**的参数会以字典的形式导入
# def print_info(arg1, **vardict):
#     print('输出：')
#     print('打印第1个参数（整形）：', arg1)
#     print('打印第2个参数（字典）：', vardict)
#
#     return
#
#
# print_info(1, a=2, b=3)

# # 加了星号*的参数会以元组的形式传入
# def print_info(arg1, *vartuple):
#     print('输出：')
#     print('打印第1个参数（整形）：', arg1)
#     print('打印第2个参数（元组）：', vartuple)
#
#     return
#
#
# print_info(10)
# print_info(70, 60, 50)


# import sys
#
# def fibonacci(n):
#     #生成器函数-斐波那契数列
#     a,b,counter=0,1,0
#     while True:
#         if(counter>n):
#             return
#         yield a
#         a,b = b, a+b
#         counter+=1
#
# f = fibonacci(8) #f是一个迭代器，由生成器返回生成
#
# while True:
#     try:
#         print(next(f),',',end='')
#     except StopIteration:
#         sys.exit()


# import sys
#
# li = [1,2,3,4]
# it = iter(li)
#
# #for val in it:
# #    print(val)
# print('the first num of it is:',next(it))
# while True:
#     try:
#         print(next(it))
#     except:
#         sys.exit()


# import os
#
# def findfile(start, name):
#     for relpath, dirs, files in os.walk(start):
#         if name in files:
#             full_path = os.path.join(start, relpath, name)
#             print(os.path.normpath(os.path.abspath(full_path)))
#
# if __name__ == '__main__':
#     findfile(sys.argv[1], sys.argv[2])
