::功能：
::使用：直接双击这个bat脚本
::from: lhb,2017-06-20

adb wait-for-device
adb root
adb wait-for-device
adb remount
adb wait-for-device

adb pull /sdcard/Z982_dumpsys60.log

pause