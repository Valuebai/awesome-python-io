#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2020/3/16 11:43
# @Software: PyCharm
# @Author  : https://github.com/Valuebai/
"""

## 题目描述

```
比较两个版本号 version1 和 version2。
如果 version1 > version2 返回 1，如果 version1 < version2 返回 -1， 除此之外返回 0。

你可以假设版本字符串非空，并且只包含数字和 . 字符。

 . 字符不代表小数点，而是用于分隔数字序列。

例如，2.5 不是“两个半”，也不是“差一半到三”，而是第二版中的第五个小版本。

你可以假设版本号的每一级的默认修订版号为 0。例如，版本号 3.4 的第一级（大版本）和第二级（小版本）修订号分别为 3 和 4。其第三级和第四级修订号均为 0。
 

示例 1:

输入: version1 = "0.1", version2 = "1.1"
输出: -1
示例 2:

输入: version1 = "1.0.1", version2 = "1"
输出: 1
示例 3:

输入: version1 = "7.5.2.4", version2 = "7.5.3"
输出: -1
示例 4：

输入：version1 = "1.01", version2 = "1.001"
输出：0
解释：忽略前导零，“01” 和 “001” 表示相同的数字 “1”。
示例 5：

输入：version1 = "1.0", version2 = "1.0.0"
输出：0
解释：version1 没有第三级修订号，这意味着它的第三级修订号默认为 “0”。
 

提示：

版本字符串由以点 （.） 分隔的数字字符串组成。这个数字字符串可能有前导零。
版本字符串不以点开始或结束，并且其中不会有两个连续的点。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/compare-version-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

## 代码实现
"""


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        """
        Leetcode-165-比较两个版本号大小

            第一步：根据"."对字符串进行分割，得到list
            第二步：比较2个列表长度，将短的列表用字符'0'补充，使长度相同
            第三步：用while循环，逐一比较每个位置i的大小

        :param version1: str，例如：1.2.1
        :param version2: str，例如：1.1
        :return: 0表示两个版本相等，1表示version1大于version2，-1表示v1小于v2
        """
        a = version1.split('.')  # 根据.进行切分,得到list
        b = version2.split('.')
        if len(a) > len(b):
            b.extend(['0'] * (len(a) - len(b)))  # 注意extend和append的区别
        if len(b) > len(a):
            a.extend(['0'] * (len(b) - len(a)))

        i = 0
        while i < len(a) or i < len(b):
            if int(a[i]) > int(b[i]):
                return 1
            elif int(a[i]) < int(b[i]):
                return -1
            else:
                i = i + 1

        return 0


def compareVersion(version1: str, version2: str) -> int:
    """
    Leetcode-165-比较两个版本号大小

        第一步：根据"."对字符串进行分割，得到list
        第二步：比较2个列表长度，将短的列表用字符'0'补充，使长度相同
        第三步：用while循环，逐一比较每个位置i的大小

    :param version1: str，例如：1.2.1
    :param version2: str，例如：1.1
    :return: 0表示两个版本相等，1表示version1大于version2，-1表示v1小于v2
    """
    a = version1.split('.')
    b = version2.split('.')
    if len(a) > len(b):
        b.extend(['0'] * (len(a) - len(b)))
    if len(b) > len(a):
        a.extend(['0'] * (len(b) - len(a)))

    i = 0
    while i < len(a) or i < len(b):
        if int(a[i]) > int(b[i]):
            return 1
        elif int(a[i]) < int(b[i]):
            return -1
        else:
            i = i + 1

    return 0


if __name__ == "__main__":
    print(compareVersion("1.0.1", "1"))
    print(compareVersion("0.1", "1.1"))
    print(compareVersion("7.5.2.4", "7.5.3"))
    print(compareVersion("1.01", "1.001"))
    print(compareVersion("1.9", "1.9.0.0.0.1"))
    s = Solution()
    print(s.compareVersion("1.01", "1.001"))
