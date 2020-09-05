# #!/usr/bin/env python
# # -*- coding: UTF-8 -*-

import time
import requests
import xlwt
import json


def json_to_excel(json_data):
    """
    读取json数据并存到xlxs中
    json_data: 数据格式为：[{},{},{}]
    """
    json_file = json_data
    print(json_file)
    workbook = xlwt.Workbook()
    sheet1 = workbook.add_sheet('save_data')
    ll = list(json_file[0].keys())
    for i in range(0, len(ll)):
        sheet1.write(0, i, ll[i])
    for j in range(0, len(json_file)):
        m = 0
        ls = list(json_file[j].values())
        for k in ls:
            sheet1.write(j + 1, m, k)
            m += 1
    workbook.save('save_data.xls')


url = 'http://d.wanfangdata.com.cn/Detail/Periodical/'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
}
body = {
    "Id": "CASS_43577964"
}
json_list = []
start_num = 43577964
end_num = 43577969
for i in range(start_num, end_num + 1):
    article_id = 'CASS_{}'.format(i)
    # 替换请求Boby id
    body['Id'] = article_id
    res = requests.post(url, headers=headers, json=body)
    data = res.content.decode()
    # print(data)
    info = json.loads(data)
    print(info)
    # 拼接数据
    json_infos = {
        "id": article_id,
        "文章标题": info['detail'][0]['periodical']['Title'],
        "作者": info['detail'][0]['periodical']['Creator'],
        "关键字": info['detail'][0]['periodical']['Keywords'],
        "摘要": info['detail'][0]['periodical']['Abstract'],
    }
    json_list.append(json_infos)
    # 停顿1s，不要频繁发起请求
    time.sleep(1)

print(json_list)

json_to_excel(json_list)
