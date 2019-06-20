#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@IDE    ：PyCharm
@Author ：LuckyHuibo
@Date   ：2019/6/17 17:53
@Desc   ：
编写一个程序判断给定的数是否为丑数。

丑数就是只包含质因数 2, 3, 5 的正整数。

示例 1:

输入: 6
输出: true
解释: 6 = 2 × 3
示例 2:

输入: 8
输出: true
解释: 8 = 2 × 2 × 2
示例 3:

输入: 14
输出: false
解释: 14 不是丑数，因为它包含了另外一个质因数 7。
说明：

1 是丑数。
输入不会超过 32 位有符号整数的范围: [−231,  231 − 1]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ugly-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
=================================================='''


class Solution:
    # 表示传入的参数为num，且必须是整形，isUgly返回值是bool类型True/False
    def isUgly(self, num: int) -> bool:
        # 将数据存储到数组当中
        result_list = []
        numOrigin = num

        # 如果输入的数字小于0，则返回空
        if num <= 0:
            return False
        if num == 1:
            print("输出：True")
            print("解释：1 是丑数")
            return True
        # 判断2,3,5是否为输入数字的因子,有的话存储到list中并将数字除以2/3/5
        while num % 2 == 0:
            num = num / 2
            result_list.append(2)
        while num % 3 == 0:
            num = num / 3
            result_list.append(3)
        while num % 5 == 0:
            num = num / 5
            result_list.append(5)
        # 如果factors里面包含7，打印下面的
        if (num % 7 == 0 or num / 7 == 1):
            print(numOrigin, "is not amazing since it includes another prime factor 7.")
            return
        if (num >= 11):
            # 这边暂时判断其他质数11的，后面有时间再优化打印具体的质数
            print("Output: None")
            return None

        # 如果存储的元组为空打印None，否则打印具体的
        if not result_list:
            print("Output: None")
        else:
            # 将数组转化为元组，再打印输出
            print("Output:", tuple(result_list))

        # 按格式num = 2 x 2 x 2...打印输入的数字
        print("Explanation:", numOrigin, "= ", end="")
        for i in range(0, len(result_list) - 1):
            print(result_list[i], "x ", end="")
        print(result_list[-1])


if __name__ == "__main__":
    # 请输入数字，且为整形
    num = int(input('输入: '))
    mySolu = Solution()
    mySolu.nthUglyNumber()
