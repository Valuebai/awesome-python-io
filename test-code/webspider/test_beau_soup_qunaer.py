#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@IDE    ：PyCharm
@Author ：LuckyHuibo
@Date   ：2019/7/9 16:02
@Desc   ：利用beautifulsoup 爬取去哪儿网的信息
=================================================='''

import requests
import xlwt
from bs4 import BeautifulSoup


def parseAllCities(url, cityNum):
    """
    解析首页每个城市
    :param url: 需要解析的网址，这里填的是去哪儿
    :param cityNum: 获取前N个城市的个数
    :return: none，这块做得不好，应该返回个列表之类的数据，再打印
    """
    html = requests.get(url, headers=headers).text
    bs = BeautifulSoup(html, "lxml")
    cities = bs.find_all('li', class_='mp-sidebar-item')  # 所有城市标签
    cities = cities[:cityNum]  # 取前3个城市(北京，上海，成都)
    print('城市检验:', cities)
    global currentCityIndex
    for city in cities:
        currentCityIndex = currentCityIndex + 1
        global currentRowIndex
        currentRowIndex = 2
        cityName = city.a.string  # 城市名
        print('=' * 20 + '\n' + '城市名校验：', cityName)
        cityUrl = 'http://piao.qunar.com' + city.a.get('href')  # 获取不含主机名的url
        cityUrl = cityUrl.replace('®', '&reg')  # 避免转义
        print(cityName, ':\n')
        global currentSheet
        currentSheet = workBook.add_sheet('sheet' + str(currentCityIndex), cell_overwrite_ok=True)  # 创建sheet
        currentSheet.write_merge(0, 0, 0, 7, cityName)  # 合并单元格，填写城市名
        # 填写表头（景区名称，地址，简介，月销量，链接...）
        tableList = ['景区名称', '地址', '简介', '月销量', '链接', '价格（单元：元）', '等级', '热度']
        for i, val in enumerate(tableList):
            currentSheet.write(1, i, val)
        parseSingleCity(cityName, cityUrl)
        print('\n\n\n')


# 解析每个单一的城市(解析多页)
def parseSingleCity(cityName, cityUrl):
    # 解析城市前5页内容
    global pageSize
    for i in range(1, 1 + pageSize):
        pageUrl = cityUrl + '&page=' + str(i)
        print('第%d页:' % (i))
        print('网址：:', pageUrl)
        parsePageInfo(pageUrl)  # 解析具体信息


# 解析每一页的具体信息
def parsePageInfo(pageUrl):
    html = requests.get(pageUrl, headers=headers).text
    bs = BeautifulSoup(html, "lxml")
    sightList = bs.find_all('div', class_='sight_item')  # 所有景点信息
    # 遍历每个景点
    for sight in sightList:
        sightName = sight.find_all('a', class_='name')[0].string  # 景区名
        # 景区等级，有些景区无等级所以可能异常
        try:
            sightLevel = sight.find_all('span', class_='level')[0].string
        except:
            sightLevel = '无'
        sightAddress = sight.find_all('p', class_='address')[0].span.string[3:]  # 地址，去掉'地址'二字
        sightDesc = sight.find_all('div', class_='intro')[0].string  # 景区介绍
        # 获取景区最低价格
        try:
            sightPrice = sight.find_all('span', class_='sight_item_price')[0].em.string + '元起'
        except:
            sightPrice = '免费'
        # 获取月销量
        try:
            sightNum = sight.find_all('span', class_='hot_num')[0].string
        except:
            sightNum = 0
        # 获取景区热度
        sightStarLevel = sight.find_all('span', class_='product_star_level')[0].text[2:]
        # 获取景区详细页Url
        sightDetailUrl = sight.find_all('a', class_='sight_item_do')[0].get('href')
        baseUrl = 'http://piao.qunar.com'
        sightDetailUrl = baseUrl + sightDetailUrl
        # 打印结果
        print('{0},{1},{2},{3},{4},{5},{6}'.format(sightName, sightAddress, sightDesc, sightNum, sightDetailUrl,
                                                   sightPrice, sightLevel))
        # 结果导入excel
        tableList = [sightName, sightAddress, sightDesc, sightNum, sightDetailUrl, sightPrice, sightLevel,
                     sightStarLevel]
        global currentSheet
        global currentRowIndex
        for i, val in enumerate(tableList):
            currentSheet.write(currentRowIndex, i, val)  # 填写每一行数据
        currentRowIndex = currentRowIndex + 1


if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
    }
    cityNum = 6  # 查询的城市数
    pageSize = 10  # 查询的页数
    startUrl = 'http://piao.qunar.com/'
    currentCityIndex = 0  # 当前处理的城市下标
    currentRowIndex = 2  # 当前在excel中的行号
    workBook = xlwt.Workbook()  # 创建excel表格
    currentSheet = None
    print('开始')
    parseAllCities(startUrl, 3)
    workBook.save('testBeauSoup_Save.xls')
