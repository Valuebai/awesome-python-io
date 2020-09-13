import requests
import json
import xlwt
import time


def get_id_list(q_search_words="泰国学习者", page_num=30):
    """
    获取万方搜索关键字的所有论文ID，默认搜索关键词=泰国学习者，如要其他的，在调用时修改传参即可
    :param q_search_words:搜索关键词
    :param page_num:获取页面数
    :return: list
    """
    url = 'http://www.wanfangdata.com.cn/searchResult/getCoreSearch.do?d=0.9156013761938864'
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    }

    id_list = []  # 列表是存储thesis的id
    # num = 30,  # 将默认的30改为参数传入
    for page_id in range(1, page_num):  # 为了爬取多页网站

        datas = {
            "paramStrs": "主题:({})".format(q_search_words),
            "classType": "degree-degree_artical",
            "pageNum": page_id,  # 慧博修改的,page_id是一个变量，不能写死了，目的是获取多页的关键。变量要写到循环里面
            "pageSize": 20,
            "isSearchSecond": "false",
            "chineseEnglishExpand": "false",
            "topicExpand": "false",
            "searchWay": "AdvancedSearch",
            "corePerio": "false",
        }
        try:
            session = requests.session()
            res = session.post(url, data=datas, headers=headers)
            data = res.content.decode()
            # print(data)
            info = json.loads(data)
            if not info['pageRow']:
                continue
            else:
                for thesisnum in info['pageRow']:
                    id_list.append(thesisnum['id'][13:])
                print('第{}页:'.format(page_id), data)
        except Exception as e:
            print(e)

    return id_list


# ============================================
# 打印获取到的文章id_list
# print(id_list)

# 用一个id获取一篇文章

def get_thesis_abstact(article_list, req_url='http://d.wanfangdata.com.cn/Detail/Thesis/',
                       origin_url='http://d.wanfangdata.com.cn/thesis/'):
    """
    获取某个具体论文的摘要等信息，默认请求URL=http://d.wanfangdata.com.cn/Detail/Thesis/, 如果文章请求URL有变化，改变传入的参数即可
    :json_list: 传入论文的 list
    :origin_url: 文章的原始URL，加上ID即可正常打开
    :return: json list
    """
    # url = 'http://d.wanfangdata.com.cn/Detail/Thesis/'  # 坑，一定要从requests URL复制
    url = req_url

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
        "Content-Type": "application/json;charset=UTF-8",
        "Host": "d.wanfangdata.com.cn"
    }

    # 需要定义List，存储最终的结果
    json_list = []
    for i in article_list:  # 这里不用+1 ，因为id_list是个列表，循环是获取里面的值
        body = {
            "Id": i
        }  # 坑，i是id，是一个变量，而且要写到循环里面，不能写死了，

        try:
            res = requests.post(url, headers=headers, json=body)
            data = res.content.decode()
            # print(data)
            info = json.loads(data)
            print('文章{}的请求数据:'.format(i), info)
            json_infos = {
                "文章标题": info['detail'][0]['thesis']['Title'],
                "关键词": info['detail'][0]['thesis']['Keywords'],
                "摘要": info['detail'][0]['thesis']['Abstract'],
                "作者": info['detail'][0]['thesis']['Creator'],
                "作者单位": info['detail'][0]['thesis']['OrganizationNorm'],
                "层次": info['detail'][0]['thesis']['Degree'],
                "专业": info['detail'][0]['thesis']['Major'],
                "导师": info['detail'][0]['thesis']['Tutor'],
                "出版日期": info['detail'][0]['thesis']['PublishYear'],
                "MetadataOnlineDate": info['detail'][0]['thesis']['MetadataOnlineDate'],
                "page": info['detail'][0]['thesis']['PageNo'],
                "链接": origin_url + info['detail'][0]['thesis']['Id'],

            }
            json_list.append(json_infos)
        except Exception as e:
            print(e)
            print('AAA所有的json数据:', json_list)

    # return是放在for循环外面的
    return json_list


# 打印最终结果
# print(json_list)

def json_to_excel(json_data):
    """
    读取json数据并存到xlxs中
    json_data: 数据格式为：[{},{},{}]
    """
    json_file = json_data
    print('写入excel的数据:', json_file)
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
    workbook.save('wanfang_data_{}.xls'.format(time.strftime("%Y%m%d%H%M%S", time.localtime())))


if __name__ == '__main__':
    # 调用函数，将函数的返回值赋值给all_article，函数里面有return必须定义个变量来获取return 后面的值
    # all_article_list = get_id_list()
    # all_article_list = get_id_list(q_search_words="语文")
    # all_article_list = get_id_list(q_search_words="人工智能", page_num=50)
    # all_article_list = get_id_list(q_search_words="人工智能", page_num=200)
    all_article_list = get_id_list(q_search_words="python", page_num=2000)
    article_data_json = get_thesis_abstact(all_article_list)
    json_to_excel(article_data_json)  # 这里的函数里面没有return，可以直接调用
    # 跑完一次结果，就重新重名excel文件名，防止再次跑时报错
