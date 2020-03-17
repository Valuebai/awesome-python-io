#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2020/3/16 16:18
# @Software: PyCharm
# @Author  : https://github.com/Valuebai/
"""
    88. 合并两个有序数组
    ~~~~~~~~~~~~~~~
    给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 num1 成为一个有序数组。
     
    说明:
    1. 初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
    2. 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。     

    示例:

    输入:
    nums1 = [1,2,3,0,0,0], m = 3
    nums2 = [2,5,6],       n = 3

    输出: [1,2,2,3,5,6]
"""


def mergeTwoPointers_first(nums1, m, nums2, n):
    """
    方法二 : 双指针 / 从前往后

    直觉，一般而言，对于有序数组可以通过 双指针法 达到O(n + m)O(n+m)的时间复杂度。
    最直接的算法实现是将指针p1 置为 nums1的开头， p2为 nums2的开头，在每一步将最小值放入输出数组中。
    由于 nums1 是用于输出的数组，需要将nums1中的前m个元素放在其他地方，也就需要 O(m)O(m) 的空间复杂度。

    复杂度分析
    - 时间复杂度 : O(n + m)O(n+m)。
    - 空间复杂度 : O(m)O(m)。

    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """
    # Make a copy of nums1.
    nums1_copy = nums1[:m]
    nums1[:] = []

    # Two get pointers for nums1_copy and nums2.
    p1 = 0
    p2 = 0

    # Compare elements from nums1_copy and nums2
    # and add the smallest one into nums1.
    while p1 < m and p2 < n:
        if nums1_copy[p1] < nums2[p2]:
            nums1.append(nums1_copy[p1])
            p1 += 1
        else:
            nums1.append(nums2[p2])
            p2 += 1

    # if there are still elements to add
    if p1 < m:
        nums1[p1 + p2:] = nums1[p1:]
    if p2 < n:
        nums1[p1 + p2:] = nums2[p2:]

    print(nums1)


def merge(nums1, m, nums2, n):
    """
    复杂度分析

    - 时间复杂度 : O((n + m)\log(n + m))O((n+m)log(n+m))。
    - 空间复杂度 : O(1)O(1)。

    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """
    # nums1 = A  # 更改 nums1 这一变量名所指向的对象。让 nums1 变量指向 A 所指向的对象
    # nums1[:] = A  # 对nums1指向的对象赋值。把A变量指向的对象的值逐个copy到nums1指向的对象中并覆盖nums1指向的对象的原来值。
    # 详细解释 https://leetcode-cn.com/problems/merge-sorted-array/solution/gelthin-gui-bing-pai-xu-by-gelthin/
    nums1[:] = sorted(nums1[:m] + nums2)  # sorted返回的是一个新的列表对象


if __name__ == "__main__":
    mergeTwoPointers_first(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3)
