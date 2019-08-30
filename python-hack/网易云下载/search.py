#author:九世
#time:2019/2/11

import requests
from netEaseMusicEncrypt import rand_a, netEase_AES_encrypt,netEase_RSA_encrypt_NoPadding,dictSerialize,aes_encrypt
import webbrowser
import os

musica={}

print('作者：By 九世')
print('网易云音乐搜索')
print('')
user = input('输入你要搜索的歌手或歌曲名称：')
query = {"s": "{}".format(user), "limit": "8", "csrf_token": ""}
key1 = "0CoJUm6Qyw8W8jud"
iv = "0102030405060708"

    # 公钥对，hex16进制编码
module = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68a\
ce615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
publickey = "010001"
    # 序列化查询dict
queryStr = dictSerialize(query)

aaa = aes_encrypt(queryStr, key1, iv)
    # AES加密随机量
key2 = rand_a()
secretStr = netEase_AES_encrypt(queryStr, key1, key2, iv)  # 加密后的params
rsaSec = netEase_RSA_encrypt_NoPadding(key2, publickey, module)  # 加密后的key


class Search:
    def __init__(self,headers,url,data):
        self.headers=headers
        self.url=url
        self.data=data

    def reqt(self):
        try:
            rqt=requests.post(url=self.url,headers=self.headers,data=self.data)
            jsons=rqt.json()

            result=jsons['result']
            songs=result['songs']
            for s in songs:
                print('歌曲名称：{} 下载ID：{}'.format(s['name'],s['id']))
                musica[s['name']]=s['id']

        except Exception as r:
            print('[-] 报错：{}'.format(r))
            return ''
        return 1

    def music(self):
        print('')
        ids=input('请输入歌曲的名称,q退出：')
        if ids in musica.keys():
            print('[+] 自动打开默认浏览器，在线试听')
            value=musica.get(ids)
            url='http://music.163.com/song/media/outer/url?id={}'.format(value)
            webbrowser.open(url)
        elif ids=='q':
            print('退出...')
            exit()
        else:
            print('[-] 找不到歌曲')

    def download(self):
        print('')
        ids = input('请输入歌曲的名称，q是退出：')
        if ids in musica.keys():
            print('[+] 下载中')
            value = musica.get(ids)
            url = 'http://music.163.com/song/media/outer/url?id={}'.format(value)
            rst=requests.get(url=url,headers=self.headers)
            rst2=requests.get(url=rst.url,headers=self.headers)
            xj=open('file/{}.mp3'.format(ids),'wb')
            xj.write(rst2.content)
            xj.close()
            if os.path.exists('file/{}.mp3'.format(ids)):
                print('[+] {}.mp3  下载成功'.format(ids))
            else:
                print('[-] {}.mp3 下载失败'.format(ids))
        elif ids=='q':
            print('退出...')
            exit()
        else:
            print('[-] 找不到歌曲')


if __name__ == '__main__':
    headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36','Content-Type': 'application/x-www-form-urlencoded'}
    url='http://music.163.com/weapi/search/suggest/web?csrf_token='
    data={'params':secretStr,'encSecKey':rsaSec}
    obj=Search(headers=headers,url=url,data=data)
    rs=obj.reqt()
    while True:
        if rs==1:
            print('1.自动打开浏览器试听')
            print('2.下载')
            print('0.退出')
            useq=input('请选择：')
            if useq=='1':
                while True:
                    obj.music()
            elif useq=='2':
                while True:
                    obj.download()
            elif useq=='0':
                print('退出...')
                exit()
            else:
                print('[-] 没有这个选择')