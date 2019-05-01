::功能：
::使用：直接双击这个bat脚本
::from: lhb,2017-06-20

adb wait-for-device
adb root
adb wait-for-device
adb remount
adb wait-for-device

adb shell "top -m 30 -s cpu -d 60 > /sdcard/Z982_cpu.log &"

pause