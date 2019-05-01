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
ping -n 2 127.1 >nul

rem tap first
adb shell input tap 400 400
ping -n 1 127.1 >nul
rem 返回键
adb shell input keyevent 4
ping -n 2 127.1 >nul

rem tap second
adb shell input tap 400 660
ping -n 1 127.1 >nul
rem 返回键
adb shell input keyevent 4
ping -n 2 127.1 >nul

rem tap third
adb shell input tap 400 950
ping -n 1 127.1 >nul
rem 返回键
adb shell input keyevent 4
ping -n 2 127.1 >nul

rem tap four
adb shell input tap 400 1110
ping -n 1 127.1 >nul
rem 返回键
adb shell input keyevent 4
ping -n 2 127.1 >nul

rem 按home键
adb shell input keyevent 3

rem 返回键
adb shell input keyevent 4
adb shell input keyevent 4
adb shell input keyevent 4

::adb shell input tap 959 1309



adb shell input tap 350 1800 

rem tap 1
adb shell input tap 300 650 
ping -n 2 127.1 >nul
adb shell input keyevent 4
ping -n 1 127.1 >nul
rem tap 1
adb shell input tap 300 650 
ping -n 2 127.1 >nul
adb shell input keyevent 4
ping -n 1 127.1 >nul
rem tap 1
adb shell input tap 300 650 
ping -n 2 127.1 >nul
adb shell input keyevent 4
ping -n 1 127.1 >nul

rem tap 2
adb shell input tap 300 850
ping -n 2 127.1 >nul
adb shell input keyevent 4
ping -n 1 127.1 >nul
rem tap 2
adb shell input tap 300 850
ping -n 2 127.1 >nul
adb shell input keyevent 4
ping -n 1 127.1 >nul
rem tap 2
adb shell input tap 300 850
ping -n 2 127.1 >nul
adb shell input keyevent 4
ping -n 1 127.1 >nul

rem tap 3
adb shell input tap 300 1050
ping -n 2 127.1 >nul
adb shell input keyevent 4
ping -n 1 127.1 >nul
rem tap 3
adb shell input tap 300 1050
ping -n 2 127.1 >nul
adb shell input keyevent 4
ping -n 1 127.1 >nul
rem tap 3
adb shell input tap 300 1050
ping -n 2 127.1 >nul
adb shell input keyevent 4
ping -n 1 127.1 >nul

rem tap 4
adb shell input tap 300 1250
ping -n 2 127.1 >nul
adb shell input keyevent 4
ping -n 1 127.1 >nul
rem tap 4
adb shell input tap 300 1250
ping -n 2 127.1 >nul
adb shell input keyevent 4
ping -n 1 127.1 >nul
rem tap 4
adb shell input tap 300 1250
ping -n 2 127.1 >nul
adb shell input keyevent 4
ping -n 1 127.1 >nul

rem tap 5
adb shell input tap 300 1450
ping -n 2 127.1 >nul
adb shell input keyevent 4
ping -n 1 127.1 >nul
rem tap 5
adb shell input tap 300 1450
ping -n 2 127.1 >nul
adb shell input keyevent 4
ping -n 1 127.1 >nul
rem tap 5
adb shell input tap 300 1450
ping -n 2 127.1 >nul
adb shell input keyevent 4
ping -n 1 127.1 >nul

rem tap 6
adb shell input tap 300 1650
ping -n 2 127.1 >nul
adb shell input keyevent 4
ping -n 1 127.1 >nul
rem tap 6
adb shell input tap 300 1650
ping -n 2 127.1 >nul
adb shell input keyevent 4
ping -n 1 127.1 >nul
rem tap 6
adb shell input tap 300 1650
ping -n 2 127.1 >nul
adb shell input keyevent 4
ping -n 1 127.1 >nul

rem tap 7
adb shell input tap 300 1850
ping -n 2 127.1 >nul
adb shell input keyevent 4
ping -n 1 127.1 >nul
rem tap 7
adb shell input tap 300 1850
ping -n 2 127.1 >nul
adb shell input keyevent 4
ping -n 1 127.1 >nul
rem tap 7
adb shell input tap 300 1850
ping -n 2 127.1 >nul
adb shell input keyevent 4
ping -n 1 127.1 >nul


goto 1

