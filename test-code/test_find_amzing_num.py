"""
@author: LuckyHuibo
@Desc: 第2个问题的描述与解法
@Time: 2019.06.16

2. Simple Number Finding
You are playing a card game with your friends. This game in China named “扎金花”. In this game, the 
2, 3, 5 are some simple powerful numbers. Because the combination of 2,3,5 is less than any other combinations
but greater than the AAA, which is the king in this game. In today, you want to find if a number is a simple
number, in which their factors only include 2, 3 and 5.
So your task is to find out whether a given number is an amazing number.
E.g
Input: 6
Output: (2, 3)
Explanation: 6 = 2 x 3
Input: 8
Output: (2, 2, 2)
Explanation: 8 = 2 x 2 x 2
Input: 14
Output：None
Explanation: 14 is not amazing since it includes another prime factor 7.
How to check your answer: 
If you test 1845281250, your program should give (2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5, 5, 5)
If you test 3690562500, your program should give (2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5, 5, 5);
If you test 1230187500, your program should give (2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5, 5, 5);
If you test 10023750, your program should give None;
"""


def findAmazingNum(num):
    # 将数据存储到数组当中
    result_list = []
    numOrigin = num

    # 如果输入的数字小于0，则返回空
    if num <= 0:
        return None
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
        return None
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
    # 输入一个整数，默认是输入字符串，需要转换为int
    num = int(input("Input:"))
    findAmazingNum(num)
