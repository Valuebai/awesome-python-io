# author:jiushi
# time:2019/7/11
# file:main.py


from gevent import monkey;monkey.patch_all()
from urllib.request import quote
from multiprocessing import Process
import sys
import itertools
import time
import gevent
import requests
import json
import config.config
import re

class Request:
    def __init__(self):
        self.headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
        self.djcs=[]
        self.guol=[]
        self.guanjianzhi=config.config.GUANJIANZI
        self.xcs=[]
        self.url=[]
        self.calc=0
        self.kq=0
    def banner(self):
        write,flush=sys.stdout.write,sys.stdout.flush
        for i in itertools.cycle('|/- \\'):
            if self.kq==30:
                flush()
                break
            data='Start Baidu Search:'+i
            write(data)
            flush()
            time.sleep(.1)
            write('\x08' * len(data))
            self.kq+=1

    def baidu_search(self,url):
        rqt=requests.get(url=url,headers=self.headers)
        data_tools=re.findall("data-tools='.*}'",rqt.text)
        for j in data_tools:
            try:
                data=json.loads(str(j).replace('data-tools=','').replace("'",''))
                urls=requests.get(url=data['url'],headers=self.headers,timeout=3)
                headers=urls.headers
                if 'Server' in headers:
                    server=headers['Server']
                else:
                    server=''

                if 'x-powered-by' in headers:
                    power=headers['x-powered-by']
                else:
                    power=''

                data='url:{} title:{} server:{} x-power-by:{}'.format(urls.url,data['title'],server,power)
                if data not in self.url:
                    self.guol.append(data)
                else:
                    continue
                self.url.append(data)

            except:
                pass

    def echo(self):
        for c in self.guol:
            if self.guanjianzhi !='' and self.guanjianzhi in str(c):
                print(c)
                print(c,file=open('save.txt','a',encoding='utf-8'))
            elif self.guanjianzhi == '':
                print(c)
                print(c,file=open('save.txt','a',encoding='utf-8'))
            else:
                pass

        self.guol.clear()

    def xc(self,rw):
        for r in rw:
            self.xcs.append(gevent.spawn(self.baidu_search,r))

        gevent.joinall(self.xcs)
        self.echo()

    def djc(self):
        for j in range(config.config.PAGE):
            if self.calc==10:
                p=Process(target=self.xc,args=(self.djcs,))
                p.start()
                self.calc=0
                self.djcs.clear()
            url='https://www.baidu.com/s?wd={}&pn={}&oq=1'.format(quote(config.config.SEARCH),j*10)
            self.djcs.append(url)
            self.calc+=1
        if len(self.djcs)>0:
            p = Process(target=self.xc, args=(self.djcs,))
            p.start()

if __name__ == '__main__':
    obj=Request()
    obj.banner()
    obj.djc()