::功能：
::使用：直接双击这个bat脚本
::from: lhb,2017-06-20

adb wait-for-device
adb root
adb wait-for-device
adb remount
adb wait-for-device

::adb shell "i=1;while [ i -gt 0 ];do echo 1;dumpsys meminfo; ping -c 6 127.0.0.1; done"

adb shell "i=1;while [ i -gt 0 ];do echo 1;dumpsys meminfo >> /sdcard/Z982_dumpsys60.log; ping -c 60 127.0.0.1; done &"

::adb shell "dumpsys meminfo > /sdcard/Z982_dumpsys.log &"

::adb shell "ping -c 60 127.0.0.1 &"



