
:1
::=======================================================Ñ¡ÔñÒÑ´æÔÚµÄÍ¼Æ¬·¢ËÍ1
rem tap attach button
adb shell input tap 80 1800
ping -n 1 127.1 >nul
adb shell input tap 325 1850
ping -n 1 127.1 >nul
adb shell input tap 80 1000
ping -n 1 127.1 >nul

rem ÓÒ»¬
adb shell input swipe 600 1750 200 1750
ping -n 1 127.1 >nul

rem Ñ¡ÔñÍ¼Æ¬
adb shell input tap 530 1300
ping -n 3 127.1 >nul

rem tap send button
adb shell input tap 970 980
adb shell input tap 1000 1800
ping -n 1 127.1 >nul

rem reset
adb shell input tap 80 1000
ping -n 1 127.1 >nul
adb shell input swipe 320 1350 320 1750
ping -n 1 127.1 >nul

goto 1



