::====================================================
:: 解锁手机
:UnlockPhone
rem 按电源键
adb shell input keyevent 26
ping -n 2 127.1 >nul
rem 解锁
adb shell input keyevent 82
ping -n 2 127.1 >nul
adb shell input swipe 540 1800 540 1800 6000
rem 按home键
adb shell input keyevent 3
ping -n 1 127.1 >nul

:1

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

