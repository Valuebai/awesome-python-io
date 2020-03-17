#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@IDE    ：PyCharm
@Author ：Valuebai
@Date   ：2020/1/28 22:11
@Desc   ：run_redis实现消息的发布与订阅


=================================================='''
import sys
import time
import redis

# 全局变量
connection_pool = redis.ConnectionPool(host="localhost", port=6379, db=1)
connection_inst = redis.Redis(connection_pool=connection_pool)
chanel_name = "Valuebai"


def msg_publish():
    """发布消息"""
    while True:
        # 发布消息
        try:
            connection_inst.publish(chanel_name, "hello" + str(time.time()))
        except Exception:
            print("error")
        print(int(time.time()) % 10)
        if int(time.time()) % 10 == 1:
            print("11111111111111111")
            connection_inst.publish(chanel_name, "over")
        time.sleep(1)


def msg_subscribe(_type=0):
    pub = connection_inst.pubsub()
    pub.subscribe(chanel_name)

    if _type == 0:
        # 订阅消息
        for item in pub.listen():
            print("listen on channel: %s" % item)
            if item["type"] == "message" and item["data"].decode('over'):
                print(item["chanel"].decode(), "已停止发布")
                break
    else:
        # 另一种订阅模式
        while True:
            item = pub.parse_response()
            print("Listen on channel: %s " % item)
            if item[0].decode() == "message" and item[2].decode() == "over":
                print(item[1].decode(), "已停止发布")
                break

    # 取消订阅
    pub.unsubscribe()
    return


if __name__ == "__main__":
    # 运行：使用python run_redis实现消息的发布与订阅.py publish 执行
    if sys.argv[1] == "publish":
        print("Hello publish")
        msg_publish()
    else:
        print("Hello msg_subscribe")
        msg_subscribe()
