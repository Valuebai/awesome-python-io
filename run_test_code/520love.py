#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2020/2/14 9:14
# @Software: PyCharm
# @Author  : https://github.com/Valuebai/
"""
    <moudule>.name
    ~~~~~~~~~~~~~~~

    描述这个文件是干嘛的

    Usage Example
    -------------
    ::
"""

from PIL import Image, ImageDraw, ImageFont

font_size = 7
text = "520.鱼最可爱.1314"
img_path = "./input/微信图片_20200214092902.jpg"

img_raw = Image.open(img_path)
img_array = img_raw.load()

img_new = Image.new("RGB", img_raw.size, (0, 0, 0))
draw = ImageDraw.Draw(img_new)
font = ImageFont.truetype('C:/Windows/fonts/Dengl.ttf', font_size)

def character_generator(text):
    while True:
        for i in range(len(text)):
            yield text[i]

ch_gen = character_generator(text)

for y in range(0, img_raw.size[1], font_size):
    for x in range(0, img_raw.size[0], font_size):
        draw.text((x, y), next(ch_gen), font=font, fill=img_array[x, y], direction=None)

img_new.convert('RGB').save("./output/520loveyou.jpeg")