"""
题目描述：求出数组中等于目标值的两个数的索引，假定肯定存在两个数并且同一个索引上的数不能用两次。
解决方法：利用python3解决，详情见下方
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        思路：用空间换时间，利用字典+内置函数enumerate来记录遍历的传递列表
              记录在字典中的是{2:0, 7:1}类似的形式
              利用target=num+another_num来确定另一个数是否存在，
              如果存在，则返回列表下标
        :param nums:List[int]
        :param target:int
        :return:List[int]
        """
        dicts = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in dicts:
                return [dicts.get(another_num), index]
                s
            dicts[num] = index

    def twoSum_violence(self, nums, target):
        """
        利用暴力算法来找到答案，并返回列表的下标，用到了for + range()内置函数的
        :param nums:List[int]
        :param target: int
        :return:i,j返回列表的下标
        """
        ls = len(nums)
        for i in range(ls):
            for j in range(i + 1, ls):
                if (nums[i] + nums[j]) == target:
                    return i, j


if __name__ == "__main__":
    mynums = [2, 7, 11, 15]
    mytarget = 9
    mysolution = Solution()
    print(mysolution.twoSum(mynums, mytarget))
    # print(mysolution.twoSum_violence(mynums, mytarget))
