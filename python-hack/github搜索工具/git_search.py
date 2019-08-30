# @author:九世
# @time:2019/6/1

from gevent import  monkey;monkey.patch_all()
from aiohttp import ClientSession
from bs4 import  BeautifulSoup
from multiprocessing import Process
import asyncio
import gevent
import requests
import re
import json

aq=[]
x=[]
us=[]

class Search:
    def version(self):
        ver={}
        ver['banner'] ='''
             __                                                  __         
          __/\ \__                                              /\ \        
      __ /\_\ \ ,_\            ____     __     __     _ __   ___\ \ \___    
    /'_ `\/\ \ \ \/           /',__\  /'__`\ /'__`\  /\`'__\/'___\ \  _ `\  
   /\ \L\ \ \ \ \ \_         /\__, `\/\  __//\ \L\.\_\ \ \//\ \__/\ \ \ \ \ 
   \ \____ \ \_\ \__\        \/\____/\ \____\ \__/.\_|| \_|| \____|| \_\ \_|
    \/___L\ \/_/\/__/  _______\/___/  \/____/\/__/\/_/ \/_/ \/____/ \/_/\/_/
      /\____/         /\______\                                             
      \_/__/          \/______/                    
        '''
        ver['version']='0.1'
        ver['author']='九世'
        ver['github']='https://github.com/422926799'
        ver['waring']='[!] 由于个别人不喜欢写README.md或者github上显示不出来导致README为空，抓取的时候抓不到。只能添加空白凑和着了，所以会有README混乱例子搜索:Metasploit即可体会到'
        v_l=list(ver.keys())
        v_v=list(ver.values())
        for v in range(0,len(v_l)):
            print('{}:{}'.format(v_l[v],v_v[v]))

    async def search(self,id):
        print(' ')
        search_sessus={}
        if id==1:
            print('[+] 单个搜索')
            headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
            query=input('搜索的内容 （输入set进入高级搜索模式）>')
            if query=='set':
                setting={'1':'星星大于指定数量','2':'搜索某个时间段之后创建出来的代码','3':'获取星星数目介于某段区域','4':'输出高级搜索语法帮助，用户自定义混搭'}
                hd=['星星大于指定数量:stars>200:','搜索某个时间段之后创建出来的代码:ios created:"2019-01-02 ..* "','获取星星数目介于某段区域:stars:"10..100"','按照文件搜索:android in:file','按照路径检索:andrioid in:path','按照语言检索:android language:java','按照文件大小:android size:>100','按照后缀名检索:android extention:css','按照是否被fork过:android fork:true','按照地域检索（这个猎头和hr应该用得着）:android location:beijing']
                s_v={'1':'stars:>{}','2':'{} created:"{} ..* "','3':'{} stars:"{}..{} "','4':hd}
                f_key=list(setting.keys())
                f_value=list(setting.values())
                for z in range(0,len(f_key)):
                    print('{}:{}'.format(f_key[z],f_value[z]))

                xw=input('>')
                if xw=='1':
                    ts=input('星星的数量>')
                    query=s_v[xw].format(ts)

                elif xw=='2':
                    ts=input('什么时间创建的代码 (输入例如:2019-01-02)>')
                    gjz=input('关键字>')
                    query=s_v[xw].format(gjz,ts)

                elif xw=='3':
                    gjz=input('关键字>')
                    ks=input('星星最小数量>')
                    kd=input('星星最大数量>')
                    query = s_v[xw].format(gjz,ks,kd)

                elif xw=='4':
                    for h in hd:
                        print(h)

                    query=input('自定义构建语法>')

            print(query)
            pags=input('页数>')
            url='https://github.com/search?q={}&type=Repositories'.format(query)
            async with ClientSession() as rqt:
                async with rqt.get(url=url,headers=headers) as respone:
                    text=await respone.text()
                    sl=re.findall('.*? repository results',text)
                    if len(sl)==0:
                        search_sessus['搜索数量结果']=0
                        print('[-] 没有你要找的结果')
                        exit()
                    else:
                        search_sessus['搜索结果数量']=str(sl[0]).lstrip()
                        page=re.findall('[/]search[?]p=[0-9]{1,}',text)
                        lt=[]
                        for p in page:
                            px=re.findall('[0-9]{1,}',str(p))
                            lt.append(px[0])
                        lt.sort()
                        if len(lt)==0:
                            bat=0
                        else:
                            bat=lt[0]
                        search_sessus['总页数']=bat
                        lt.clear()

            s_k=list(search_sessus.keys())
            s_v=list(search_sessus.values())
            for s in range(0,len(s_k)):
                print('[+] {}:{}'.format(s_k[s],s_v[s]))

            if  int(pags)>int(search_sessus['总页数']):
                pags=search_sessus['总页数']
                print('[!] 要搜索的页数大于总页数，自动设置总页数为要搜索的页数')

            calc=0
            lt=[]
            if int(pags)==0: #如果只有一页的话，匹配页数的正则是匹配不到的只能改变了
                url = 'https://github.com/search?p={}&q={}&type=Repositories'.format(pags, query)
                lt.append(url)
                p = Process(target=self.xc, args=(lt,))
                p.start()
            else:
                for u in range(1,int(pags)+1):
                    if calc=='50':
                        p=Process(target=self.xc,args=(lt,))
                        p.start()
                        calc=0
                        lt.clear()
                    url='https://github.com/search?p={}&q={}&type=Repositories'.format(u,query)
                    lt.append(url)
                    calc+=0

                if len(lt)>0:
                    p = Process(target=self.xc, args=(lt,))
                    p.start()

    def xc(self,op,):
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
        reg=[]
        for o in op:
            reg.append(gevent.spawn(self.searcs,o,headers,))

        gevent.joinall(reg)

    def searcs(self,url,headers,):
        rqt=requests.get(url=url,headers=headers)
        red=BeautifulSoup(rqt.text,'html.parser')
        for h in red.find_all('h3'):
            jsons=re.findall('{.*}',str(h))
            if len(jsons)>0:
                for j in jsons:
                    jsons=json.loads(j)
                    git_url=jsons['payload']['result']['url']
                    us.append(git_url)
                    author=re.findall('github.com/.*[/]',git_url)
                    for a in author:
                        aq.append(str(a).replace('github.com/','').replace('/',''))

        readme=re.findall(' <p class="col-.*">\s.*',rqt.text)
        for r in readme:
            rs=BeautifulSoup(str(r),'html.parser')
            x.append(str(rs.get_text()).strip().lstrip().rstrip())

        while len(x)!=len(us):
            x.append('')
        for c in range(0,len(us)):
            print('作者:{} 仓库地址:{} 简介:{}'.format(aq[c],us[c],x[c]))


    async def main(self):
        suomin=['1.单项搜索']
        for s in suomin:
            print(s)
        xw=input('git_search>')
        if xw=='1':
            rw=asyncio.ensure_future(self.search(int(xw)))
        taks=[rw]
        await asyncio.wait(taks)
if __name__ == '__main__':
    obj=Search()
    obj.version()
    asyncio.run(obj.main())