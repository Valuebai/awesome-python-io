import json
from Crypto.Cipher import AES
import base64
from Crypto.PublicKey import RSA
import codecs
import random
#PKCS_7方式进行补位
def pad(data:bytes,blockbytes:int=16):
    """
    data:需要补位的bytes
    blockbytes:块bytes大小
    """
    _data = data
    #判断是否是字符串，如果是则按utf8编码为bytes
    if isinstance(_data,str):
        _data = _data.encode('utf8')
    length = len(_data)
    pad_length = blockbytes - length % blockbytes
    padding = (chr(pad_length)*pad_length).encode('utf8')
    _data += padding
    return _data

#dict序列化
def dictSerialize(data:dict):
    if not isinstance(data,dict):
        _data = dict(data)
    _data = data
    _data = json.dumps(_data,ensure_ascii=False)
    return _data

#生成随机值用于AES第二阶段加密的密钥
def rand_a(a=16):
    b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    c = ""
    length = len(b)
    for _ in range(a):
        c += b[int(random.random()*length)]
    return c

#aes加密
def aes_encrypt(data,key,iv,mode=AES.MODE_CBC):
    """
    data:明文
    key:密钥
    iv:偏移量
    mode:模式，默认为CBC模式
    """
    encryptor=AES.new(key.encode('utf-8'),mode=mode,IV=iv.encode('utf-8'))
    #补位操作
    _data = pad(data,16)
    encrypted_data = encryptor.encrypt(_data)
    return base64.b64encode(encrypted_data)

#aes解密
def aes_decrypt(data,key,iv,mode=AES.MODE_CBC):
    """
    data:密文
    key:密钥
    iv:偏移量
    mode:模式，默认为CBC模式
    """
    decryptor = AES.new(key,mode=mode,IV=iv)
    return decryptor.decrypt(data)

def netEase_AES_encrypt(data,key1,key2,iv,mode=AES.MODE_CBC):
    """
    data:明文
    key1:第一阶段密钥
    key2:第二阶段密钥
    iv:偏移量
    mode:模式，默认为CBC模式
    """
    if isinstance(data,dict):
        _data = dictSerialize(data)
    _data = str(data)
    _encryptedData = aes_encrypt(_data,key1,iv,mode)
    _encryptedData = aes_encrypt(_encryptedData,key2,iv,mode)
    return _encryptedData.decode('utf8')

def netEase_AES_decryot(data,key1,key2,iv,mode=AES.MODE_CBC):
    """
    data:密文
    key1:第一阶段加密函数
    key2:第二阶段加密函数
    iv:偏移量
    mode:模式，默认为CBC模式
    """
    _data = base64.b64decode(data)
    plaintext = aes_decrypt(_data,key2,iv,mode)
    plaintext = base64.b64decode(plaintext)
    plaintext = aes_decrypt(plaintext,key1,iv,mode)
    plaintext = plaintext.decode('utf8')
    return plaintext


def netEase_RSA_encrypt_NoPadding(data:str,publickey:str,module:str):
    """
    RSA采用Nopadding方式，即明文先倒排，再在前面补0
    data:明文
    publickey:公钥
    module:RSA中两个大质数的乘积
    """
    #网易云云音乐中js加密采用的算法中的参数是以16进制来操作的
    _publickey = int(publickey,16)
    _module = int(module,16)
    _data = data[::-1]
    _data = int(codecs.encode(_data.encode('utf8'),'hex'),16)
    #RSA加密过程
    rs = _data**_publickey%_module
    #返回16进制解码，前面补0补足256位的字符串
    return format(rs,'x').zfill(256)


