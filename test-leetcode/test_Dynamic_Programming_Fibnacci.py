#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@IDE    ：PyCharm
@Author ：LuckyHuibo
@Date   ：2019/7/17 17:23
@Desc   ：动态规划

【核心思想】
根据Fibnacci 提炼出来
既然重复计算如此耗时，那么能不能不重复计算这些值呢？
当第一次计算了这些值的时候，我们把他们缓存起来，
等到再次使用的时候，直接把他们拿过来用，
这样就不用做大量的重复计算了。这就是动态规划的核心思想。
=================================================='''
import time


def fibnacci(n):
    """
    fibonacci数列是递归算法的一个典型的例子
    Fibnacci(120) ，这个千万不敢试，会怀孕，说错了，是会看不到明天的太阳。（官方统计算完基本上要250000年）
    :param n:
    :return:
    """
    if n == 0 or n == 1:
        return 1
    else:
        return fibnacci(n - 1) + fibnacci(n - 2)


def fastFibnacci(n, memo={}):
    """
    加了memo={}字典来存储递归过的数据，不用每次递归都去算，有点像redis缓存一样，
    复杂度为O(n)
    :param n: 数字,int
    :param memo: 字典，存储递归过的数据
    :return:
    """
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fastFibnacci(n - 1, memo) + fastFibnacci(n - 2, memo)
        memo[n] = result
        return result


if __name__ == "__main__":
    # 没有使用memo记录，直接去递归的
    num = 37
    start = time.perf_counter()
    fibnacci(num)
    end = time.perf_counter()
    print("Fibnacci sequense costs", end - start)

    # 使用memo记录，变为动态规划的
    num = 120
    start = time.perf_counter()
    fastFibnacci(num)
    end = time.perf_counter()
    print("fastFibnacci sequense costs", end - start)
