rem ���͸������ݵ���Ϣ

:1


::=======================================================ѡ��������Ƭ������1����
rem ѡ��������Ƭ������
rem tap attach button
adb shell input tap 80 1800
ping -n 1 127.1 >nul
adb shell input tap 325 1850
ping -n 1 127.1 >nul

rem ������հ�ť
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

