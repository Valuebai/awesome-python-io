adb root
adb wait-for-device
adb remount
adb wait-for-device



rem �����ռ��˱���
set  User1=14802443776
set  User2=17029453883
set  User3=17029341868
set  User4=17029454865
set  User5=14802443740
set  User6=17029341703
set  User7=17029341856
set  User8=14802443740
set  User9=14802443929
set  User10=17029379475
set  User11=14802443726
set  User12=17029341864

:1
adb shell input keyevent 3
rem ��home��
ping -n 5 127.1 >nul

rem ����1-1chat�ű�
call 1-1chat.bat

ping -n 10 127.1 >nul

rem ����group_chat�ű�
call group_chat.bat

::echo restart the code again.
::pause
goto 1

