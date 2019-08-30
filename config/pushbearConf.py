#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@IDE    ：PyCharm
@Author ：LuckyHuibo
@Date   ：2019/8/30 16:51
@Desc   ：
=================================================='''
import requests
from config.get_yaml import _get_yaml

PUSH_BEAR_API_PATH = "https://pushbear.ftqq.com/sub"


def send_push_bear(msg):
    '''
    pushBear微信通知
    :param msg: 微信模板发送的内容
    :return: None
    '''
    conf = _get_yaml()
    if conf["pushbear_conf"]["is_pushbear"] and conf["pushbear_conf"]["send_key"].strip() != "":
        try:
            data = {
                "sendkey": conf["pushbear_conf"]["send_key"].strip(),
                "text": "易行购票成功通知",
                "desp": msg
            }
            send_push_rsp = requests.post(PUSH_BEAR_API_PATH, data=data)
            print('API请求返回的内容: ', send_push_rsp.text)
            if send_push_rsp.status_code is 200:
                print(u"已下发 pushbear 微信通知, 请查收")
            else:
                print(send_push_rsp)
        except Exception as e:
            print(u"pushbear 配置有误 {}".format(e))
    else:
        pass


if __name__ == '__main__':
    send_push_bear(1)
