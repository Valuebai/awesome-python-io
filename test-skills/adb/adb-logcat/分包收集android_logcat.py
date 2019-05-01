"""
python分包写入文件，写入固定字节内容，当包达到指定大小时继续写入新文件
第6行通过 for 循环控制生成 .log 文件的数量

第8行，如果该文件存在时先进行清空，然后再进行写入操作

第13行，将文件大小的单位转为MB

第14行，如果文件大小超过1MB时，跳出当前循环，重新进入for 循环中生成一个新文件
"""
# -*- coding:utf-8 -*-
import os
import sys
import time

for i in range(3):
    fp = r'D:\WorkSpace3\performance\run_log\run' + str(i) + '.log'
    with open(fp, 'w', encoding='utf-8') as fn:  # 如果文件存在时，先进行清空，实现对一个文件重复写
        pass
    while True:
        with open(fp, 'a+', encoding='utf-8') as fn:
            fn.write(time.strftime("%Y-%m-%d %H:%M:%S") + " hello world!\n")
        fs = round(os.path.getsize(fp) / float(1024 * 1024), 2)  # 将文件大小的单位转换成MB
        if fs >= 1:  # 如果文件大小超过1MB时，重新写入另一个文件
            break

"""
分包收集 android 运行的 logcat 日志
"""
# -*- coding:utf-8 -*-
import os
import time
from common import Common

comm = Common()

cmd = r'adb logcat -v time -b main -b radio -b system >'
for i in range(3):
    fn = r'../run_log/logcat' + str(i) + '.log'
    os.popen(cmd + fn)
    pid = comm.getAppPid('logcat')
    while True:
        fs = round(os.path.getsize(fn) / float(1024 * 1024), 2)
        time.sleep(1)
        print("当前文件的大小为：%s MB" % fs)
        if fs >= 1:
            kill_cmd = 'adb shell kill ' + pid
            os.popen(kill_cmd)
            break
    print("当前的日志文件为：%s" % fn)
