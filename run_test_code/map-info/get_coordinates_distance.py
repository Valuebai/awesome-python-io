#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@IDE    ：PyCharm
@Author ：LuckyHuibo
@Date   ：2019/7/15 11:05
@Desc   ：python，用经纬度计算地图上2个点的距离

1、经度、纬度、经纬度都分别是什么？
经纬度是经度与纬度的合称组成一个坐标系统。又称为地理坐标系统，它是一种利用三度空间的球面来定义地球上的空间的球面坐标系统，能够标示地球上的任何一个位置。

经纬度 coordinates
经度 longitude #为方便记忆，可以认为long的是经度
纬度 latitude

地球上所有的经线都一样长，并汇集到两极。通过英国格林威治天文台的经线为零度，称作本初子午线。由此向东、向西各分成180°，分别称东经和西经。东、西经180°线是重合在一起的。

在地球表面与经线直交的线叫纬线，把地球分成南北两半，到南极和北极距离相等的纬线就是赤道。所有的纬线都呈东西方向、与赤道平行，但长短不等，愈往极地愈短。

赤道的纬度是0°，南北极是90°，赤道以北叫北纬，赤道以南叫南纬。习惯上，人们还把纬度0～30°叫低纬，30～60°叫中纬，60～90°叫高纬。南、北纬23.5°，分别被称为南、北回归线。

经度：东经为正数，西经为负数。
纬度：北纬为正数，南纬为负数。

2、如何取地图上某个点的坐标？
经纬度 -> 地址
http://www.gpsspg.com/maps.htm

地址 -> 经纬度
#百度拾取坐标系统
#高德地图获取鼠标点击经纬度
#腾讯地图坐标拾取器

3、坐标之间的距离该如何计算？
地球上的位置现在都用经纬度来进行精确标注，又因为地球是一个球体，两点之间的距离不能简单的用平面上的方法来算，要考虑球面的因素，而常用的是Haversine公式，这里公式细节不细说，直接放出用Python计算的方法，方便参考和使用。

注：虽然叫「经纬度」但一般坐标里面是把「纬度放在前面」，即：「坐标 = （纬度，经度）」。且对于国内的坐标情况，一般是纬度数值要小于经度的数值。
=================================================='''

# 第一种计算方式
import math


def get_haversine_distance(origin, destination):
    """
        Calculate the Haversine distance.（用Haversine公式来计算经纬度距离）
        # 先纬度，后经度，跟另一个有区别
    Parameters
    ----------
    origin : tuple of float
        (lat, long)
    destination : tuple of float
        (lat, long)

    Returns
    -------
    distance_in_km : float

    Examples
    --------
    > origin = (48.1372, 11.5756)  # Munich
    > destination = (52.5186, 13.4083)  # Berlin
    > round(distance(origin, destination), 1)
    504.2
    """
    lat1, lon1 = origin  # 纬度1，经度1（十进制度数）
    lat2, lon2 = destination  # 纬度2，经度2（十进制度数）
    radius = 6371  # km，地球的平均半径

    # Haversine公式
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) * math.sin(dlat / 2) +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dlon / 2) * math.sin(dlon / 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = radius * c  # 返回的单位是公里，需要米的话乘以1000
    return d


# 第二种计算方式
from math import sin, asin, cos, radians, fabs, sqrt


def haversine(lon1, lat1, lon2, lat2):  # 经度1，纬度1，经度2，纬度2 （十进制度数）
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    # 先经度，后纬度，跟另一个有区别
    """
    # 将十进制度数转化为弧度
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine公式
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # 地球平均半径，单位为公里
    # 这里乘以1000，返回的单位是米
    return c * r * 1000


if __name__ == "__main__":
    # 38352.523132 (km为单位)
    loc1 = (22.599578, 113.973129)
    loc2 = (22.6986848, 114.3311032)
    print(get_haversine_distance(loc1, loc2))

    # 38352.523132 (m为单位)
    print(haversine(113.973129, 22.599578, 114.3311032, 22.6986848))
