#author:九世
#time:2019/1/13

import requests
import threading
import re
import os
import time


xj=open('domain_file/domain.txt','w')
xj.close()

def reads(file):
    dk=open('doc_host/{}'.format(file),'r')
    for d in dk.readlines():
        sc="".join(d.split('\n'))
        yield sc

headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'}
def doamin(url,users):
    try:
        print('[a] search {} domain:'.format(users))
        print('')
        print('')
        rqt=requests.get(url=url,headers=headers)
        page=re.search('共.*页',rqt.text)
        pages=str(page.group()).replace('页，到第</span> <input type="text" class="pagewrite" isnum="true" id="pn" /> <span class="col-gray02">页','').replace('共','')
        pages=int(pages)+1
        for p in range(1,int(pages)):
            time.sleep(1)
            urls='http://tool.chinaz.com/subdomain?domain={}&page={}'.format(users,p)
            time.sleep(1)
            rqt = requests.get(url=urls, headers=headers)
            domains=re.findall("window.open(.*)",rqt.text)
            for d in domains:
                pp=re.findall('[a-zA-z]+://[^\s]*',str(d))
                for j in pp:
                    sc=str(j).replace("');",'').replace('"','').replace('http://OTHER','')
                    print(sc.strip())
                    print(sc.strip(),file=open('domain_file/domain.txt','a'))
    except Exception as r:
        if 'NoneType' in str(r):
            print('[q] No subdomain name')
        else:
            print('[q] Error {}'.format(r))
if __name__ == '__main__':
    if os.path.exists('doc_host'):
        print('[a] Found doc_host')
        pl = os.listdir('doc_host')
        for p in pl:
            for b in reads(p):
                url = 'http://tool.chinaz.com/subdomain?domain={}'.format(b)
                t=threading.Thread(target=doamin,args=(url,b))
                t.start()