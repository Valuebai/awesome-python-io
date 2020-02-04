#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import requests


class RunMain:
    def __init__(self, method, url, data=None):
        self.res = self.run_main(method, url, data)

    def send_get(self, url, data):
        res = requests.get(url, data=data)
        return res.json()

    def send_post(self, url, data):
        res = requests.post(url, data=data)
        return res.json()

    def run_main(self, method, url, data=None):
        res = None
        if method == "GET":
            res = self.send_get(url, data)
        else:
            res = self.send_post(url, data)
        return res


if __name__ == "__main__":
    url = 'http://www.imooc.com/m/web/shizhanapi/loadmorepingjia.html?cart=11'
    data = {
        'cart': '11'
    }
    run = RunMain('GET', url, data)
    print(run.res)
