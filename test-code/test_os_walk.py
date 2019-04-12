# 通过文件名查找文件
import os


def findfile(start, name):
    """
    :param start: 文件的路径
    :param name: 要查找到的文件的名称
    :return: 返回文件的绝对路径

    查找文件，可使用 os.walk() 函数，传一个顶级目录名给它。
    下面是一个例子，查找特定的文件名并答应所有符合条件的文件全路径：
    """
    for relpath, dirs, files in os.walk(start):
        if name in files:
            full_path = os.path.join(start, relpath, name)
            abs_path = os.path.normpath(os.path.abspath(full_path))
            print(abs_path)
    return abs_path


if __name__ == '__main__':
    a = findfile('../config', 'logging.ini')
    print(a)
