rem ���͸������ݵ���Ϣ

:1
::=======================================================���뵱ǰ���ں�ʱ�䷢��
rem ���뵱ǰ���ں�ʱ�䷢��
adb shell input tap 400 1800
adb shell input text "11a"
::ping -n 0.1 127.1 >nul
adb shell input tap 970 980
::ping -n 0.1 127.1 >nul


::=======================================================�ٴ����뵱ǰ���ں�ʱ�䷢��
rem �ٴ����뵱ǰ���ں�ʱ�䷢��
adb shell input text "11a"
::ping -n 0.1 127.1 >nul
adb shell input tap 970 980
::ping -n 0.1 127.1 >nul


goto 1

