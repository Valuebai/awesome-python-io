rem 发送各种内容的消息

:1
::=======================================================输入当前日期和时间发送
rem 输入当前日期和时间发送
adb shell input tap 400 1800
adb shell input text "1"
ping -n 1 127.1 >nul
adb shell input tap 970 980
ping -n 1 127.1 >nul
adb shell input tap 80 1000
ping -n 1 127.1 >nul
adb shell input swipe 320 1350 320 1750

goto 1

