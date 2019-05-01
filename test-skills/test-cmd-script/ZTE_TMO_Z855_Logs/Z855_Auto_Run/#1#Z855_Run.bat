::==========================================================
::修改好1-1和groupchat里面的userX后，可直接运行改程序
::运行后会直接调用录像和logcat，QXDM需要另外打开
::==========================================================
adb wait-for-device
adb root
adb wait-for-device
adb remount
adb wait-for-device

timeout /t 5

start Z985_Screen_Record_3min_pull.bat

::====================================================
:: 解锁手机
:UnlockPhone
rem 按电源键
adb shell input keyevent 26
timeout /t 1
rem 解锁
adb shell input keyevent 82
timeout /t 2
adb shell input swipe 240 817 240 817 6000
rem 按home键
adb shell input keyevent 3
timeout /t 1

::===========================================
rem 第一次开机时进入mms权限没有开启
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
rem 第一次开机时进入mms权限没有开启
:OpenPermissionSendPic
adb shell input keyevent 3
adb shell am start -n com.android.messaging/.ui.conversationlist.ConversationListActivity
timeout /t 1
adb shell am start -a android.intent.action.SENDTO -d sms:"14255891576"
timeout /t 1
::=======================================================选择拍摄照片并发送1
REM tap attach button
adb shell input tap 48 785
REM 选择拍摄照片并发送
adb shell input tap 45 395
timeout /t 1
adb shell input tap 135 820
timeout /t 1

REM 点击拍照按钮
adb shell input tap 240 720
timeout /t 2

REM 点击返回键
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
rem 调用1-1chat脚本
call Z855_1_1chat.bat
ping -n 2 127.1 >nul

rem 调用group_chat脚本
call Z855_group_chat.bat
ping -n 2 127.1 >nul
::===========================================

goto 1