# #!/usr/bin/env python
# # -*- coding: UTF-8 -*-

import time
import requests
import xlwt
import json
import pandas as pd


def get_periodical_year_article(perioId, publishYear):
    """
    获取 XXX年《期刊》的所有文章ID
    :param perioId: 期刊代码，如汉语学习代码为：hanyxx
    :param publishYear: 出刊年份
    :return: []
    """

    URL = 'http://www.wanfangdata.com.cn/sns/third-web/per/perio/articleList'
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    }

    id_list = []
    # 默认期刊只有6期，从第1期到6期
    for issueNum in range(1, 6):
        # 默认每期的文章最多有30篇
        for page_id in range(1, 4):

            datas = {
                "page": page_id,
                "pageSize": 10,
                "perioId": perioId,
                "publishYear": publishYear,
                "issueNum": issueNum,
            }
            try:
                session = requests.session()
                res = session.post(URL, data=datas, headers=headers)
                data = res.content.decode()
                # print(data)
                info = json.loads(data)
                if not info['pageRow']:
                    continue
                else:
                    # 获取文章id
                    for jn in info['pageRow']:
                        id_list.append(jn['article_id'])
                print('《{}》第{}期{}页的文章：'.format(perioId, issueNum, page_id), end="")
                print(info)
            except Exception as e:
                print(e)
    print(id_list)
    return id_list


def get_all_article_id(perioId='hanyxx'):
    """
    获取《某期刊》所有文章ID，这里默认了《汉语学习》，如果需要获取其他期刊的，自行获取相关期刊id，加for循环处理
    :param perioId: 期刊名称
    :return: [[],[]]
    """
    all_artile_list = []
    # 2001年到2020年的文章ID
    for year in range(2001, 2021):
        article_id = get_periodical_year_article(perioId, year)
        all_artile_list.append(article_id)
    print(all_artile_list)

    return all_artile_list


def json_to_excel(json_data):
    """
    读取json数据并存到xlxs中
    json_data: 数据格式为：[{},{},{}]
    """
    json_file = json_data
    print(json_file)
    workbook = xlwt.Workbook()
    sheet1 = workbook.add_sheet('save_data')

    # 获取表头，即第一行
    ll = list(json_file[0].keys())
    for i in range(0, len(ll)):
        sheet1.write(0, i, ll[i])  # 写入第一行，i列，数据

    # 讲数据写入第2行到N行
    for j in range(0, len(json_file)):
        m = 0
        ls = list(json_file[j].values())  # 获取json字段对应的数据
        for k in ls:
            sheet1.write(j + 1, m, k)
            m += 1
    workbook.save('save_data.xls')


def get_wanfang_dataone_excel(req_id):
    url = 'http://d.wanfangdata.com.cn/Detail/Periodical/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
    }
    body = {
        "Id": req_id
    }
    try:
        res = requests.post(url, headers=headers, json=body)
        data = res.content.decode()
        # print(data)
        info = json.loads(data)
        print(info)
        # 拼接数据成[{}]
        json_list = []
        if not info['detail']:
            json_list.append('')
        # 拼接数据
        else:
            json_infos = {
                "文章标题": info['detail'][0]['periodical']['Title'],
                "摘要": info['detail'][0]['periodical']['Abstract'],
                "关键字": info['detail'][0]['periodical']['Keywords'],
                "作者": info['detail'][0]['periodical']['Creator'],
                "作者单位": info['detail'][0]['periodical']['AuthorOrg'],
                "期刊名称": info['detail'][0]['periodical']['PeriodicalTitle'],
                "年，卷(期)": str(info['detail'][0]['periodical']['PublishYear']) + '(' + str(
                    info['detail'][0]['periodical']['Issue']) + ")",
                "基金项目": info['detail'][0]['periodical']['Fund'],
                "在线发表时间": info['detail'][0]['periodical']['MetadataOnlineDate'],
                "链接": 'http://d.wanfangdata.com.cn/periodical/' + info['detail'][0]['periodical']['Id'],
            }

            json_list.append(json_infos)
        return json_list
    except Exception as e:
        print(e)


def get_wanfang_data():
    """
    一开始的DEMO
    :return:
    """
    url = 'http://d.wanfangdata.com.cn/Detail/Periodical/'

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
    }
    body = {
        "Id": "CASS_43577964"
    }

    start_num = 43577964
    end_num = 43577969
    for i in range(start_num, end_num + 1):
        json_list = []
        article_id = 'CASS_{}'.format(i)
        # 替换请求Boby id
        body['Id'] = article_id
        res = requests.post(url, headers=headers, json=body)
        data = res.content.decode()
        # print(data)
        info = json.loads(data)
        print(info)
        if not info['detail']:
            json_list.append({})
        # 拼接数据
        else:
            json_infos = {

                "文章标题": info['detail'][0]['periodical']['Title'],
                "摘要": info['detail'][0]['periodical']['Abstract'],
                "关键字": info['detail'][0]['periodical']['Keywords'],
                "作者": info['detail'][0]['periodical']['Creator'],
                "作者单位": info['detail'][0]['periodical']['AuthorOrg'],
                "期刊名称": info['detail'][0]['periodical']['PeriodicalTitle'],
                "年，卷(期)": str(info['detail'][0]['periodical']['PublishYear']) + '(' + str(
                    info['detail'][0]['periodical']['Issue']) + ")",
                "基金项目": info['detail'][0]['periodical']['Fund'],
                "在线发表时间": info['detail'][0]['periodical']['MetadataOnlineDate'],
                "链接": 'http://d.wanfangdata.com.cn/periodical/' + info['detail'][0]['periodical']['Id'],

            }

            json_list.append(json_infos)
        # 停顿1s，不要频繁发起请求
        # time.sleep(1)

    print(json_list)
    return json_list


def pandas_json_to_excel(json_data):
    """
    #TODO：pandas追加数据到excel ，有空再弄
    """

    
    rows_num = 0
    try:
        # 读取excel，获取行数
        df = pd.read_excel('save_data.xls', sheet_name='save_data')
        rows_num = df.shape[0]
        print(rows_num)
    except Exception as e:
        print(e)

    writer = pd.ExcelWriter('save_data.xls', sheet_name='save_data')
    for jsn in json_data:

        df = pd.DataFrame(pd.json_normalize(jsn))
        if rows_num > 0:
            df.to_excel(writer, startrow=int(rows_num) + 1, sheet_name='save_data')
        else:
            df.to_excel(writer)


if __name__ == '__main__':
    # j_data = get_wanfang_data()
    # # json_to_excel(j_data)
    # pandas_json_to_excel(j_data)
    # get_periodical_year_article(perioId='hanyxx', publishYear=2020)
    # get_all_article_id()

    article_list = get_all_article_id()
    save_json = []
    for year_list in article_list:
        for arti_id in year_list:
            print(arti_id)
            arti_json = get_wanfang_dataone_excel(arti_id)
            save_json.append(arti_json[0])

    json_to_excel(save_json)
    try:
        with open('save.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(save_json))
    except Exception as e:
        print(e)
