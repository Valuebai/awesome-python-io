#author:九世
#time:2019/1/13

import requests
import threading
import os

xj=open('doc_host/save2host.txt','w')
xj2=open('doc_text/save2text.txt','w')
xj3=open('doc_name/save2name.txt','w')
xj.close()

cookie=input('Please cookie:').strip()
cookies={}
host=[]
text=[]
names=[]

for k in cookie.split(';'):
    key,value=k.split('=',1)
    cookies[key]=value

headers={
'Host':'butian.360.cn',
'Connection': 'close',
'Content-Length': '21',
'Accept': 'application/json, text/javascript, */*; q=0.01',
'Origin': 'https://butian.360.cn',
'X-Requested-With': 'XMLHttpRequest',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Referer': 'https://butian.360.cn/Reward/plan',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.8',
}
data = {'s': '3', 'p': '1', 'sort': '1', 'token': ''}
def pac(url):
    rqt=requests.post(url=url,headers=headers,data=data,cookies=cookies)
    jn=rqt.json()
    lj=jn['data']['list']
    for l in lj:
        host.append(l['host'])
        text.append(l['test_range'])
        names.append(l['company_name'])

def shuchu():
    for w in range(0,len(names)):
        print('[a] name:{}'.format(names[w]))
        print(names[w],file=open('doc_name/save2name.txt','a'))
        print('-'*36)
        print('[a] host:{}'.format(host[w]))
        print(host[w],file=open('doc_host/save2host.txt','a'))
        print('-'*36)
        print('[a] text:{}'.format(text[w]))
        print(text[w],file=open('doc_text/save2text.txt','a'))
        print('-'*36)
        print('')
        print('')
        print('')

if __name__ == '__main__':
    url='https://butian.360.cn/Reward/corps'
    t=threading.Thread(target=pac,args=(url,))
    t.start()
    t.join()
    shuchu()