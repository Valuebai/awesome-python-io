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
if %Flag11% equ 0 (set User_1=%User27%)

::设置第二次发送的1-1号码
if %Flag11% equ 1 (set User_1=%User9%)


:: 目前会给2个号码发送消息，请修改在线的号码（14255891575、14255891576文豪的号码经常在线）
::==========================================================
adb shell input tap 970 1800
ping -n 2 127.1 >nul
REM 发送1-1消息
adb shell am start -a android.intent.action.SENDTO -d sms:"%User_1%" --es sms_body  "111"
ping -n 4 127.1 >nul
REM tap send button
adb shell input tap 970 1800
ping -n 2 127.1 >nul



::==========================================================
adb shell input tap 970 1800
ping -n 2 127.1 >nul
adb shell am start -a android.intent.action.SENDTO -d sms:"%User_1%" --es sms_body  "111"
ping -n 4 127.1 >nul
REM tap send button
adb shell input tap 970 1800
ping -n 2 127.1 >nul
::=======================================================选择拍摄照片并发送1
REM 选择拍摄照片并发送
REM tap attach button
adb shell input tap 80 1800
ping -n 1 127.1 >nul
adb shell input tap 325 1850
ping -n 1 127.1 >nul

REM 点击拍照按钮
adb shell input tap 540 1640
ping -n 2 127.1 >nul
REM tap send button
adb shell input tap 970 980
ping -n 2 127.1 >nul

REM reset
adb shell input tap 80 1000
ping -n 1 127.1 >nul
adb shell input swipe 320 1350 320 1750
ping -n 1 127.1 >nul


::==========================================================
adb shell input tap 970 1800
ping -n 2 127.1 >nul
adb shell am start -a android.intent.action.SENDTO -d sms:"%User_1%" --es sms_body  "111"
ping -n 4 127.1 >nul
rem tap send button
adb shell input tap 970 1800
adb shell input tap 970 1800
ping -n 2 127.1 >nul
::=======================================================发送Hold to say
ping -n 2 127.1 >nul
adb shell input swipe 560 1800 560 1800 6000
ping -n 3 127.1 >nul
::=======================================================发送Hold to say
ping -n 2 127.1 >nul
adb shell input swipe 560 1800 560 1800 6000
ping -n 3 127.1 >nul

::==========================================================
adb shell input tap 970 1800
ping -n 2 127.1 >nul
adb shell am start -a android.intent.action.SENDTO -d sms:"%User_1%" --es sms_body  "111"
ping -n 4 127.1 >nul
rem tap send button
adb shell input tap 970 1800
ping -n 2 127.1 >nul
::=======================================================选择拍摄视频并发送1
rem 选择拍摄视频并发送
rem tap attach button
adb shell input tap 80 1800
ping -n 1 127.1 >nul
adb shell input tap 325 1850
ping -n 1 127.1 >nul

rem 点击拍摄按钮
adb shell input tap 110 1630
ping -n 4 127.1 >nul
adb shell input tap 540 1770
ping -n 2 127.1 >nul

rem tap send button
adb shell input tap 970 980
ping -n 2 127.1 >nul

rem reset
adb shell input tap 80 1000
ping -n 1 127.1 >nul
adb shell input swipe 320 1350 320 1750
ping -n 1 127.1 >nul


::==========================================================
adb shell input tap 970 1800
ping -n 2 127.1 >nul
adb shell am start -a android.intent.action.SENDTO -d sms:"%User_1%" --es sms_body  "111"
ping -n 4 127.1 >nul
rem tap send button
adb shell input tap 970 1800
adb shell input tap 970 1800
ping -n 2 127.1 >nul
::=======================================================选择Vcard并发送1
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

rem 点击Contacts
adb shell input tap 140 1520
ping -n 2 127.1 >nul
rem 选择 vcard
adb shell input tap 240 1140
ping -n 2 127.1 >nul

adb shell input tap 440 440
ping -n 2 127.1 >nul

rem tap send button
adb shell input tap 1000 1800
ping -n 2 127.1 >nul



::==========================================================
adb shell input tap 970 1800
ping -n 2 127.1 >nul
adb shell am start -a android.intent.action.SENDTO -d sms:"%User_1%" --es sms_body  "111"
ping -n 4 127.1 >nul
rem tap send button
adb shell input tap 970 1800
ping -n 2 127.1 >nul
::=======================================================选择File->pic并发送1
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

rem 点击File
adb shell input tap 950 1300
ping -n 1 127.1 >nul

rem 选择File->pic
adb shell input tap 180 370
ping -n 2 127.1 >nul
adb shell input tap 800 500
ping -n 2 127.1 >nul
adb shell input tap 800 500
ping -n 2 127.1 >nul

rem tap send button
adb shell input tap 970 980
ping -n 2 127.1 >nul


::==========================================================
adb shell input tap 970 1800
ping -n 2 127.1 >nul
adb shell am start -a android.intent.action.SENDTO -d sms:"%User_1%" --es sms_body  "111"
ping -n 4 127.1 >nul
rem tap send button
adb shell input tap 970 1800
ping -n 2 127.1 >nul
::=======================================================选择File->music并发送1
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

rem 点击File
adb shell input tap 950 1300
ping -n 2 127.1 >nul
rem 选择File->music
adb shell input tap 540 375
ping -n 2 127.1 >nul
adb shell input tap 500 350
ping -n 2 127.1 >nul

rem tap send button
adb shell input tap 970 980
ping -n 2 127.1 >nul

if %Flag11% equ 0 (set Flag11=1&goto OneOneStart_1) else (echo no)


:OneOneStart_1_end


::==========================================================
::==========================================================
::==========================================================

