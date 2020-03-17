#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2020/3/10 18:24
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

from bert_serving.client import BertClient
from sklearn.metrics.pairwise import cosine_similarity


class Encoding(object):
    def __init__(self):
        self.server_ip = "localhost"
        print('1')
        self.bert_client = BertClient(ip=self.server_ip, port=5555, port_out=5556, timeout=10000)
        print('2')

    def encode(self, query):
        tensor = self.bert_client.encode([query])
        return tensor

    def query_similarity(self, query_list):
        tensors = self.bert_client.encode(query_list)
        return cosine_similarity(tensors)[0][1]

    def test1(self, base_text, compared_text):
        tensors = self.bert_client.encode([str(base_text), str(compared_text)])
        return cosine_similarity(tensors)[0][1]

    def test2(self, base_text, compared_text):
        tensors = self.bert_client.encode([base_text,compared_text])
        return cosine_similarity(tensors)[0][1]

if __name__ == "__main__":
    ec = Encoding()
    print(ec.encode("中国"))
    print(ec.encode("美国").shape)
    print("中国和美国的向量相似度:", ec.query_similarity(["中国", "美国"]))
    print("中国和地球的向量相似度:", ec.query_similarity(["中国", "地球"]))
    print("美国和地球的向量相似度:", ec.query_similarity(["美国", "地球"]))

    print(ec.test2('中国','美国'))