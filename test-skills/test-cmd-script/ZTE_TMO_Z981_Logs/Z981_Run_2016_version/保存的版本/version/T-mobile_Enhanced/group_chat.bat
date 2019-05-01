rem 开始抓取adb log
start %cd%\adb_logcat.bat

::单独运行group_chat时需加入
::set  User1=14802443776
::set  User2=17029453883

rem 群聊
adb shell am start -a android.intent.action.SENDTO -d sms:"%User11%,%User2%" --es sms_body  "%time%"
rem adb shell input text "%time%"
ping -n 1 127.1 >nul
adb shell input tap 1000 1800
ping -n 10 127.1 >nul

call message_content.bat

call kill_logcat.bat
