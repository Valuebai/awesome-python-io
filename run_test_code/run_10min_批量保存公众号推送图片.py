#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@IDE    ：PyCharm
@Author ：Valuebai
@Date   ：2019/11/18 11:25
@Desc   ：
有时候我们浏览公众号的时候会看到一系列中意的图片，本例子就教大家如何批量保存公众号推送的图片。
=================================================='''

import requests
from lxml import etree
import pandas as pd
import re

url = 'https://mp.weixin.qq.com/s?__biz=MzI3NTg3Nzc5NQ==&mid=2247483696&idx=1&sn=54e7b07baa4c74262845cc0ea22046f1&chksm=eb7f5bfcdc08d2eab27536dade3166ea3d430f3bbca163b8a54bd63f37efd49e91e21656116b&token=1134416884&lang=zh_CN#rd'
with requests.get(url) as req:
    content = req.content
    html = etree.HTML(content)

# 利用xpath获取所有图片的子节点img的属性data-src
a = html.xpath('//*[@id="js_content"]/p/img/@data-src')

# 注意每个图片的格式不一样，为了获得最好的效果，可以根据不同图片格式保存不同的文件后缀名：
for i, path in enumerate(a):
    img_format = re.search('wx_fmt=([a-z]{3,4})', path).group(1)
    imgname = str(i) + '.' + img_format
    with requests.get(path) as img_req:
        img_content = img_req.content

    output_root = './output/'
    with open(output_root+imgname, 'wb') as f:
        f.write(img_content)

    print('第{0}张图片{1}保存成功...'.format(i,output_root+imgname))