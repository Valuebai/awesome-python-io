#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/4/2 14:46
# @Software: PyCharm
# @Author  : https://github.com/Valuebai/
"""
    封装python logging日志，命名为log_config.py
    ~~~~~~~~~~~~~~~

    - 修改日志保存路径，否则使用默认上一层目录的./outputs/logs/
    - 使用：from common.log_config import logger     # common表示本文件放在的文件夹
        logger.info('打印info日志')
        logger.error('打印error日志')
    - 优化加快日志速度，不用之前线程版本
"""
import os
import datetime
import logging
from logging.handlers import TimedRotatingFileHandler


def singleton(cls, *args, **kw):
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return _singleton


@singleton
class GetLogger(object):
    """
    自定义logging，方便使用
    """

    def __init__(self, logs_dir=None, logs_level=logging.INFO):
        self.logs_dir = logs_dir  # 日志路径
        self.now_time = datetime.datetime.now().strftime('%Y-%m-%d')
        self.logs_level = logs_level  # 日志级别
        # 日志的输出格式
        self.log_formatter = logging.Formatter(
            # '%(asctime)s [%(filename)s] [%(funcName)s] [%(levelname)s] [%(lineno)d] %(message)s')
            '%(message)s')

        if logs_dir is None:
            sep = os.sep  # 自动匹配win,mac,linux 下的路径分隔符
            self.logs_dir = os.path.abspath(
                os.path.join(__file__, f"..{sep}..{sep}outputs{sep}logs{sep}"))  # 设置日志保存路径

        # 如果logs文件夹不存在，则创建
        if os.path.exists(self.logs_dir) is False:
            os.mkdir(self.logs_dir)

    def get_logger(self):
        """在logger中添加日志句柄并返回，如果logger已有句柄，则直接返回"""
        # 实例化root日志对象
        log_logger = logging.getLogger('root')

        # 设置日志的输出级别
        log_logger.setLevel(self.logs_level)

        # 创建一个handler，用于输出到cmd窗口控制台
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)  # 设置日志级别
        console_handler.setFormatter(self.log_formatter)  # 设置日志格式
        log_logger.addHandler(console_handler)

        # 建立一个循环文件handler来把日志记录在文件里
        file_handler = TimedRotatingFileHandler(
            filename=self.logs_dir + os.sep + 'app-{}.log'.format(self.now_time),  # 定义日志的存储
            when='MIDNIGHT',
            backupCount=1,  # 最多存放日志的数量
            encoding="UTF-8",  # 使用UTF - 8的编码来写日志
        )
        file_handler.setLevel(logging.DEBUG)  # 设置日志级别
        file_handler.setFormatter(self.log_formatter)  # 设置日志格式

        log_logger.addHandler(file_handler)

        return log_logger


logger = GetLogger().get_logger()

if __name__ == "__main__":
    # 对上面代码进行测试
    logger = GetLogger().get_logger()

    # 在具体需要的地方
    logger.info('INFO日志打印...')
    logger.error('ERROR日志打印...')

    import time

    while True:
        logger.info('每隔X打印一下')
        time.sleep(2)
