rem ���͸������ݵ���Ϣ


:1
::=======================================================ѡ��Vcard������1
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

rem ���Contacts
adb shell input tap 140 1520
ping -n 2 127.1 >nul
rem ѡ�� vcard
adb shell input tap 240 1140
ping -n 2 127.1 >nul

adb shell input tap 440 440
ping -n 2 127.1 >nul

rem tap send button
adb shell input tap 1000 1800
ping -n 2 127.1 >nul

goto 1



