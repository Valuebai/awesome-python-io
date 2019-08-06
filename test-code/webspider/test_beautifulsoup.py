#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@IDE    ：PyCharm
@Author ：LuckyHuibo
@Date   ：2019/7/8 18:38
@Desc   ：根据beautiful soup官方文档进行代码测试
=================================================='''
from bs4 import BeautifulSoup
import re

if __name__ == "__main__":
    html_doc = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title"><b>The Dormouse's story</b></p>

    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>

    <p class="story">...</p>
    """

    soup = BeautifulSoup(html_doc, 'html.parser')
    # print(soup.prettify())
    print(soup.title)
    print(soup.find_all('b'))
    print(soup.find_all(re.compile('p')))
    print('='*20)
    for tag in soup.find_all(re.compile('t')):
        print(tag.name)