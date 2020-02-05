#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@IDE    ：PyCharm
@Author ：Valuebai
@Date   ：2019/9/3 10:44
@Desc   ：封装log日志，方便使用，注意修改log路径

@使用：from common.logConf import logger

# 在具体需要的地方
logger.info('开始连接数据库...')
logger.error(e)

注意：flask 有自带的log，导入自创建的文件后会覆盖flask自带的
=================================================='''
import os, sys
import time
import logging.config
from logging.handlers import TimedRotatingFileHandler


class GetLogger:
    sep = os.sep  # 自动匹配win,mac,linux 下的路径分隔符
    set_log_path = os.path.abspath(os.path.join(__file__, f"..{sep}..{sep}output{sep}logs{sep}"))  # 设置日志保存路径

    def __init__(self, logs_dir=set_log_path, logs_level=logging.INFO):

        # 如果logs文件夹不存在，则创建
        self.logs_dir = logs_dir
        if not os.path.exists(self.logs_dir):
            os.mkdir(self.logs_dir)

        # 实例化root日志对象
        self.logger = logging.getLogger('root')

        # 设置日志的输出级别
        self.logger.setLevel(logs_level)

        # 获取今天的日期
        self.getTodayDateStr = time.strftime("%Y-%m-%d", time.localtime(time.time()))

        # 定义日志的输出格式
        self.log_formatter = logging.Formatter(
            "[%(asctime)s][%(pathname)s: line(%(lineno)d)][%(levelname)s][thread:%(thread)d] - %(message)s")

    def get_logger(self):
        """在logger中添加日志句柄并返回，如果logger已有句柄，则直接返回"""
        if not self.logger.handlers:  # 避免重复日志
            # 创建一个handler，用于输出到cmd窗口控制台
            console_handler = logging.StreamHandler()

            console_handler.setLevel(logging.INFO)  # 设置日志级别
            console_handler.setFormatter(self.log_formatter)  # 设置日志格式
            self.logger.addHandler(console_handler)

            # 建立一个循环文件handler来把日志记录在文件里
            file_handler = TimedRotatingFileHandler(
                filename=self.logs_dir + r'/log_' + self.getTodayDateStr + r".log",  # 定义日志的存储
                when="MIDNIGHT",  # 按照日期进行切分when = D： 表示按天进行切分,or self.when == 'MIDNIGHT'
                interval=1,  # interval = 1： 每天都切分。 比如interval = 2就表示两天切分一下。
                backupCount=30,  # 最多存放日志的数量
                encoding="UTF-8",  # 使用UTF - 8的编码来写日志
                delay=False,
                utc=True  # utc = True: 使用UTC + 0的时间来记录 （一般docker镜像默认也是UTC + 0）
            )

            file_handler.setLevel(logging.DEBUG)  # 设置日志级别
            file_handler.setFormatter(self.log_formatter)  # 设置日志格式
            self.logger.addHandler(file_handler)

        return self.logger


logger = GetLogger().get_logger()

if __name__ == "__main__":
    # 对上面代码进行测试
    logger = GetLogger().get_logger()

    # 在具体需要的地方
    logger.info('INFO日志打印...')
    logger.error('ERROR日志打印...')

    sep = os.sep
    root_path = os.path.abspath(os.path.join(__file__, f"..{sep}..{sep}output{sep}log{sep}"))
    # sys.path.append(root_path)
    print('测试Log路径：', root_path)
