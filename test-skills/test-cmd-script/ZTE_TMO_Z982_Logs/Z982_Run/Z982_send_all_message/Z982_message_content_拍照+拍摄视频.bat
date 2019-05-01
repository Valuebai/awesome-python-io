

:1

::=======================================================Ñ¡ÔñÅÄÉãÕÕÆ¬²¢·¢ËÍ1
rem Ñ¡ÔñÅÄÉãÕÕÆ¬²¢·¢ËÍ
rem tap attach button
adb shell input tap 80 1800
ping -n 1 127.1 >nul
adb shell input tap 325 1850
ping -n 1 127.1 >nul

rem µã»÷ÅÄÕÕ°´Å¥
adb shell input tap 540 1640
ping -n 2 127.1 >nul
rem tap send button
adb shell input tap 970 980
adb shell input tap 1000 1800
ping -n 2 127.1 >nul

rem reset
adb shell input tap 80 1000
ping -n 1 127.1 >nul
adb shell input swipe 320 1350 320 1750
ping -n 1 127.1 >nul

::=======================================================Ñ¡ÔñÅÄÉãÊÓÆµ²¢·¢ËÍ1
rem Ñ¡ÔñÅÄÉãÊÓÆµ²¢·¢ËÍ
rem tap attach button
adb shell input tap 80 1800
ping -n 1 127.1 >nul
adb shell input tap 325 1850
ping -n 1 127.1 >nul

rem µã»÷ÅÄÉã°´Å¥
adb shell input tap 110 1630
ping -n 4 127.1 >nul
adb shell input tap 540 1770
ping -n 2 127.1 >nul

rem tap send button
adb shell input tap 970 980
adb shell input tap 1000 1800
ping -n 2 127.1 >nul

rem reset
adb shell input tap 80 1000
ping -n 1 127.1 >nul
adb shell input swipe 320 1350 320 1750
ping -n 1 127.1 >nul

goto 1



