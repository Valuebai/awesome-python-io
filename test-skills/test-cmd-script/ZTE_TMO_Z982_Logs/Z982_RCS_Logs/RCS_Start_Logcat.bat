::功能：抓取logcat日志并保存到脚本存放的路径
::使用：直接双击这个bat脚本
::from: lhb,2017-05-19

adb wait-for-device
adb root
adb wait-for-device
adb remount
adb wait-for-device


adb logcat -v time >logcat.txt

