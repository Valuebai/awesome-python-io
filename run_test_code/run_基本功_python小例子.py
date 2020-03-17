# # # 调用对象的 repr() 方法，获得该方法的返回值，如下例子返回值为字符串
# # class Student(object):
# #     def __init__(self, id, name):
# #         self.id = id
# #         self.name = name
# #
# #     def __repr__(self):
# #         return 'id=' + self.id + ', name=' + self.name
# #
# #     @classmethod
# #     def f(cls):
# #         print(cls)
# #
# #
# # xiaoming = Student(id='001', name='xiaoming')
# #
# # print(
# #     xiaoming
# # )
# #
# # print(
# #     ascii(xiaoming)
# # )
# #
# # s = ['a', 'b', 'c']
# # for i, v in enumerate(s):
# #     print(i, v)
# #
# # print("i am {0}, age{1}".format("tom", 18))
# #
# # print(frozenset([1, 1, 3, 2, 3]))
# #
# #
# # class Student(object):
# #     def __init__(self, id, name):
# #         self.id = id
# #         self.name = name
# #
# #     def __repr__(self):
# #         return 'id=' + self.id + ', name=' + self.name
# #
# #
# # xiaoming = Student(id='001', name='xiaoming')
# # getattr(xiaoming, 'name')  # 获取xiaoming这个实例的name属性值
# #
# #
# # class undergraduate(Student):
# #     def studyClass(self):
# #         pass
# #
# #     def attendActivity(self):
# #         pass
# #
# #
# # print(issubclass(undergraduate, Student))
# #
# # lst = [1, 3, 5]
# #
# # for i in iter(lst):
# #     print(i)
# #
# #
# # class TestIter(object):
# #     def __init__(self):
# #         self.l = [1, 3, 2, 3, 4, 5]
# #         self.i = iter(self.l)
# #
# #     def __call__(self):  # 定义了__call__ 方法的类的实例是可调用的
# #         item = next(self.i)
# #         print("__call__ is called, fowhich would return", item)
# #         return item
# #
# #     def __iter__(self):  # 支持迭代协议（即定义有__iter__() 函数
# #         print("__iter__ is called")
# #         return iter(self.i)
# #
# #
# # t = TestIter()
# # print(t())
# #
# # for e in TestIter():
# #     print(e)
# #
# # a = [
# #     {
# #         'name': 'xiaoming',
# #         'age': 18,
# #         'gender': 'male',
# #
# #     },
# #     {
# #         'name': 'xiaohong',
# #         'age': 11,
# #         'gender': 'female',
# #     }
# #
# # ]
# # a = sorted(a, key=lambda x: x['age'], reverse=False)
# # print(a)
#
# class Student(object):
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name
#
#     def __repr__(self):
#         return 'id=' + self.id + ', name=' + self.name
#
#
# xiaoming = Student(id='001', name='xiaoming')
# print(type(xiaoming))
#
# x = [3, 2, 1]
# y = [4, 5, 6]
#
# print(list(zip(y, x)))
#
# a = range(5)
# b = list('abcde')
#
# print(b)
# print([str(y) + str(x) for x, y in zip(a, b)])
#
# import time
#
#
# def exceter(f, n):
#     i = 0
#     t1 = time.time()
#
#     def wrapper():
#         try:
#             f()
#         except Exception as e:
#             nonlocal i
#             i += 1
#             print(f'{e.args[0]}:{i}')
#             t2 = time.time()
#             if i == n:
#                 print(f'spending time:{round(t2 - t1, 2)}')
#
#     return wrapper
#
#
# from math import ceil
#
#
# def divide(lst, size):
#     if size <= 0:
#         return [lst]
#     print(lst[1: (1 + 1) * size])
#     return [lst[i * size: (i + 1) * size] for i in range(0, ceil(len(lst) / size))]
#
#
# r = divide([1, 3, 5, 7, 9], 2)
# print(r)
#
# r = divide([1, 3, 5, 7, 9], 0)
# print(r)
#
#
# def filter_false(lst):
#     return list(filter(bool, lst))
#
#
# r = filter_false([None, 0, False, '', [], 'ok', [1, 2]])
# print(r)
#
#
# def max_length(*lst):
#     return max(*lst, key=lambda v: len(v))
#
#
# r = max_length([1, 2, 3], [4, 5, 6, 7], [8])
# print(f'更长的列表是{r}')
#
#
# def top1(lst):
#     return max(lst, default='列表为空', key=lambda v: lst.count(v))
#
#
# lst = [1, 3, 3, 2, 1, 1, 2]
# r = top1(lst)
# print(f'{lst}中出现次数最多的元素为：{r}')


