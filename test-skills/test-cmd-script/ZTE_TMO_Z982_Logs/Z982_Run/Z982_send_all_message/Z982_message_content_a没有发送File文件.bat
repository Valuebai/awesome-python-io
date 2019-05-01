:1

rem 发送各种内容的消息


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

::=======================================================选择拍摄照片并发送1
rem 选择拍摄照片并发送
rem tap attach button
adb shell input tap 80 1800
ping -n 1 127.1 >nul
adb shell input tap 325 1850
ping -n 1 127.1 >nul

rem 点击拍照按钮
adb shell input tap 540 1640
ping -n 2 127.1 >nul
rem tap send button
adb shell input tap 970 980
adb shell input tap 970 1800
ping -n 2 127.1 >nul

rem reset
adb shell input tap 80 1000
ping -n 1 127.1 >nul
adb shell input swipe 320 1350 320 1750
ping -n 1 127.1 >nul

::=======================================================选择拍摄视频并发送1
rem 选择拍摄视频并发送
rem tap attach button
adb shell input tap 80 1800
ping -n 1 127.1 >nul
adb shell input tap 325 1850
ping -n 1 127.1 >nul

rem 点击拍摄按钮
adb shell input tap 110 1630
ping -n 4 127.1 >nul
adb shell input tap 540 1770
ping -n 2 127.1 >nul

rem tap send button
adb shell input tap 970 980
adb shell input tap 970 1800
ping -n 2 127.1 >nul

rem reset
adb shell input tap 80 1000
ping -n 1 127.1 >nul
adb shell input swipe 320 1350 320 1750
ping -n 1 127.1 >nul

::=======================================================选择Vcard并发送1
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

rem 点击Contacts
adb shell input tap 140 1520
ping -n 2 127.1 >nul
rem 选择 vcard
adb shell input tap 240 1140
ping -n 2 127.1 >nul

adb shell input tap 440 440
ping -n 2 127.1 >nul

rem tap send button
adb shell input tap 970 1800
ping -n 2 127.1 >nul


goto 1
