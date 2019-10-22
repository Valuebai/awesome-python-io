#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@IDE    ：PyCharm
@Author ：LuckyHuibo
@Date   ：2019/8/26 17:27
@Desc   ：PS, 用python实现p图

1. 简介：通过调用removebg库去除照片中的背景，也可以通过调用PIL库添加背景，这样可以用来实现证件照的背景颜色更换，比如生成白色、蓝色和红色
2. 代码流程：输入-要得到的图片背景处理效果 A-切换为红色背景，B-蓝色，C-白色，D-仅去除背景色，输出-得到对应的图片
3. removebg库简介：基于 Python、Ruby 和深度学习技术开发，通过强大的 AI 人工智能算法实现自动识别出前景主体与背景图，处理时间在5s以内。
用户也可直接到官网上传照片处理，每月最多免费处理 50 张照片如果想生成高清甚至 4K 的图片或者处理更多需要付费，官网如下：https://www.remove.bg。调用接口需要自己注册账号生成一个apikey(在调用接口时必备)
4. PIL库简介：python的第三方图像处理库，本次实验主要用来添加背景颜色,官网如下：http://www.pythonware.com/products/pil/index.htm
通过创建类来去除图片背景和添加背景
=================================================='''
# Requires "requests" to be installed (see python-requests.org)
import requests
import os
from PIL import Image
from removebg import RemoveBg


def remove_offical() -> None:
    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files={'image_file': open('./data/test.jpg', 'rb')},
        data={'size': 'auto'},
        headers={'X-Api-Key': 'UNFDsmLmH6pWpZpqMJA3vwZq'},
    )
    if response.status_code == requests.codes.ok:
        with open('./data/test-no-bg.png', 'wb') as out:
            out.write(response.content)
            print('图片保存成功')
    else:
        print("Error:", response.status_code, response.text)


def remove_one() -> None:
    rmbg = RemoveBg("UNFDsmLmH6pWpZpqMJA3vwZq", "./data/error.log")  # 引号内是你获取的API
    rmbg.remove_background_from_img_file("./data/test.jpg")  # 图片地址


def remove_all() -> None:
    rmbg = RemoveBg("UNFDsmLmH6pWpZpqMJA3vwZq", "./data/error.log")
    path = '%s/picture' % os.getcwd()  # 图片放到程序的同级文件夹 picture 里面
    for pic in os.listdir(path):
        rmbg.remove_background_from_img_file("%s\%s" % (path, pic))


def change2bg() -> None:
    im = Image.open('./data/test-no-bg.png')
    x, y = im.size
    try:
        # 使用red来填充背景
        p = Image.new('RGBA', im.size, (255, 0, 0))  # 附一个RGB的颜色对比连接：http://tool.oschina.net/commons?type=3
        p.paste(im, (0, 0, x, y), im)
        p.save('./data/test-with-bg.png')
        print('pic save success')
    except:
        pass


# 封装成类
class Imgprocess():
    def __init__(self, apikey):
        self.apikey = apikey

    # removebg: 调用RemoveBg接口并生成去除背景的图片，图片名在原图片名称后加_no_bg.png，
    # 如本实验原图片名称certificate.jpg 生成的去背景图片名称certificate.jpg_no_bg.png
    def removebg(self, img):
        rmbg = RemoveBg(self.apikey, "./data/error.log")
        rmbg.remove_background_from_img_file(img)

    # changebg: 调用PIL添加背景颜色
    def changebg(self, img, color):

        color_dict = {"A": (255, 0, 0), "B": (67, 142, 219), "C": (255, 255, 255)}
        im = Image.open(img)
        x, y = im.size
        try:
            p = Image.new('RGBA', im.size, color=color_dict.get(color))
            p.paste(im, (0, 0, x, y), im)
            p.save('{}.png'.format('./data/new' + color))
        except:
            print('changebg err')
            pass


def main():
    option = input("pls input your taget img type, A:red B:bule C:white D:justremovebg: \n")
    print(option)
    newimg = Imgprocess("UNFDsmLmH6pWpZpqMJA3vwZq")
    newimg.removebg("./data/test.jpg")
    if option in list('ABC'):
        print('in')
        newimg.changebg('./data/test.jpg_no_bg.png', option)
        print('out')
    else:
        print('done')
        pass


if __name__ == "__main__":
    # remove_offical()
    # change2bg()
    main()
