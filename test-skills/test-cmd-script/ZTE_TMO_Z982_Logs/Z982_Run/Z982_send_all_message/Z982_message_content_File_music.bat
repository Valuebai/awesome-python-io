rem ���͸������ݵ���Ϣ


:1
::=======================================================ѡ��File->music������1
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

rem ���File
adb shell input tap 950 1300
ping -n 2 127.1 >nul
rem ѡ��File->music
adb shell input tap 540 375
ping -n 2 127.1 >nul
adb shell input tap 500 350
ping -n 2 127.1 >nul

rem tap send button
adb shell input tap 970 980
adb shell input tap 970 1800
ping -n 2 127.1 >nul

goto 1



