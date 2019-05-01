::==========================================================
::修改好1-1和groupchat里面的userX后，可直接运行改程序
::运行后会直接调用录像和logcat，QXDM需要另外打开
::==========================================================

adb root
adb wait-for-device
adb remount
adb wait-for-device



rem 定义收件人变量
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

start Z981_Screen_Record_3min_pull.bat
:1
adb shell input keyevent 26
rem 电源键
::ping -n 3 127.1 >nul
adb shell input keyevent 82
rem 解锁
ping -n 3 127.1 >nul
adb shell input keyevent 3
rem 按home键
ping -n 3 127.1 >nul

rem 调用1-1chat脚本
call Z981_1_1chat.bat

ping -n 10 127.1 >nul

rem 调用group_chat脚本
call Z981_group_chat.bat

::echo restart the code again.
::pause
goto 1

