:1

rem ���͸������ݵ���Ϣ


::=======================================================���뵱ǰ���ں�ʱ�䷢��
rem ���뵱ǰ���ں�ʱ�䷢��
adb shell input tap 400 1800
adb shell input text "1"
ping -n 1 127.1 >nul
adb shell input tap 970 980
ping -n 1 127.1 >nul
adb shell input tap 80 1000
ping -n 1 127.1 >nul
adb shell input swipe 320 1350 320 1750

::=======================================================����Hold to say
rem �����ı�
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


rem ����Hold to say
rem ���¼����ť
ping -n 2 127.1 >nul
adb shell input swipe 560 1800 560 1800 6000
ping -n 3 127.1 >nul

::=======================================================����Hold to say2
rem ���¼����ť
adb shell input swipe 560 1800 560 1800 6000
ping -n 3 127.1 >nul

rem reset
adb shell input tap 80 1800
ping -n 1 127.1 >nul
adb shell input swipe 320 1350 320 1750

::=======================================================ѡ��������Ƭ������1
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

rem reset
adb shell input tap 80 1000
ping -n 1 127.1 >nul
adb shell input swipe 320 1350 320 1750
ping -n 1 127.1 >nul

::=======================================================ѡ��������Ƶ������1
rem ѡ��������Ƶ������
rem tap attach button
adb shell input tap 80 1800
ping -n 1 127.1 >nul
adb shell input tap 325 1850
ping -n 1 127.1 >nul

rem ������㰴ť
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
adb shell input tap 970 1800
ping -n 2 127.1 >nul

::=======================================================ѡ��File->pic������1
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
ping -n 1 127.1 >nul

rem ѡ��File->pic
adb shell input tap 180 370
ping -n 2 127.1 >nul
adb shell input tap 800 500
ping -n 2 127.1 >nul
adb shell input tap 800 500
ping -n 2 127.1 >nul

rem tap send button
adb shell input tap 970 980
adb shell input tap 970 1800
ping -n 2 127.1 >nul

::=======================================================ѡ��File->video������1
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
rem ѡ��File->vedio
adb shell input tap 900 380
ping -n 2 127.1 >nul
adb shell input tap 180 430
ping -n 2 127.1 >nul

rem tap send button
adb shell input tap 970 980
adb shell input tap 970 1800
ping -n 2 127.1 >nul

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

::=======================================================¼����Ƶ������1
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

rem ���¼�ư�ť
adb shell input tap 650 1250
ping -n 1 127.1 >nul
adb shell input tap 540 1735
ping -n 5 127.1 >nul
adb shell input tap 900 1740
ping -n 3 127.1 >nul


rem tap send button
adb shell input tap 970 980
adb shell input tap 970 1800
ping -n 1 127.1 >nul

rem reset
adb shell input tap 80 1000
ping -n 1 127.1 >nul
adb shell input swipe 320 1350 320 1750
ping -n 1 127.1 >nul


goto 1
