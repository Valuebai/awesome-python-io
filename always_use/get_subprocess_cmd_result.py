#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2020/7/21 16:40
# @Software: PyCharm
# @Author  : https://github.com/Valuebai/
"""
    adb shell dumpsys meminfo com.midea.ai.appliances的数据如下:
    ~~~~~~~~~~~~~~~
    - Native Heap是指c 中malloc出来的堆空间
    - Dalvik Heap是指java中new出来的java堆空间

    Native Heap Pss Total列是2737 也就是native代码中分配了2737KB的空间被占用
    Heap Size列是9728，是指Native堆最大是9728这么多KB
    Heap Alloc列是8103，这里是指在虚拟地址中分配了这么多空间
    Pss Total是指占用了真实的物理内存的空间，而Heap Alloc只是占用的虚拟内存的空间。是分配了空间，没有使用的那部分内存。


    Objects是统计App内部组件对象个数，其中Views、ViewRootImpl以及Activities个数，
    在Activity onDestroy后应该都会回收清零，如果onDestroy调用后这几个对象个数没有清零，就可能发生了内存泄漏。

"""
import re
import time
import subprocess

import pysnooper

# get_subprocess_cmd_result
def get_cmd_result(cmd_string: str) -> str:
    """
    subprocess.Popen:subprocess模块下的Popen方法，实现：
    在执行该程序的服务器上实现shell命令的执行；
    > subprocess.PIPE--->管道机制：一个程序与另一个程序实现通信，例如：cmd命令提示符与屏幕显示，又如：subprocess 与屏幕显示
    > subprocess.POPE,有stdout:标准输出内容扔到管道；
    > stdin：标准输入内容扔到管道；
    > stderr：标准错误输出内容扔到管道；
    通过read将管道里面的内容一部分一部分的获取读出；管道里面的内容，只可读一次，即：丢进管道的内容读一部分少一部分，直到读完；
    stdout, stdin, stderr 的内容扔进不同管道，read不冲突；
    例如：如果一个命令执行出错，那么，stderr扔进管道就有内容，stdout就read空；
    所以，这个就可以判断一个命令是否执行有错；

    Args:
        cmd_string: 执行的命令，例如：adb shell dumpsys meminfo com.midea.ai.appliances

    Returns: 执行后的结果

    """
    cmd_res = ""
    try:
        # 执行命令，得到命令结果cmd_res
        res = subprocess.Popen(cmd_string, shell=True,
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)

        # res是一个对象，需要读取res对象的stderr\strout\stdin的属性，才可获取值
        # 或者用下面这个命令获取结果，(stdout, stderr) = res.communicate()
        err = res.stderr.read()

        # 如果：err有值，即表示命令执行报错，即：stdout就为空
        if err:
            cmd_res = err.decode("utf-8")
            print("err", cmd_res)
        else:
            cmd_res = res.stdout.read()
            # byte 使用 decode 方法就能转变成 str
            cmd_res = cmd_res.decode("utf-8")
    except Exception as e:
        print(e)

    return cmd_res


