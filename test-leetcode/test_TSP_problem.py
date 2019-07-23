#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@IDE    ：PyCharm
@Author ：LuckyHuibo
@Date   ：2019/7/23 17:18
@Desc   ：
#### 问题描述：TSP-用动态规划算法求解旅行商问题

旅行推销员问题（英语：Travelling salesman problem, TSP）是这样一个问题：给定一系列城市和每对城市之间的距离，求解访问每一座城市一次并回到起始城市的最短回路。


#### 解题思路：


对于TSP问题，最简单的求解方式是贪心算法，即每次去下一个城市时都贪心地先去距离最短的城市，但是这样的问题时到达最后一个城市时再回到出发点却不一定是最短的，这种算法的好处是算法简单，求解速度非常快，缺点显而易见，无法求出最优解。


动态规划算法是通过拆分问题，大事化小，小事化了，从而解决问题，这部分的难点在于建立递推过程，理解递推思想。


对于这个问题的解题思路[1]如下：


先大事化小，我们首先考虑4个城市，城市间距离矩阵如下：

![enter description here](https://www.github.com/Valuebai/my-markdown-img/raw/master/小书匠/1563873726149.png)

我们从城市0出发，经过城市{1, 2, 3}再回到城市0，然后分解问题为，{1, 2, 3}又可以分解为(1, {2, 3})、（2, {1, 3}）、（3, {1, 2})，然后继续分解，知道{}里为空，图解如下：
![enter description here](https://www.github.com/Valuebai/my-markdown-img/raw/master/小书匠/1563873781810.png)


 这时候你可能不理解(1, {2, 3})是什么意思，就这是从1出发，经过2，3的过程，那么这样的话便缺少了3到0的距离了啊，其实当递归到最后的时候，我们在设置递归结束条件时便加上了这段距离，如果你对这一部分还是有疑问，那么先保留疑问下面看代码你可能就明白了。

那么，我们可以得到递归最重要的状态转移方程：
![enter description here](https://www.github.com/Valuebai/my-markdown-img/raw/master/小书匠/1563873797399.png)

T(s,init)代表的意思是从init点出发经过s中全部的点回到0的距离。dist是distance的缩写

看到这里，如果你明白了，那么恭喜你，基本思想你已经掌握了！

那么，在代码实现过程中我们如何去表示{1，2，3}呢，你或许想可以用列表记录之类，但是这里有一个非常巧妙的方法，我用二进制数来表示，用位记录，比如说000便是{}，001是{1}， 010是{2}， 011是{1，2}，即某一位上有数，便说明这经过哪个城市。
![enter description here](https://www.github.com/Valuebai/my-markdown-img/raw/master/小书匠/1563873817087.png)


因此，我们在实现代码时可以用一个n x 2^(n-1)的矩阵进行数据存储，为什么要进行数据存储，因为在递归过程中如果不进行数据存储，计算机需要进行大量的重复计算过程。
![enter description here](https://www.github.com/Valuebai/my-markdown-img/raw/master/小书匠/1563873829066.png)

 终于，可以愉快的写代码了

=================================================='''
import random
import matplotlib.pylab as plt

import pandas as pd
import numpy as np
import math
import time

if __name__ == "__main__":
    # 随机生成20个点
    latitudes = [random.randint(-100, 100) for _ in range(20)]
    longitude = [random.randint(-100, 100) for _ in range(20)]
    chosen_p = (-50, 10)  # 起点
    plt.scatter(latitudes, longitude)
    #plt.show()  # 在pycharm需要添加显示的，jupternotebook不需要加就能显示

    point_list = [(x, y) for x, y in zip(latitudes, longitude)]
    point_list.insert(0, chosen_p)
    point_array = np.array(point_list)

    # 距离矩阵
    dist = np.zeros((point_array.shape[0], point_array.shape[0]))
    for i in range(point_array.shape[0]):
        for j in range(point_array.shape[0]):
            dist[i, j] = math.sqrt(np.sum((point_array[i, :] - point_array[j, :]) ** 2))

    """
    N:计数
    s:二进制表示，遍历过得城市对应位为0，未遍历为1
    dp:动态规划的距离数组
    dist：目的地间距离矩阵
    sumpath:目前的最小路径总长度
    Dtemp：当前最小距离
    path:记录下一个应该到达的城市
    """

    N = point_array.shape[0]
    path = np.ones((2 ** N - 1, N), dtype=np.int)
    dp = np.ones((2 ** N - 1, N)) * -1


    # 代码的核心
    def TSP(s, init):
        if dp[s][init] != -1:
            return dp[s][init]

        if s == 0:  # 成立代表遍历结束
            return dist[0][init]

        sumpath = float('inf')

        for i in range(N):
            if s & (1 << i):  # 判断是否遍历过，未遍历则执行
                m = TSP(s & (~ (1 << i)), i) + dist[i][init]  # s & (~ (1 << i))让遍历过的点的相应位置变0
                if m < sumpath:
                    sumpath = m
                    path[s][init] = i
        dp[s][init] = sumpath
        return dp[s][init]


    init_point = 0
    s = 0
    for i in range(1, N):
        s = s | (1 << i)

    start = time.time()
    distance = TSP(s, init_point)
    end = time.time()

    for i in range(1, N):
        s = s | (1 << i)
    init = 0
    num = 0
    print(distance)
    route = [chosen_p]

    while True:
        print(path[s][init])
        init = path[s][init]
        route.append(point_list[init])
        s = s & (~ (1 << init))
        num += 1
        if num > N - 2:
            break
    print("程序的运行时间是：%s" % (end - start))

    # 此代码为结果可视化展示
    route.append(chosen_p)
    plt.scatter(latitudes, longitude)
    plt.scatter([chosen_p[0]], [chosen_p[1]], color='r')
    x = [point[0] for point in route]
    y = [point[1] for point in route]
    plt.plot(x, y, color='black')
    plt.show()


    """运行时间有点长的
    C:\Python37\python.exe C:/mycode/awesome-python-io/test-leetcode/test_TSP_problem.py
758.4780798890544
13
20
12
18
14
11
8
7
5
10
9
2
16
6
4
1
17
15
3
19
程序的运行时间是：230.9781723022461

Process finished with exit code 0

    """
