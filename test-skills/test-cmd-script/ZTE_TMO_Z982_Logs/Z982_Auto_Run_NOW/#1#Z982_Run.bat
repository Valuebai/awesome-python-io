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

start Z982_Screen_Record_3min_pull.bat

::====================================================
:: �����ֻ�
:UnlockPhone
rem ����Դ��
adb shell input keyevent 26
ping -n 2 127.1 >nul
rem ����
adb shell input keyevent 82
ping -n 2 127.1 >nul
adb shell input swipe 540 1800 540 1800 6000
rem ��home��
adb shell input keyevent 3
ping -n 1 127.1 >nul


::===========================================
rem ��һ�ο���ʱ����mmsȨ��û�п���
:OpenPermissionMessaging
adb shell am start -n com.android.messaging/.ui.conversationlist.ConversationListActivity
timeout /t 1
adb shell input tap 800 1850
timeout /t 1
adb shell input tap 820 1165
timeout /t 1
adb shell input tap 820 1165
timeout /t 1
adb shell input tap 820 1165
timeout /t 1
adb shell input tap 820 1165
timeout /t 1
adb shell input tap 820 1165
timeout /t 1
adb shell input keyevent 3
adb shell am start -n com.android.messaging/.ui.conversationlist.ConversationListActivity
timeout /t 1

rem ���÷���ͼƬ��ѹ����
::adb shell input tap 840 1224
::adb shell input tap 400 1000

::===========================================
rem ���ʼ��������home��������Ϣ���˻�

:1
::===========================================
rem ����1-1chat�ű�
call Z982_1_1chat.bat
ping -n 2 127.1 >nul

rem ����group_chat�ű�
call Z982_group_chat.bat
ping -n 2 127.1 >nul
::===========================================

goto 1