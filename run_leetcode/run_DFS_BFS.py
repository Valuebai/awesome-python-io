#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@IDE    ：PyCharm
@Author ：LuckyHuibo
@Date   ：2019/7/24 16:31
@Desc   ：广度优先算法实现 + 深度优先算法实现
传入的是字典和开始的节点
用到3个list，
list_result：记录遍历顺序
list_queue：临时列表，充当队列或者堆栈
list_closed：记录返回过的节点数据
=================================================='''
import pysnooper


def bfs(graph, s):
    """
    广度优先算法实现，使用临时queue做队列
    :param graph: 图，类型：dict
    :param s: 图中的节点，即开始的节点
    :return: 遍历的顺序，类型：list
    """
    # 记录最终的访问顺序，并返回
    result = []
    # 临时列表，在广度优先搜索中作为队列使用
    queue = []
    # 记录访问过的节点
    closed = []
    # 将开始访问的节点加到队列中
    queue.append(s)

    # 对queue队列进行遍历
    while queue:
        data = queue.pop(0)
        if data in closed:
            continue
        closed.append(data)
        result.append(data)
        for i in graph[data]:
            if i not in queue:
                queue.append(i)

    return result


@pysnooper.snoop(r'dfs.log', watch=('result', 'queue'), prefix='dfs函数测试=')
def dfs(graph, s):
    """
    深度优先算法实现，使用临时queue做堆栈
    :param graph: 图，类型：dict
    :param s: 图中的节点，即开始的节点
    :return: 遍历的顺序，类型：list
    """
    # 记录最终的访问顺序，并返回
    result = []
    # 临时列表，在广度优先搜索中作为堆栈使用
    queue = []
    # 记录访问过的节点
    closed = []
    # 将开始访问的节点加到堆栈中
    queue.append(s)

    # 对queue堆栈进行遍历
    while queue:
        data = queue.pop()
        if data in closed:
            continue
        closed.append(data)
        result.append(data)

        for i in graph[data][::-1]:
            if i not in queue:
                queue.append(i)

    return result


if __name__ == "__main__":
    # 给出图，记录节点相连接的情况（字典形式），如果不是，需要整理下
    graph = {
        1: [2, 5, 6, 9],
        2: [1, 3, 4],
        3: [2],
        4: [2],
        5: [1],
        6: [1, 7],
        7: [6, 8],
        8: [7],
        9: [1, 10],
        10: [9]
    }
    import time

    start = time.perf_counter()

    print('run dfs:', dfs(graph, 1))
    end = time.perf_counter()
    print("run dfs time is:", end - start)

    start = time.perf_counter()
    print('run bfs:', bfs(graph, 1))
    end = time.perf_counter()
    print("run dfs time is:", end - start)
