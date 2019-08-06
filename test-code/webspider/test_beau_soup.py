#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@IDE    ：PyCharm
@Author ：LuckyHuibo
@Date   ：2019/7/9 11:22
@Desc   ：
=================================================='''


# 爬取testerhome的topic为例，看每天大家都在关注什么。
import requests
from bs4 import BeautifulSoup
import re

s = requests.Session()
username = "安蜀黍"
password = "snake"

login_url = "https://testerhome.com/account/sign_in"
search_url= "https://testerhome.com/topics/last"

result = s.post(url=login_url,data={"user[login]":username,"user[password]":password,"commit":"登陆"})
print(result.status_code)
print(result.cookies)

page = s.get(search_url)

# soup = BeautifulSoup(page.content, 'html5lib')
soup = BeautifulSoup(page.content, 'lxml')

target = soup.select('div.title.media-heading a')
# 网页中的div信息
# < div class ="title media-heading" >
# < a title = "Monkey 测试中，对外放声音的处理方法？"href = "/topics/19802" >
# < span class ="node" > 测试管理 < / span >Monkey 测试中，对外放声音的处理方法？< / a >
#
# < / div >

for title in target:

    find_result = re.search(r'title="(.*?)"',str(title))
    if find_result !=None:
        print(find_result.group(1))


# from bs4 import BeautifulSoup
# import requests
#
# if __name__ == "__main__":
#     get_csdn = requests.get("https://www.csdn.net/")
#     soup = BeautifulSoup(get_csdn.text,"html.parser")
#     titles = soup.select("h3[class='company_name'] a")
#     for title in titles:
#         print(title.get_text(),title.get('href'))