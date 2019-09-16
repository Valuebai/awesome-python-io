#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@IDE    ：PyCharm
@Author ：LuckyHuibo
@Date   ：2019/9/16 11:13
@Desc   ：多线程爬虫
=================================================='''

import requests
from bs4 import BeautifulSoup
import time
import threading
from queue import Queue

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
}


class MyThread(threading.Thread):
    def __init__(self, name, queue, file):
        super().__init__()
        self.name = name
        self.queue = queue
        self.file = file

    def run(self):
        print("启动{}".format(self.name))
        while not self.queue.empty():
            try:
                url = self.queue.get()
                response = requests.get(url, headers=headers)
                self.parse(response.text)
            except:
                pass
        print("结束{}".format(self.name))

    def parse(self, html):
        soup = BeautifulSoup(html, "html.parser")
        div_list = soup.select('.article')

        for div in div_list:
            author = div.select('.author')[0].select('h2')[0].get_text()
            content = div.select('.content')[0].get_text()
            self.file.write(author + content)


if __name__ == "__main__":

    start = time.time()
    f = open("qiushit10.txt", "a", encoding='utf-8')

    queue = Queue()
    for i in range(1, 11):
        queue.put('https://www.qiushibaike.com/8hr/page/{}/'.format(i))

    thread1 = MyThread("线程1", queue, f)
    thread2 = MyThread("线程2", queue, f)

    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

    f.close()
    end = time.time()
    print("下载完成. 用时{}秒".format(end - start))
