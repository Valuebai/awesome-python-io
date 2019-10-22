#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@IDE    ：PyCharm
@Author ：LuckyHuibo
@Date   ：2019/7/18 10:26
@Desc   ：利用动态规划来解决0/1背包问题呢？

首先动态规划有两个条件;
如果可以把局部子问题的解结合起来得到全局最优解，那这个问题就具备最优子结构
如果计算最优解时需要处理很多相同的问题，那么这个问题就具备重复子问题


从这两点看，0/1背包问题跟动态规划没有半毛钱的关系啊。那这两者又是怎么联系起来的呢？我们通过二叉树将两者联系起来。

二叉树是一种树，每个跟节点至多有两个子节点。

我们可以将0/1背包问题通过二叉树来表示：

[0-1背包问题]有一个背包，背包容量是M=150kg。有7个物品，物品不可以分割成任意大小。（这句很重要）
要求尽可能让装入背包中的物品总价值最大，但不能超过总容量。
物品 A B C D E F G
重量 35kg 30kg 6kg 50kg 40kg 10kg 25kg
价值 10 40 30 50 35 40 30

我们可以用下面的二叉树来表示问题的所有的解空间。

每个节点由四部分组成：

第一个集合表示：已经拿到背包里的物品
第二个集合表示：还没有决定要拿走的物品
第三个值表示：当前背包里的物品总价值
第四个值表示：背包剩余的重量

=================================================='''
import time


# item have three attribute: name,weight,value
class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.weight = float(w)
        self.value = float(v)

    def getName(self):
        return self.name

    def getValue(self):
        return self.value

    def getWeight(self):
        return self.weight

    def __str__(self):
        result = ' < ' + self.name + ' , ' + str(self.value) + ' , ' + str(self.weight) + '>'
        return result


def buildItem():
    names = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    vals = [35, 30, 6, 50, 40, 10, 25]
    weights = [10, 40, 30, 50, 35, 40, 30]
    Items = []
    for i in range(len(names)):
        Items.append(Item(names[i], vals[i], weights[i]))
    return Items


def maxValue(oraSet, leftRoom):
    """
    我们按照如下的策略进行生长
    左子树表示：拿到了第二个集合中的第一个物品，右子树表示放弃掉第二个集合中的第一个物品
    那么由着这个树一直生长下去，我们可以得到最终问题的解空间。
    很明显这是一个可以用递归解决的问题。
    那么下面就首先用递归的算法先来解决这个问题
    对于递归来说要有一个边界条件，那么这里的边界条件有两个，一个是第二个集合为空（意味着全部拿走），
    另一个是第四个值为0（意味着背包已经装满了），而他们就是叶子节点，因为树的遍历或者说是递归只能是到达叶子节点就结束了。
    :param oraSet:
    :param leftRoom:
    :return:
    """
    # leaf
    if oraSet == [] or leftRoom == 0:
        return (0, ())
    # only right tree
    elif oraSet[0].getWeight() > leftRoom:
        result = maxValue(oraSet[1:], leftRoom)
    # select the best from the left and right
    else:
        # left tree, means we select nextItem(the first value of the remains)
        nextItem = oraSet[0]
        leftVal, leftToken = maxValue(oraSet[1:], leftRoom - nextItem.getWeight())
        leftVal += nextItem.getValue()

        # right tree,means we do not select nextItem
        rightVal, rightToken = maxValue(oraSet[1:], leftRoom)

        if leftVal > rightVal:
            result = (leftVal, leftToken + (nextItem,))
        else:
            result = (rightVal, rightToken)

    return result


def fastMaxVal(oraSet, leftRoom, memo={}):
    """
    动态规划解法：
    要想用动态规划，首先要满足两个条件：重复子问题 和 最优子结构
    每个父节点会组合子节点的解来得到这个父节点为跟的子树的最优解，所以存在最优子结构。
    同一层的每个节点剩余的可选物品集合都是一样的，所以具有重复子问题
    因此可以利用动态规划来解决问题。

    动态规划的核心就是提供了一个memory，能够缓存已经计算过的值
    :param oraSet:
    :param leftRoom:
    :param memo:
    :return:
    """
    if (len(oraSet), leftRoom) in memo:
        result = memo[(len(oraSet), leftRoom)]
    elif oraSet == [] or leftRoom == 0:
        result = (0, ())
    elif oraSet[0].getWeight() > leftRoom:
        result = fastMaxVal(oraSet[1:], leftRoom, memo)
    else:
        nextItem = oraSet[0]

        leftValue, leftToken = fastMaxVal(oraSet[1:], leftRoom - nextItem.getWeight(), memo)
        leftValue += nextItem.getValue()

        rightValue, rightToken = fastMaxVal(oraSet[1:], leftRoom, memo)

        if leftValue > rightValue:
            result = (leftValue, leftToken + (nextItem,))
        else:
            result = (rightValue, rightToken)

    memo[(len(oraSet), leftRoom)] = result

    return result


def testCode():
    # 使用递归思想
    # value, token = maxValue(buildItem(), 150)
    # 使用动态规划思想
    value, token = fastMaxVal(buildItem(), 150)
    for item in token:
        print(item)
    print("Total value of tokens is ", value)


if __name__ == "__main__":
    start_time = time.perf_counter()
    testCode()
    end_time = time.perf_counter()
    print('time consumption is:', end_time - start_time)
