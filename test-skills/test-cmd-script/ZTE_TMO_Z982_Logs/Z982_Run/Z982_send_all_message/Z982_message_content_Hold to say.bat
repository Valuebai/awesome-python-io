
:1

::=======================================================发送Hold to say
rem 发送文本
adb shell input tap 400 1800
adb shell input text "111"
ping -n 1 127.1 >nul
adb shell input tap 970 980
ping -n 1 127.1 >nul
adb shell input tap 80 1000
ping -n 1 127.1 >nul
adb shell input swipe 320 1350 320 1750
adb shell input tap 970 1800
ping -n 1 127.1 >nul


rem 发送Hold to say
rem 点击录音按钮
ping -n 2 127.1 >nul
adb shell input swipe 560 1800 560 1800 6000
ping -n 3 127.1 >nul

::=======================================================发送Hold to say2
rem 点击录音按钮
adb shell input swipe 560 1800 560 1800 6000
ping -n 3 127.1 >nul

rem reset
adb shell input tap 80 1800
ping -n 1 127.1 >nul
adb shell input swipe 320 1350 320 1750

goto 1