# def rang(start, stop, n):
#     start, stop, n = float('%.2f' % start), float('%.2f' % stop), int('%.d' % n)
#     step = (stop - start) / n
#     lst = [start]
#     while n > 0:
#         start, n = start + step, n - 1
#         lst.append(round((start), 2))
#     return lst
#
#
# r = rang(1, 8, 10)
# print(r)
#
#
# def bif_by(lst, f):
#     return [[x for x in lst if f(x)], [x for x in lst if not f(x)]]
#
#
# records = [25, 89, 31, 34]
# r = bif_by(records, lambda x: x < 80)
# print(r)

# lst1 = [1, 2, 3, 4, 5, 6]
# lst2 = [3, 4, 5, 6, 3, 2]
# r = list(map(lambda x, y: x * y + 1, lst1, lst2))
# print(r)


# def max_pairs(dic):
#     if len(dic) == 0:
#         return dic
#     max_val = max(map(lambda v: v[1], dic.items()))
#     return [item for item in dic.items() if item[1] == max_val]
#
#
# r = max_pairs({'a': -10, 'b': 5, 'c': 3, 'd': 5})
# print(r)


# def merge_dict(dict1, dict2):
#     return {**dict1, **dict2}  # python3.5后支持一行代码实现合并字典
#
#
# r = merge_dict({'a': 1, 'b': 2}, {'c': 3})
# print(r)

# # 一行代码实现
# a = {'c': 3}
# b = {'a': 1, 'b': 2}
# a.update(b)
# print(a)

# from heapq import nlargest
#
#
# # 返回字典d 前n个最大值对应的键
# def topn_dict(d, n):
#     return nlargest(n, d, key=lambda k: d[k])
#
#
# r = topn_dict({'a': 1, 'b': 8, 'c': 8, 'd': 11}, 3)
# print(r)


# from collections import Counter
#
#
# # 检查两个字符是否 相同字母异序词，简称：互为变位词
#
# def anagram(str1, str2):
#     return Counter(str1) == Counter(str2)
#
#
# r = anagram('eleven+two', 'twelve+one')  # True 这是一对神器的变位词
# print(r)
# anagram('eleven', 'twelve')  # False


# from collections import ChainMap
#
# dict1 = {'x': 1, 'y': 2}
# dict2 = {'y': 3, 'z': 4}
# merged2 = ChainMap(dict1, dict2)
# print(merged2)

# from collections import namedtuple
# #
# # Point = namedtuple('Point', ['x', 'y', 'z'])  # 定义名为Point的元组，字段数组有x,y,z
# # lst = [Point(1.5, 2, 3.0), Point(-0.3, -1.0, 2.1), Point(1.3, 2.8, -2.5)]
# # print(lst[0].y - lst[1].y)

# # 使用sample抽样，如下例子从100个样本中随机抽样10个
# from random import randint, sample
#
# lst = [randint(0, 50) for _ in range(100)]
# print(lst[:5])
# lst_sample = sample(lst, 10)
# print(lst_sample)

# from random import shuffle
# from random import randint
#
# lst = [randint(0, 50) for _ in range(100)]
# print(lst)
# shuffle(lst)
# print(lst[:5])


# from random import uniform
#
# r = [(uniform(0, 10), uniform(0, 10)) for _ in range(10)]
# print(r)


# from random import gauss
#
# x = range(10)
# y = [2 * xi + 1 + gauss(0, 1) for xi in x]
# points = list(zip(x, y))
# print(points)


# from itertools import chain
#
# a = [1, 3, 4, 0]
# b = (2, 4, 6)
#
# for i in chain(a, b):
#     print(i)


def f():
    print('i\'m f')


def g():
    print('i\'m g')


[f, g][1]()
