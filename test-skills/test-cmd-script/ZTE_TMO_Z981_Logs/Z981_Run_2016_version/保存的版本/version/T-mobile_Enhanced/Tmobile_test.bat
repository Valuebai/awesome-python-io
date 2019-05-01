adb root
adb wait-for-device
adb remount
adb wait-for-device



rem 定义收件人变量
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
rem 按home键
ping -n 5 127.1 >nul

rem 调用1-1chat脚本
call 1-1chat.bat

ping -n 10 127.1 >nul

rem 调用group_chat脚本
call group_chat.bat

::echo restart the code again.
::pause
goto 1

