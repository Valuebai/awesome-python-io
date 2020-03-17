#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2020/3/10 18:24
# @Software: PyCharm
# @Author  : https://github.com/Valuebai/
"""
    bert-as-serving的使用
    ~~~~~~~~~~~~~~~

    1. 调用远程Linux部署好的bert-as-serving服务
    2. 使用bert和sklearn的cosine_similarity计算两个词的相似度
"""

from bert_serving.client import BertClient
from sklearn.metrics.pairwise import cosine_similarity


class Encoding(object):
    def __init__(self):
        self.server_ip = "111.229.74.215"  # 调用远程部署好的bert-as-serving服务的机器IP
        # self.server_ip = "localhost"   # 调用本地远程部署好的bert-as-serving服务
        print('1. star BertClient')
        self.bert_client = BertClient(ip=self.server_ip, port=5555, port_out=5556, timeout=20000)
        print('2. end BertClient')

    def encode(self, query: str):
        """
        对输入的a list of strings to a list of vectors
        :param query: str,下面做了处理为a list of strings
        :return: 向量
        """
        tensor = self.bert_client.encode([query])
        return tensor

    def query_similarity(self, query_list):
        """
        查询输入列表的词的相似度
        :param query_list:如["孔子", "珠穆朗玛峰"]
        :return:返回概率大小0-100，概率越大，相似度越高
        """
        tensors = self.bert_client.encode(query_list)
        return cosine_similarity(tensors)[0][1]

    def cosine_two_words(self, base_text: str, compared_text: str):
        """
        用cosine计算2个词之间的相似度
        :param base_text: 想比较的词
        :param compared_text: 被比较的词
        :return: 返回概率大小0-100，概率越大，相似度越高
        """
        tensors = self.bert_client.encode([base_text, compared_text])
        return cosine_similarity(tensors)[0][1]


if __name__ == "__main__":
    ec = Encoding()
    print(ec.encode("孔子").shape)
    print(ec.encode("美国").shape)
    print("孔子和珠穆朗玛峰的向量相似度:", ec.query_similarity(["孔子", "珠穆朗玛峰"]))
    print("中国和孔子的向量相似度:", ec.query_similarity(["中国", "孔子"]))
    print("中国和香港的向量相似度:", ec.query_similarity(["中国", "香港"]))

    print(ec.cosine_two_words('中国', '美国'))
