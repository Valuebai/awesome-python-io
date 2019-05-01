rem 消息app默认放在第三个位置

:1


rem 按home键
adb shell input keyevent 3

rem 返回键
adb shell input keyevent 4
adb shell input keyevent 4
adb shell input keyevent 4

rem tap mms app
adb shell input tap 730 1800 

rem tap first
adb shell input tap 400 400

rem 返回键
adb shell input keyevent 4
ping -n 1 127.1 >nul

rem tap second
adb shell input tap 400 660

rem 返回键
adb shell input keyevent 4
ping -n 1 127.1 >nul

rem tap third
adb shell input tap 400 950

rem 返回键
adb shell input keyevent 4
ping -n 1 127.1 >nul

rem tap four
adb shell input tap 400 1110

rem 返回键
adb shell input keyevent 4
ping -n 1 127.1 >nul

goto 1

