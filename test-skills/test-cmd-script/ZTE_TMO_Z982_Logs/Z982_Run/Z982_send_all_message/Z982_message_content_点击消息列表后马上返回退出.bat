adb wait-for-device
adb root
adb wait-for-device
adb remount
adb wait-for-device


:1

::===========================================
rem 类初始化，返回home并进入消息或退回

rem 按home键
adb shell input keyevent 3
ping -n 1 127.1 >nul
rem tap mms app
adb shell input tap 730 1800
ping -n 1 127.1 >nul

rem tap first
adb shell input tap 400 400
ping -n 1 127.1 >nul
rem 返回键
adb shell input keyevent 4

rem tap second
adb shell input tap 400 660
ping -n 1 127.1 >nul
rem 返回键
adb shell input keyevent 4

rem tap third
adb shell input tap 400 950
ping -n 1 127.1 >nul
rem 返回键
adb shell input keyevent 4

rem tap four
adb shell input tap 400 1110
ping -n 1 127.1 >nul
rem 返回键
adb shell input keyevent 4


goto 1

