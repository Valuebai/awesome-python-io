::==========================================================
::修改好1-1和groupchat里面的userX后，可直接运行改程序
::运行后会直接调用录像和logcat，QXDM需要另外打开
::==========================================================
adb wait-for-device
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


start %cd%\RCS_E_Logcat.bat
start Z982_Screen_Record_3min_pull.bat

:1

::===========================================
rem 类初始化，返回home并进入消息或退回

rem 返回键
adb shell input keyevent 4
adb shell input keyevent 4
adb shell input tap 650 1145

rem 按home键
adb shell input keyevent 3
ping -n 2 127.1 >nul
rem tap mms app
adb shell input tap 730 1800
ping -n 2 127.1 >nul

rem 返回键
adb shell input keyevent 4
adb shell input keyevent 4
adb shell input tap 650 1145
adb shell input keyevent 4
adb shell input keyevent 4
adb shell input keyevent 4 
adb shell input keyevent 4 
adb shell input tap 650 1145
ping -n 3 127.1 >nul

rem 按home键
ping -n 2 127.1 >nul
rem tap mms app
adb shell input tap 730 1800
ping -n 2 127.1 >nul
rem 进入advanced messaging
adb shell input tap 1014 153
ping -n 2 127.1 >nul
adb shell input tap 620 305
ping -n 2 127.1 >nul
adb shell input tap 300 550
rem 返回键
adb shell input keyevent 4
adb shell input keyevent 4
adb shell input keyevent 4
adb shell input keyevent 4
adb shell input keyevent 4 
ping -n 3 127.1 >nul

rem 按home键
adb shell input keyevent 3
ping -n 2 127.1 >nul
rem tap mms app
adb shell input tap 730 1800
ping -n 2 127.1 >nul

rem tap first
adb shell input tap 400 400
rem 返回键
adb shell input keyevent 4
adb shell input tap 650 1145
ping -n 1 127.1 >nul
rem tap second
adb shell input tap 400 660
rem 返回键
adb shell input keyevent 4
adb shell input tap 650 1145
ping -n 1 127.1 >nul
rem tap third
adb shell input tap 400 950
rem 返回键
adb shell input keyevent 4
adb shell input tap 650 1145
ping -n 1 127.1 >nul
rem tap four
adb shell input tap 400 1110
rem 返回键
adb shell input keyevent 4
adb shell input tap 650 1145
ping -n 1 127.1 >nul

adb shell input tap 730 1800

rem 返回键
adb shell input keyevent 4
adb shell input keyevent 4
adb shell input keyevent 4
adb shell input keyevent 4 
ping -n 4 127.1 >nul



::===========================================
rem 调用1-1chat脚本
call Z982_1_1chat.bat
ping -n 6 127.1 >nul

rem 调用group_chat脚本
call Z982_group_chat.bat
::===========================================

goto 1

