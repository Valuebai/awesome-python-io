rem 发送各种内容的消息


:1
::=======================================================录制音频并发送1
rem tap attach button
adb shell input tap 80 1800
ping -n 1 127.1 >nul
adb shell input tap 325 1850
ping -n 1 127.1 >nul
adb shell input tap 80 1000
ping -n 1 127.1 >nul

rem tap file option
adb shell input tap 750 1850
ping -n 1 127.1 >nul

rem 点击录制按钮
adb shell input tap 650 1250
ping -n 1 127.1 >nul
adb shell input tap 540 1735
ping -n 5 127.1 >nul
adb shell input tap 900 1740
ping -n 3 127.1 >nul


rem tap send button
adb shell input tap 970 980
adb shell input tap 970 1800
ping -n 1 127.1 >nul

rem reset
adb shell input tap 80 1000
ping -n 1 127.1 >nul
adb shell input swipe 320 1350 320 1750
ping -n 1 127.1 >nul

goto 1



