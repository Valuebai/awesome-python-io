import requests


# 目的：通过排名网站http://alexa.chinaz.com/
#       去查询各个主要交易所的访问人数，并对其进行打印
# 实现：利用requests去请求，获取返回的body数据
def get_exchange_pv():
    myrequest = requests.post("http://alexa.chinaz.com/www.biss.com/")
    print(myrequest)
    pass


if __name__ == '__main__':
    get_exchange_pv()
