#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@IDE    ：PyCharm
@Author ：LuckyHuibo
@Date   ：2019/8/2 14:41
@Desc   ：爬楼梯问题
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/climbing-stairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
=================================================='''
import pysnooper


class Solution:

    @pysnooper.snoop(watch=('self.climbStairs_Power(i + 1, n)', 'self.climbStairs_Power(i + 2, n)'))
    def climbStairs_Power(self, i: int, n: int) -> int:
        """
        方法一：暴力法
        在暴力法中，我们将会把所有可能爬的阶数进行组合，也就是 1 和 2 。
        而在每一步中我们都会继续调用climbStairsclimbStairs这个函数模拟爬11阶和 22 阶的情形，并返回两个函数的返回值之和。

        climbStairs(i,n)=(i + 1, n) + climbStairs(i + 2, n)
        climbStairs(i,n)=(i+1,n)+climbStairs(i+2,n)

        其中 ii 定义了当前阶数，而 nn 定义了目标阶数。
        """
        if (i > n):
            return 0
        if (i == n):
            return 1

        # 这块的运行是有顺序的，会先运行climbStairs_Power(i + 1, n)，再运行i+2的
        """
        Starting var:.. i = 3
            Starting var:.. n = 3
            15:48:16.020198 call        40     def climbStairs_Power(self, i: int, n: int) -> int:
            15:48:16.020198 return      54             return 1
            Starting var:.. self = <__main__.Solution object at 0x00000271ACBCDF28>
            Starting var:.. i = 4
            Starting var:.. n = 3
            15:48:16.020198 call        40     def climbStairs_Power(self, i: int, n: int) -> int:
            15:48:16.020198 return      52             return 0
        """
        return self.climbStairs_Power(i + 1, n) + self.climbStairs_Power(i + 2, n)

    @pysnooper.snoop()
    def climbStairs_Dynamic(self, n: int) -> int:
        """
        方法：动态规划
        基本思路：状态转移方程：dp[i] = d[i-2]+dp[i-1]，先求出初始状态的dp[0]和dp[1]，然后用动态规划解决（其实就是斐波那契数列）：
        :param n:
        :return:
        """
        dp = []
        dp.append(1)  # 初始状态，只有1阶的时候有一种走法
        dp.append(2)  # 有2阶的时候有两种走法
        if n == 1:
            return 1
        if n == 2:
            return 2
        for i in range(2, n):
            dp.append(dp[i - 1] + dp[i - 2])
        print('[dp] is', dp)
        return dp[-1]

    @pysnooper.snoop()
    def climbStairs_Dynamic2(self, n: int) -> int:
        """
        方法：动态规划2
        其实就是减少了空间的存储，但是时空复杂度好很多，建议用这个。
        :param n:
        :return:
        """
        p = 1
        q = 2
        if n == 1:
            return 1
        if n == 2:
            return 2
        for i in range(2, n):
            p, q = q, p + q

        return q


if __name__ == "__main__":
    mySolution = Solution()
    # print('climbStairs_Dynamic2:', mySolution.climbStairs_Dynamic2(10))
    print('climbStairesPower:', mySolution.climbStairs_Power(0, 3))
