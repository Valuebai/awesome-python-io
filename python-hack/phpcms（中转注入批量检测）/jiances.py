import requests
import os
print('[!]请确保你把生成的php文件夹拷贝到你的php环境目录之下，然后请输入目录的路径。我将获取路径下所有的文件进行检测')
user=input('path:')

ok=open('sqllin.txt','w')
ok.close()

xj=open('save.txt','w')
xj.close()

def exploitsqllin():
    cs=os.listdir(user)
    headers={'user-gent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    for s in cs:
        print(s,file=open('save.txt','a'))

    dk=open('save.txt','r')
    for r in dk.readlines():
        wed="".join(r.split('\n'))
        urls='http://127.0.0.1/scv/{}?id=1'.format(wed)
        rq=requests.get(url=urls,headers=headers)
        if '0' in rq.text:
            print('[-]Not bug {}'.format(rq.url))
        elif '-1' in rq.text:
            print('[+]Bug url {}'.format(rq.url))
            print('[+]Bug url {}'.format(rq.url),file=open('sqllin.txt','a'))
exploitsqllin()
