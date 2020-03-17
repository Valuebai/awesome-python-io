#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@IDE    ：PyCharm
@Author ：Valuebai
@Date   ：2019/12/1 11:56
@Desc   ：
=================================================='''
import hashlib
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

read_wc = pd.read_excel(r'./input/test_wordcloud.xls')
print(read_wc.head())

# 绘制词频云图
words = ','.join(x for x in read_wc['city'] if x != [])  # 筛选出非空列表值
wc = WordCloud(
    background_color='green',  # 设置背景颜色为绿色
    max_words=100,  # 显示最大词数
    font_path='./input/SourceHanSerifCN-Regular.otf',  # 设置字体，显示中中文
    min_font_size=5,
    max_font_size=100,
    width=500  # 图幅宽度
)

x = wc.generate(words)
x.to_file('./output/wordcloud.png')  # 保存，只保存1张的
# 隐藏x轴和y轴，在pycharm需要plt显示出来
plt.axis("off")
plt.imshow(wc, interpolation="bilinear")
plt.show()

# 想要学习详情的：在我的地址https://github.com/Valuebai/learn-NLP-luhuibo/blob/master/lesson-04-NLP-basic-word2vec/wiki_5_test_result.py