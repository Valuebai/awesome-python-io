::======================================================================
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

::在此处修改要发送的1-1号码
::===============================
set Flag11=0

:OneOneStart_1

::设置第一次发送的1-1号码
if %Flag11% equ 0 (set User_1=%User24%)

:1

::当前界面发送文本消息
::==========================================================
timeout /t 1
REM 发送1-1消息
adb shell am start -a android.intent.action.SENDTO -d sms:"%User_1%" --es sms_body  "111"
timeout /t 2


REM 往下滑动
adb shell input swipe 30 150 30 250
timeout /t 1
REM tap send button
adb shell input tap 430 785
adb shell input tap 430 785
timeout /t 1

::=======================================================选择拍摄照片并发送1
REM tap attach button
adb shell input tap 48 785
REM 选择拍摄照片并发送
adb shell input tap 45 395
timeout /t 1
adb shell input tap 135 820
timeout /t 1

REM 点击拍摄按钮
adb shell input tap 55 710
timeout /t 4
adb shell input tap 240 720
timeout /t 1

REM 点击返回键
adb shell input keyevent 4
timeout /t 1

REM tap send button
adb shell input tap 430 785
adb shell input tap 430 785
timeout /t 1

goto 1

pause