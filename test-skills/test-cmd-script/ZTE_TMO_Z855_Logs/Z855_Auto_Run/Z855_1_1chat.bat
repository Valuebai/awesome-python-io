::======================================================================
rem �����ռ��˱���
set  User1=14802443776
set  User2=17029379475
set  User3=17029341868
set  User4=17029454865
set  User5=17029455361
set  User6=17029341703
set  User7=17029341856
set  User8=14802443740
set  User9=14802443598
set  User10=17029453883
set  User11=17029341864
set  User12=14802443726
set  User13=17029341860
set  User14=14802443570
set  User15=17029341867
set  User16=13235614865
set  User17=13237654940
set  User18=13237654937
set  User19=13239758527
set  User20=13239758534
set  User21=13238426623
set  User22=14242792781
set  User23=14255021438
set  User24=13236816626
set  User25=13233845664
set  User26=14255891575
set  User27=14255891576

set  User28=14253657889
set  User29=14253726795
set  User30=14254354110
set  User31=14253659570
set  User32=14253726021
set  User33=13109854575

::�ڴ˴��޸�Ҫ���͵�1-1����
::===============================
set Flag11=0

:OneOneStart_1

::���õ�һ�η��͵�1-1����
if %Flag11% equ 0 (set User_1=%User27%)

::���õڶ��η��͵�1-1����
if %Flag11% equ 1 (set User_1=%User22%)


:: Ŀǰ���2�����뷢����Ϣ�����޸����ߵĺ��루14255891575��14255891576�ĺ��ĺ��뾭�����ߣ�

::��ǰ���淢���ı���Ϣ
::==========================================================
timeout /t 1
REM ����1-1��Ϣ
adb shell am start -a android.intent.action.SENDTO -d sms:"%User_1%" --es sms_body  "111"
timeout /t 1

REM ������ؼ�
adb shell input keyevent 4

timeout /t 1
REM tap send button
adb shell input tap 430 785
adb shell input tap 430 785
timeout /t 1

::=======================================================ѡ��������Ƭ������1
REM tap attach button
adb shell input tap 48 785
REM ѡ��������Ƭ������
adb shell input tap 45 395
timeout /t 1
adb shell input tap 135 820
timeout /t 1

REM ������հ�ť
adb shell input tap 240 720
timeout /t 2

REM ������ؼ�
adb shell input keyevent 4
timeout /t 1

REM tap send button
adb shell input tap 430 785
adb shell input tap 430 785
timeout /t 1


::��ǰ���淢���ı���Ϣ
::==========================================================
timeout /t 1
REM ����1-1��Ϣ
adb shell am start -a android.intent.action.SENDTO -d sms:"%User_1%" --es sms_body  "111"
timeout /t 2


REM ���»���
adb shell input swipe 30 150 30 250
timeout /t 1
REM tap send button
adb shell input tap 430 785
adb shell input tap 430 785
timeout /t 1

::=======================================================ѡ��������Ƭ������1
REM tap attach button
adb shell input tap 48 785
REM ѡ��������Ƭ������
adb shell input tap 45 395
timeout /t 1
adb shell input tap 135 820
timeout /t 1

REM ������㰴ť
adb shell input tap 55 710
timeout /t 4
adb shell input tap 240 720
timeout /t 1

REM ������ؼ�
adb shell input keyevent 4
timeout /t 1

REM tap send button
adb shell input tap 430 785
adb shell input tap 430 785
timeout /t 1


::��ǰ���淢���ı���Ϣ
::==========================================================
timeout /t 1
REM ����1-1��Ϣ
adb shell am start -a android.intent.action.SENDTO -d sms:"%User_1%" --es sms_body  "111"
timeout /t 2

::=======================================================����Hold to say
REM ���»���
adb shell input swipe 30 150 30 250
timeout /t 1
REM �л���¼��״̬
adb shell input tap 430 785
timeout /t 1
adb shell input tap 430 785
timeout /t 1
adb shell input tap 430 785
timeout /t 1
adb shell input tap 430 785
timeout /t 1

REM send
adb shell input swipe 250 800 250 800 6000
timeout /t 2


::��ǰ���淢���ı���Ϣ
::==========================================================
timeout /t 1
REM ����1-1��Ϣ
adb shell am start -a android.intent.action.SENDTO -d sms:"%User_1%" --es sms_body  "111"
timeout /t 2


REM ���»���
adb shell input swipe 30 150 30 250
timeout /t 1
REM tap send button
adb shell input tap 430 785
adb shell input tap 430 785
timeout /t 1

::=======================================================ѡ��vcard������1
REM tap attach button
adb shell input tap 48 785
REM ѡ��������Ƭ������
adb shell input tap 45 395
timeout /t 1
REM �������FILE
adb shell input tap 350 820
timeout /t 1

REM ѡ��vcard
adb shell input tap 240 700
timeout /t 1
adb shell input tap 100 520
timeout /t 1
adb shell input tap 220 220
timeout /t 1

REM ���»���
adb shell input swipe 30 150 30 250
timeout /t 1
REM tap send button
adb shell input tap 430 785
adb shell input tap 430 785
timeout /t 1


::��ǰ���淢���ı���Ϣ
::==========================================================
timeout /t 1
REM ����1-1��Ϣ
adb shell am start -a android.intent.action.SENDTO -d sms:"%User_1%" --es sms_body  "111"
timeout /t 2


REM ���»���
adb shell input swipe 30 150 30 250
timeout /t 1
REM tap send button
adb shell input tap 430 785
adb shell input tap 430 785
timeout /t 1

::=======================================================ѡ��file��Ƭ������1
REM tap attach button
adb shell input tap 48 785
REM ѡ��������Ƭ������
adb shell input tap 45 395
timeout /t 1
REM �������FILE
adb shell input tap 350 820
timeout /t 1

REM ѡ��FileͼƬ
adb shell input tap 80 680
timeout /t 2
adb shell input tap 78 187
timeout /t 2
adb shell input tap 120 230
timeout /t 2
adb shell input tap 75 220
timeout /t 2

REM ������ؼ�
adb shell input keyevent 4
timeout /t 1

REM tap send button
adb shell input tap 430 785
adb shell input tap 430 785
timeout /t 1

if %Flag11% equ 0 (set Flag11=1&goto OneOneStart_1) else (echo no)


:OneOneStart_1_end