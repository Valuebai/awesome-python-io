rem ��ϢappĬ�Ϸ��ڵ�����λ��

:1


rem ��home��
adb shell input keyevent 3

rem ���ؼ�
adb shell input keyevent 4
adb shell input keyevent 4
adb shell input keyevent 4

rem tap mms app
adb shell input tap 730 1800 

rem tap first
adb shell input tap 400 400

rem ���ؼ�
adb shell input keyevent 4
ping -n 1 127.1 >nul

rem tap second
adb shell input tap 400 660

rem ���ؼ�
adb shell input keyevent 4
ping -n 1 127.1 >nul

rem tap third
adb shell input tap 400 950

rem ���ؼ�
adb shell input keyevent 4
ping -n 1 127.1 >nul

rem tap four
adb shell input tap 400 1110

rem ���ؼ�
adb shell input keyevent 4
ping -n 1 127.1 >nul

goto 1

