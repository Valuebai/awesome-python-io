::==========================================================
::�޸ĺ�1-1��groupchat�����userX�󣬿�ֱ�����иĳ���
::���к��ֱ�ӵ���¼���logcat��QXDM��Ҫ�����
::==========================================================
adb wait-for-device
adb root
adb wait-for-device
adb remount
adb wait-for-device

timeout /t 5

start Z985_Screen_Record_3min_pull.bat

::====================================================
:: �����ֻ�
:UnlockPhone
rem ����Դ��
adb shell input keyevent 26
timeout /t 1
rem ����
adb shell input keyevent 82
timeout /t 2
adb shell input swipe 240 817 240 817 6000
rem ��home��
adb shell input keyevent 3
timeout /t 1

::===========================================
rem ��һ�ο���ʱ����mmsȨ��û�п���
:OpenPermissionMessaging
adb shell am start -n com.android.messaging/.ui.conversationlist.ConversationListActivity
timeout /t 1
adb shell input tap 350 820
timeout /t 1
adb shell input tap 380 530
timeout /t 1
adb shell input tap 380 530
timeout /t 1
adb shell input tap 380 530
timeout /t 1
adb shell input tap 380 530
timeout /t 1
adb shell input tap 380 530
timeout /t 1
adb shell input keyevent 3
adb shell am start -n com.android.messaging/.ui.conversationlist.ConversationListActivity
timeout /t 1

::===========================================
rem ��һ�ο���ʱ����mmsȨ��û�п���
:OpenPermissionSendPic
adb shell input keyevent 3
adb shell am start -n com.android.messaging/.ui.conversationlist.ConversationListActivity
timeout /t 1
adb shell am start -a android.intent.action.SENDTO -d sms:"14255891576"
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

adb shell input tap 380 555
timeout /t 1
adb shell input tap 180 430
timeout /t 1



:1
::===========================================
rem ����1-1chat�ű�
call Z855_1_1chat.bat
ping -n 2 127.1 >nul

rem ����group_chat�ű�
call Z855_group_chat.bat
ping -n 2 127.1 >nul
::===========================================

goto 1