class MemInfoPackage(object):
    pid = 0
    processName = ""
    datetime = None
    totalPSS = 0
    totalAllocHeap = 0
    javaHeap = 0
    nativeHeap = 0
    system = 0
    mem_total = {}
    mem_app_summary = {}
    mem_objects = {}

    def __init__(self, dump):
        self.dump = dump
        self._parse_main_info()
        self._parse_realtime()
        self.mem_total, self.mem_app_summary, self.mem_objects = self._parse_adb_meminfo_result(self.dump)

    def _parse_main_info(self):
        """
        dumpsys meminfo package 中解析出需要的数据，由于版本变迁，这个数据的结构变化较多，
        比较了不同版本发现这两列数据total pss和Heap Alloc是都有的，而且这两个指标对于展示应用性能指标还是比较有代表性的。
        """
        RE_PROCESS = re.compile(r"\*\* MEMINFO in pid (\d+) \[(\S+)] \*\*")
        RE_TOTAL_PSS = re.compile(r"TOTAL\s+(\d+)")
        RE_JAVA_HEAP = re.compile(r"Java Heap:\s+(\d+)")
        RE_Native_HEAP = re.compile(r"Native Heap:\s+(\d+)")
        RE_System = re.compile(r"System:\s+(\d+)")

        match = RE_PROCESS.search(self.dump)
        if match:
            self.pid = match.group(1)
            self.processName = match.group(2)

        match = RE_TOTAL_PSS.search(self.dump)
        if match:
            self.totalPSS = round(float(match.group(1)) / 1024, 2)  # 处理后的数据单位，MB

        match = RE_JAVA_HEAP.search(self.dump)
        if match:
            self.javaHeap = round(float(match.group(1)) / 1024, 2)  # 处理后的数据单位，MB
            # print(self.javaHeap)

        match = RE_Native_HEAP.search(self.dump)
        if match:
            self.nativeHeap = round(float(match.group(1)) / 1024, 2)  # 处理后的数据单位，MB
            # print(self.nativeHeap)

        match = RE_System.search(self.dump)
        if match:
            self.system = round(float(match.group(1)) / 1024, 2)  # 处理后的数据单位，MB
            # print(self.system)

    def mem_str_list_to_dict(self, source_list, flag_object=None):
        """Convert
        将str列表处理为字典
        """
        res_dict = {}
        for info in source_list:
            info = info.strip()
            info_split = info.split('   ')
            info_split = [i.strip().strip(":") for i in info_split if i != ""]
            # print(info_split)
            if not info_split:
                continue
            if flag_object:
                res_dict[info_split[0]] = info_split[1]

                # 对dumpsys meminfo中的object数据单独进行处理
                if len(info_split) <= 2:
                    continue
                else:
                    res_dict[info_split[2]] = info_split[3]
            else:
                res_dict[info_split[0]] = info_split[1]

        return res_dict

    def _parse_adb_meminfo_result(self, parse_string: str):
        """
        将dumpsys meminfo 结果转为dict 结果，方便处理
        Args:
            parse_string: 执行 dumpsys meminfo命令的结果，如下的获取

            cmdStr = "adb shell dumpsys meminfo com.midea.ai.appliances"
            cmdResult = get_cmd_result(cmdStr)

        Returns: 3个字典

        """
        str_list = re.split(r"\n", parse_string)

        # mem_TOTAL的数据, PSS TOTAL, KB
        # Pss  Private  Private  SwapPss     Heap     Heap     Heap
        # Total    Dirty    Clean    Dirty     Size    Alloc     Free

        mem_total_info = str_list[7:24]
        mem_total = self.mem_str_list_to_dict(mem_total_info)
        print(mem_total)

        # mem_App Summary的数据, Pss(KB)
        mem_app_summary_info = str_list[28:37]
        mem_app_summary = self.mem_str_list_to_dict(mem_app_summary_info)
        print(mem_app_summary)

        # mem_Objects的数据
        mem_objects_info = str_list[39:46]
        mem_objects = self.mem_str_list_to_dict(mem_objects_info, flag_object=True)
        print(mem_objects)

        # SQL, DATABASES这2个数据未处理

        return mem_total, mem_app_summary, mem_objects

    def _parse_realtime(self):
        RE_Realtime = re.compile(r"Realtime: (\d+)")

        match = RE_Realtime.search(self.dump)
        if match:
            self.datetime = match.group(1)
            self.datetime = self.timeStamp_s_convert_time(self.datetime)

    @staticmethod
    def timeStamp_s_convert_time(time_num):
        """
        输入秒级时间戳的时间，转出正常格式的时间
         如: 1595498910 -> 2020-07-23 18:08:30
        param time_num: ms时间戳
        return: 正常格式的时间
        """
        time_array = time.localtime(int(time_num))
        normal_time = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
        # print(normal_time)

        return normal_time


def main():
    """主函数"""
    print("test")

    cmdStr = "adb shell dumpsys meminfo com.midea.ai.appliances"
    cmdResult = get_cmd_result(cmdStr)
    print(cmdResult)
    print("===================")
    a = MemInfoPackage(cmdResult)
    print(a.mem_objects)
    print(a.mem_app_summary)
    print(a.mem_total)
    print(a.pid)
    print(a.processName)
    print(a.datetime)
    print(a.totalPSS)
    print(a.totalAllocHeap)
    print(a.javaHeap)
    print(a.nativeHeap)
    print(a.system)
    print("===================")


if __name__ == "__main__":
    main()
