::==========================================================
::�޸ĺ�1-1��groupchat�����userX�󣬿�ֱ�����иĳ���
::���к��ֱ�ӵ���¼���logcat��QXDM��Ҫ�����
::==========================================================

adb root
adb wait-for-device
adb remount
adb wait-for-device



rem �����ռ��˱���
set  User1=14802443776
set  User2=17029379475
set  User3=17029341868
set  User4=17029454865
set  User5=17029455361
set  User6=17029341703
set  User7=17029341856
set  User8=14802443740
set  User9=14802443929
set  User10=17029453883
set  User11=17029341864
set  User12=14802443726
set  User13=17029341860
set  User14=14802443570
set  User15=17029341867
set  User16=13237654940

start screen_record.bat
:1
adb shell input keyevent 26
rem ��Դ��
::ping -n 3 127.1 >nul
adb shell input keyevent 82
rem ����
ping -n 3 127.1 >nul
adb shell input keyevent 3
rem ��home��
ping -n 3 127.1 >nul

rem ����1-1chat�ű�
call 1-1chat.bat

ping -n 10 127.1 >nul

rem ����group_chat�ű�
call group_chat.bat

::echo restart the code again.
::pause
goto 1

