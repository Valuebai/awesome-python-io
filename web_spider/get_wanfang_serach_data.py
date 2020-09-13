#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import requests
import json

# URL = 'http://www.wanfangdata.com.cn/searchResult/getCoreSearch.do?d=0.1815591873188529'
# headers = {
#     "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
#     "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
# }
# datas = {
#     "paramStrs": "主题:(汉韩)",
#     "classType": "degree-degree_artical",
#     "pageNum": 1,
#     "pageSize": 20,
#     "isSearchSecond": "false",
#     "chineseEnglishExpand": "false",
#     "topicExpand": "false",
#     "searchWay": "AdvancedSearch",
#     "corePerio": "false",
# }
#
# session = requests.session()
# res = session.post(URL, data=datas, headers=headers)
# data = res.content.decode()
# print(data)

# id_list = []
#
# num = 22
# for page_id in range(1, num):
#
#     datas = {
#         "paramStrs": "主题:(汉韩)",
#         "classType": "degree-degree_artical",
#         "pageNum": page_id,
#         "pageSize": 20,
#         "isSearchSecond": "false",
#         "chineseEnglishExpand": "false",
#         "topicExpand": "false",
#         "searchWay": "AdvancedSearch",
#         "corePerio": "false",
#     }
#
#     session = requests.session()
#     res = session.post(URL, data=datas, headers=headers)
#     data = res.content.decode()
#     print(data)
#     # info = json.loads(data)
#     # for thesisnum in info['pageRow']:
#     #     id_list.append(thesisnum['id'])
#     # print('第{}页:'.format(page_id))


# url = 'http://d.wanfangdata.com.cn/Detail/Thesis/'
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
#     "Content-Type": "application/json;charset=UTF-8",
#     "Host":"d.wanfangdata.com.cn"
# }
# body = {
#     "Id": "D048000"
# }
#
# res = requests.post(url, headers=headers, json=body)
# data = res.content.decode()
# print(data)


url = ' http://d.wanfangdata.com.cn/Detail/Thesis/'  # 坑，一定要从requests URL复制

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    "Content-Type": "application/json;charset=UTF-8",
    "Host": "d.wanfangdata.com.cn"
}
body = {
    "Id": "D048000"
}

json_list = []
for i in range(0, len(id_list) + 1):
    thesis_id = '{}'.format(i)
    body['ID'] = thesis_id
    res = requests.post(url, headers=headers, json=body)
    data = res.content.decode()
    print(data)
    info = json.loads(data)
    # print(info)
    json_infos = {
        "文章标题": info['detail'][0]['thesis']['Title'],
        "关键词": info['detail'][0]['thesis']['Keywords'],
        "摘要": info['detail'][0]['thesis']['Abstract'],
        "作者": info['detail'][0]['thesis']['Creator'],
        "作者单位": info['detail'][0]['thesis']['OrganizationNorm'],
        "层次": info['detail'][0]['thesis']['Degree'],
        "专业": info['detail'][0]['thesis']['Major'],
        "导师": info['detail'][0]['thesis']['Tutor'],

        "链接": 'http://d.wanfangdata.com.cn/Detail/Thesis/' + info['detail'][0]['thesis']['Id']
        # "在线发表时间":['pageRow'],#??
    }
    json_list.append(json_infos)
print(json_infos)
