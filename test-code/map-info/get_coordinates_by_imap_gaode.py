#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@IDE    ：PyCharm
@Author ：LuckyHuibo
@Date   ：2019/7/13 13:28
@Desc   ：Passed，可以直接拿来用
=================================================='''
import requests


def get_longitude_latitude(city_info, station):
    """
    利用高德地图查询对应的地铁站经纬度信息，下面的key需要自己去高德官网申请
    https://lbs.amap.com/api/webservice/guide/api/georegeo
    :param city_info: 具体城市的地铁，如：广州市地铁
    :param station: 具体的地铁站名称，如：珠江新城站
    :return: 经纬度
    """
    addr = city_info + station
    print('*要查找的地点：' + addr)
    parameters = {'address': addr, 'key': '98a3444618af14c0f20c601f5a442000'}
    base = 'https://restapi.amap.com/v3/geocode/geo'
    response = requests.get(base, parameters, timeout=10)  # 超时设置为10s，翻墙开了全局代理会慢点的
    if response.status_code == 200:
        answer = response.json()
        x, y = answer['geocodes'][0]['location'].split(',')
        coor = (float(x), float(y))
        print('*' + station + '的坐标是：', coor)
        return coor
    else:
        return (None, None)


if __name__ == "__main__":
    print(get_longitude_latitude(city_info='广州市地铁', station='大沙东站'))
