#author:九世
#time:2019/1/12

import requests
import threading
import re
import time

ids=[]
names=[]
cookies={}
domains=[]

page=input('Please input page:')
ck=input('Please cookie:').strip()

xj=open('doc_host/save_2.txt','w')
xj.close()

for c in ck.split(';'):
    key,value=c.split('=',1)
    cookies[key]=value

url = 'https://butian.360.cn/Reward/pub'

headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'}
def pa(url):
    for p in range(1,int(page.strip())):
        data = {'s': '1','p':'{}'.format(p),'token': ''}
        time.sleep(1)
        rqt=requests.post(url=url,headers=headers,data=data)
        json=rqt.json()
        for z in json['data']['list']:
            print('[a] id:{} name:{}'.format(z['company_id'],z['company_name']))
            ids.append(z['company_id'])
            names.append(z['company_name'])


def ud(urls):
    time.sleep(1)
    rqt2=requests.get(url=urls,headers=headers,cookies=cookies)
    pp=re.findall('<input class="input-xlarge" type="text" name="host" placeholder="请输入厂商域名" value=".*" />',rqt2.text)
    for w in pp:
        sc=str(w).replace('<input class="input-xlarge" type="text" name="host" placeholder="请输入厂商域名" value="','').replace('" />','')
        domains.append(sc)

def sc():
    print(' ')
    print(' ')
    for r in range(0,len(names)):
        print('[a] name:{} domain:{}'.format(names[r],domains[r]))
        print(domains[r],file=open('doc_host/save_2.txt','a'))

if __name__ == '__main__':
    t=threading.Thread(target=pa,args=(url,))
    t.start()
    t.join()
    if len(ids)!=0 or len(cookies)!=0:
        for w in ids:
            url2='https://butian.360.cn/Loo/submit?cid={}'.format(w)
            s=threading.Thread(target=ud,args=(url2,))
            s.start()
            s.join()
    else:
        print('[q] fuck you. exit..')

    sc()