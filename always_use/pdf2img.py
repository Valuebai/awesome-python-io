#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2020/9/26 16:40
# @Software: PyCharm
# @Author  : https://github.com/Valuebai/
"""
    PYTHON 批量将PDF转成图片
    ~~~~~~~~~~~~~~~

    方法：PyMuPDF，其他方法不方便及性能不佳就暂时不考虑
    ①、安装PyMuPDF：pip install PyMuPDF
    ②、转换图片代码：如下
"""
import datetime
import os

import fitz  # fitz就是pip install PyMuPDF，而不是install fitz !!!


def pyMuPDF_fitz_pdf2img(pdf_path, image_path):
    """
    PDF转图片

    Args:
        pdf_path: PDF所在路径，如同级目录下的./xxx/abc.pdf
        image_path: 图片保存的路径（文件夹路径），如同级目录下的./images/

    Returns: 无，打印操作时间

    """
    startTime_pdf2img = datetime.datetime.now()  # 开始时间

    print("PDF转图片中ing...PDF文件名为:{},图片保存路径为：{}".format(pdf_path, image_path))
    pdfDoc = fitz.open(pdf_path)
    # 统计PDF的页码，保存的图片按照images_0-N命名
    for pg in range(pdfDoc.pageCount):
        page = pdfDoc[pg]
        rotate = int(0)
        # 每个尺寸的缩放系数为1.3，这将为我们生成分辨率提高2.6的图像。
        # 此处若是不做设置，默认图片大小为：792X612, dpi=96
        zoom_x = 1.33333333  # (1.33333333-->1056x816)   (2-->1584x1224)
        zoom_y = 1.33333333
        mat = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
        pix = page.getPixmap(matrix=mat, alpha=False)

        if not os.path.exists(image_path):  # 判断存放图片的文件夹是否存在
            os.makedirs(image_path)  # 若图片文件夹不存在就创建

        pix.writePNG(image_path + '/' + 'images_%s.png' % pg)  # 将图片写入指定的文件夹内

    endTime_pdf2img = datetime.datetime.now()  # 结束时间
    # 打印本次PDF转为图片的时间=结束-开始
    print('OK~转换完成，pdf2img的时间={}s，PDF名称:{}\n'.format((endTime_pdf2img - startTime_pdf2img).seconds, pdf_path))


def get_files_by_suffix(path, suffix_name):
    """
    获取指定路径下所有带有.xxx后缀名的文件
    Args:
        path: 指定的文件夹路径
        suffix_name: 固定格式，为 suffix_name=".apk"

    Returns: files of list

    """

    file_num = 0
    res = []
    # 遍历该文件夹
    # 默认先读取当前文件夹里面的文件，如果存在子文件夹，读完当前再遍历子文件夹里面的
    for root, dirs, files in os.walk(path):
        # print(files)
        for file in files:  # 遍历刚获得的文件名files
            filename, extension = os.path.splitext(file)  # 将文件名拆分为文件名与后缀
            if extension == suffix_name:  # 判断该后缀是否为.X文件
                file_num = file_num + 1  # 文件个数标记
                # print(file_num, os.path.join(root,filename)) #输出文件号以及对应的路径加文件名

                # res.append(filename + suffix_name)  # ["a.x","b,x"]格式
                res.append(root + filename + suffix_name)  # ["C:\\a.x"]格式，带绝对路径
    return res


if __name__ == "__main__":
    # # 1、PDF地址
    # pdfPath = '韩国语及汉语拒绝性言语行为比较研究--以中国的韩国语专业本科生为研究对象.pdf'
    # # 2、需要储存图片的目录
    # imagePath = './image'
    # pyMuPDF_fitz_pdf2img(pdfPath, imagePath)

    # TODO 1、2调试单个，3、4操作多个

    # 3、结合get_files_by_suffix函数找到指定路径下所有pdf文件
    all_pdf = get_files_by_suffix(path='./', suffix_name='.pdf')  # 比如找到当前路径
    # 4、遍历所有得到的pdf列表，逐一调用处理PDF转为图片
    for pdf in all_pdf:
        pdf_name = pdf.split('.')[-2]  # 获取pdf对应命名，后续将转换图片存到对应文件夹
        target_path = './'  # 定义存储图片路径，这里默认为同级目录
        pyMuPDF_fitz_pdf2img(pdf, target_path + pdf_name)
