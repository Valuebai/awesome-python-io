::功能：录制视频存放在手机中
::使用：直接双击这个bat脚本
::from: lhb,2017-05-19

adb wait-for-device
adb root
adb wait-for-device
adb remount
adb wait-for-device

::执行录屏命令
adb  shell screenrecord --size 480x640 --bit-rate 1000000  /sdcard/zdemo.mp4

