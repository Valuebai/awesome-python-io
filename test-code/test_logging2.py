# 导入日志模块
import logging
# 使用配置文件设置日志时,需要导入这个模块
import logging.config


class MyLog:
    '''日志类,用于将日志信息写入到.txt文件中'''

    # 载入配置信息,从Logging.cfg
    __loadcfg = logging.config.fileConfig("../config/logging.ini")

    # 获取一个logger对象,通过这个名字参数可以保证在当前程序进程中其它地方获取日志对象时,是同一个日志对象.
    __dblog = logging.getLogger('dblog')

    @staticmethod
    def AddLog(msg, logrefname=None):
        '''// 添加日志
           // 1.msg:日志内容
           // 2.logrefname:通过这个名字获取日志对象,默认是dblog.其它名字要到配置文件里查看
        '''
        if logrefname is not None:
            MyLog.__dblog = logging.getLogger(logrefname)

        MyLog.__dblog.debug(msg)