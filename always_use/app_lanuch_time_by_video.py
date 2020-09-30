#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# import cv2

# vc = cv2.VideoCapture(r'/Users/user/Desktop/IMG_0162.MP4')  # 读入视频文件，命名cv
# n = 1  # 计数

# if vc.isOpened():  # 判断是否正常打开
#     rval, frame = vc.read()
# else:
#     rval = False

# timeF = 1  # 视频帧计数间隔频率

# i = 0
# while rval:  # 循环读取视频帧
#     rval, frame = vc.read()
#     if (n % timeF == 0):  # 每隔timeF帧进行存储操作
#         i += 1
#         print(i)
#         cv2.imwrite(r'/Users/user/iot/dev/1/{}.jpg'.format(i), frame)  # 存储为图像
#     n = n + 1
#     cv2.waitKey(1)

# vc.release()


import os
import sys
import cv2

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# BASE_DIR='E:/脚本/video/'

class FrameBlock():
    """docstring for FrameBlock"""

    def __init__(self):
        super(FrameBlock, self).__init__()

    def save_img(self, path):
        print("BASE_DIR:", BASE_DIR)
        video_path = BASE_DIR + path
        print("=========", video_path)
        videos = os.listdir(video_path)
        for video_name in videos:
            file_name = video_name.split('.')[0]
            folder_name = video_path + file_name
            os.makedirs(folder_name, exist_ok=True)
            vc = cv2.VideoCapture(video_path + video_name)  # 读入视频文件
            (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
            if int(major_ver) < 3:
                fps = vc.get(cv2.cv.CV_CAP_PROP_FPS)
                if fps != 0:
                    print(folder_name,
                          "Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(1.0 / fps))
            else:
                fps = vc.get(cv2.CAP_PROP_FPS)
                if fps != 0:
                    print(folder_name, "Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(1.0 / fps))

            c = 0
            rval = vc.isOpened()

            while rval:  # 循环读取视频帧

                c = c + 1
                rval, frame = vc.read()
                pic_path = folder_name + '/'
                if rval:
                    # print("=======", pic_path + file_name + '_' + str(c) + '.jpg',frame)
                    cv2.imwrite(pic_path + file_name + '_' + str(c) + '.jpg', frame)  # 存储为图像,保存名为 文件夹名_数字（第几个文件）.jpg
                    cv2.waitKey(1)
                else:
                    break
            vc.release()
            # print('save_success')
            # print(folder_name)


def lanuch_android_app():
    """
    开始录制安卓屏幕视频后，启动该脚本
    注意：本脚本适用于电脑只连接一台安卓手机且安装好美居app

    Android单次启动美居的adb命令：
        adb shell am start -W com.midea.ai.appliances/com.midea.meiju.main.MainActivity
    Android单次启动美居的adb命令（-S 启动前会杀死app）：
        adb shell am start -W -S com.midea.ai.appliances/com.midea.meiju.main.MainActivity
    Android多次启动美居的adb命令（中间不停）：
        adb shell am start -R 5 -W -S com.midea.ai.appliances/com.midea.meiju.main.MainActivity
    """
    import subprocess
    import time

    # 重复启动app 20次，执行完在把视频导出，结合上面的FrameBlock分析
    for i in range(0, 20):
        lanuch_app_cmd = "adb shell am start -W com.midea.ai.appliances/com.midea.meiju.main.MainActivity"
        lanuch_kill_app_cmd = "adb shell am start -W -S com.midea.ai.appliances/com.midea.meiju.main.MainActivity"
        stop_app_cmd = "adb shell am force-stop com.midea.ai.appliances"
        subprocess.call(lanuch_app_cmd, shell=True)
        time.sleep(3)
        subprocess.call(stop_app_cmd, shell=True)
        time.sleep(5)


if __name__ == '__main__':
    # 路径不包含中文
    # 这块注释掉的是手动输入参数
    # arg = sys.argv
    # if len(arg) < 2:
    #     print('you must input file dir')
    # else:
    #     frame = FrameBlock()
    #     frame.save_img(arg[1])

    # 测试结果：
    # 1. 查看图片，开始和结束的；
    # 2. 结束图片_num2 - 开始图片_num1 = N 
    # 3. 最终加载时间= N*16.66ms

    frame = FrameBlock()
    frame.save_img('./video/')  # 默认当前video.py脚本路径，需要将视频放到video里面

    # lanuch_android_app()
