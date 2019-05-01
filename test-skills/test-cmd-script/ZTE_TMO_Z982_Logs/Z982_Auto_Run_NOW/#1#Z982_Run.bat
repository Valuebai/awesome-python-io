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

start Z982_Screen_Record_3min_pull.bat

::====================================================
:: 解锁手机
:UnlockPhone
rem 按电源键
adb shell input keyevent 26
ping -n 2 127.1 >nul
rem 解锁
adb shell input keyevent 82
ping -n 2 127.1 >nul
adb shell input swipe 540 1800 540 1800 6000
rem 按home键
adb shell input keyevent 3
ping -n 1 127.1 >nul


::===========================================
rem 第一次开机时进入mms权限没有开启
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

rem 设置发送图片的压缩比
::adb shell input tap 840 1224
::adb shell input tap 400 1000

::===========================================
rem 类初始化，返回home并进入消息或退回

:1
::===========================================
rem 调用1-1chat脚本
call Z982_1_1chat.bat
ping -n 2 127.1 >nul

rem 调用group_chat脚本
call Z982_group_chat.bat
ping -n 2 127.1 >nul
::===========================================

goto 1