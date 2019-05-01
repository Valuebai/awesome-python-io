rem 发送各种内容的消息

:1


::=======================================================选择拍摄照片并发送1解锁
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

adb shell input tap 840 1220
ping -n 2 127.1 >nul
adb shell input tap 500 850
ping -n 2 127.1 >nul


goto 1

