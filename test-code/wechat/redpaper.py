#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@IDE    ：PyCharm
@Author ：LuckyHuibo
@Date   ：2019/9/18 16:27
@Desc   ：使用Python模拟抢红包程序——二倍均值法

于是我选择进行第三次尝试（较为成功）
这次尝试源于网上提供的思路，即为了保证每个人的收益均值，所以每次红包金额的范围被控制在（0.01，m/n*2）之间，
其中m为剩余金额，n为剩余人数，这样即可以保证每次红包金额的均值是相同的。

二倍均值法的缺点：每个人获得的人不会超过均值的2倍

举个例子：
假设有10个人，红包总额100元。
100/10X2 = 20, 所以第一个人的随机范围是（0，20 )，平均可以抢到10元。
假设第一个人随机到10元，那么剩余金额是100-10 = 90 元。
90/9X2 = 20, 所以第二个人的随机范围同样是（0，20 )，平均可以抢到10元。
假设第二个人随机到10元，那么剩余金额是90-10 = 80 元。
80/8X2 = 20, 所以第三个人的随机范围同样是（0，20 )，平均可以抢到10元。
以此类推，每一次随机范围的均值是相等的。

此外，前两次尝试时总是会涉及保留两位小数的问题，较为繁琐也缺少精度，因此，在此次尝试中统一将数值*100，
用randint的方法取整数后在/100,由此来保证数据的可靠性。

此次尝试中还加入了运气王组件
————————————————
版权声明：本文为CSDN博主「Colton.」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/weixin_43816074/article/details/86411185
=================================================='''

import random

total = float(input('The total amount of your rad packet:'))
division = int(input('How many people are to get the red packet:'))

each = []
rest = total * 100
restpeople = division
for i in range(1, division):
    if rest == 0:
        print('done')
    else:
        money = random.randint(1, int((rest / restpeople) * 2) - 1)
        restpeople -= 1
        rest -= money
        each.append(money)
        print('the %d player get %.2f yuan' % (i, money / 100))
each.append(rest)
print('the %d people get %.2f yuan' % (division, rest / 100))
print('the best one is %d player, get %.2f yuan' % (each.index(max(each)) + 1, each[each.index(max(each))] / 100))
