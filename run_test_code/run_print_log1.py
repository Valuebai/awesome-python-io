#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2020/4/10 0:16
# @Software: PyCharm
# @Author  : https://github.com/Valuebai/
"""
    <moudule>.$ {NAME} 
    ~~~~~~~~~~~~~~~

    描述这个文件是干嘛的

    Usage Example
    -------------
    ::
"""
from run_log_config import logger

# from fishbase.fish_logger import set_log_file, logger
# from fishbase.fish_file import get_abs_filename_with_sub_path
#
# log_abs_filename = get_abs_filename_with_sub_path('logs', 'fish_test.log')[1]
#
# set_log_file(log_abs_filename)

if __name__ == "__main__":
    # 在具体需要的地方
    logger.info('INFO日志1111打印...')
    logger.error('ERROR日志1111打印...')

    # # 打印日志保存路径
    # sep = os.sep
    # set_log_path = os.path.abspath(
    #     os.path.join(__file__, f"..{sep}..{sep}logs{sep}"))
    # print('测试Log路径：', set_log_path)

    import time

    while True:
        logger.info('每隔X打印一下111')
        time.sleep(2)


