#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@IDE    ：PyCharm
@Author ：Valuebai
@Date   ：2019/11/18 11:38
@Desc   ：

下一步做什么？

自然是将生成的密码表中的密码遍历，

暴力破解啦！


科普时间：

zipFile模块式Python自带的模块，提供了对zip 文件的创建，读，写，追加，解压以及列出文件列表的操作

解压使用extractll方法extractall(path=None, members=None, pwd=None)

path：指定解压后文件的位置
members:（可选）指定要Zip文件中要解压的文件，这个文件名称必须是通过namelist()方法返回列表的子集
pwd：指定Zip文件的解压密码

那么我们可以利用 zipFile 模块来遍历密码表，

挨个挨个密码尝试，看能不能打开压缩包。

直到成功。

导入zipFile
=================================================='''
import zipfile

def extractFile(zipFile, password):
    try:
        zipFile.extractall(pwd= bytes(password, "utf8" ))
        print("李大伟的压缩包密码是" + password)  #破解成功
    except:
        pass  #失败，就跳过

def main():
    zipFile = zipfile.ZipFile('./input/李大伟.zip')  #需要破解的zip文件
    PwdLists = open('./output/passdict.txt')   #读入所有密码
    for line in PwdLists.readlines():   #挨个挨个的写入密码
        Pwd = line.strip('\n')
        guess = extractFile(zipFile, Pwd)

if __name__ == '__main__':
    # 生成从000000到99999的密码表
    f = open('./output/passdict.txt', 'w', encoding='utf-8')
    for id in range(1000000):
        password = str(id).zfill(6) + '\n'
        f.write(password)
    f.close()
    main()


