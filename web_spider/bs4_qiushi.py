#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@IDE    ：PyCharm
@Author ：LuckyHuibo
@Date   ：2019/9/16 11:12
@Desc   ：单线程爬虫


BeautifulSoup库可以对HTML或XML文件解析，查找到一个或多个标签元素(tag)，并获取每个标签里的文本和属性，这为我们python爬虫从html文本里提取所需要的内容提供了很大的便利。一个BeautifulSoup很好的特性是它接受一个str或byte对象后会对编码自动检测，并把当前文档编码并转换成Unicode编码，这样你就不用担心乱码问题了。

安装和使用只需要使用如下两个命令:

pip install beautifulsoup4

from bs4 import BeautifulSoup

我们还建议你安装lxml HTML解析库，比python自带的解析库html.parser更快。

pip install lxml

安装好BeautifulSoup对象后，你就可以创建soup对象，并开始后面的查找了。

soup = BeautifulSoup(html, "html.parser")
soup = BeautifulSoup(html, "lxml")



BeautifulSoup库的使用方法

BeautifulSoup对一个元素的查找主要有3中方法:

根据标签名直接查找 - 比如soup.title, soup.p，仅适用于查找单个元素

使用find和find_all方法 - 根据标签名和属性对文档遍历查找提取一个或多个元素。

使用select方法 - 根据css样式选择器对文档进行遍历提取一个或多个元素


# 根据tag直接获取元素
soup.p #获取p标签元素对象，只获取第一个
soup.p.name #获取p标签的名字，即'p"
soup.p.string # 获取p标签元素内的文本
soup.p['class'] #获取p标签元素的class属性
soup.p.get('class') #等同于上述案例
soup.a['href'] #获取第一个a元素的href属性


# find_all方法。find方法类似，仅用于提取首个匹配元素
# find_all( name , attrs , recursive , text , **kwargs )
#  name :要查找的标签名（字符串、正则、方法、True）
#  attrs: 标签的属性
#  recursive: 递归
#  text: 查找文本
# **kwargs :其它 键值参数
# 因class是关键字，所以要写成class_="value", 等同于attrs={"class":"value"}
soup.find_all('p')  # 以列表形式返回所有p标签
soup.find_all('p', attrs={"class":"sister"})  # 以列表形式返回所有class属性==sister的p标签
soup.find_all('p', class_="sister")  # 以列表形式返回所有class属性==sister的p标签
soup.find_all(id='link2')  # 返回所有id属性==link2的标签
soup.find_all(re.compile("^b"))  # 使用正则查找标签以b开头的元素
soup.find_all(href=re.compile("elsie")) # 使用正则, 返回所有href属性包含elsie的标签
soup.find_all(id="link1", href=re.compile('elsie'))  # id=link1且href包含elsie的标签


# select方法 - css选择器
# 注意select方法提取的元素均是列表形式，获取文本时注意加index
soup.select('p') # 根据标签名查找所有p元素，等于soup.find_all('p')
soup.select('.sister') # 通过css属性查找class=sister的标签
soup.select('#link1') # 通过id查找所有id=#link1的元素
soup.select('p #link1') # 组合查找id=#link11的p元素
soup.select("head > title") # 查找head标签的子元素title
soup.select('a[class="sister"]') # 查找所有属性为sister的a标签
soup.select('a[href="http://example.com/elsie"]') #查找href=xxx的a标签元素
soup.select('p')[0].get_text() # 获取首个p元素的文本
soup.select('a[href*=".com/el"]')[0].attrs['href'] #获取xxx.com的href
=================================================='''
import requests
from bs4 import BeautifulSoup
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
}

if __name__ == "__main__":

    start = time.time()
    f = open("qiushi01.txt", "a", encoding='utf-8')

    url_list = []
    for i in range(1, 11):
        url_list.append('https://www.qiushibaike.com/8hr/page/{}/'.format(i))

    for url in url_list:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        div_list = soup.select('.article')

        for div in div_list:
            author = div.select('.author')[0].select('h2')[0].get_text()
            content = div.select('.content')[0].get_text()
            f.write(author)
            f.write(content)

    f.close()
    end = time.time()
    print("下载完成. 用时{}秒".format(end - start))
