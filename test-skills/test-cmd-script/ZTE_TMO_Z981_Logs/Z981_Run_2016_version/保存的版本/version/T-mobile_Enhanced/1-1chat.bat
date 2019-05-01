rem 开始抓取adb log
start %cd%\adb_logcat.bat

::单独运行1-1_chat时需加入
::set  User1=14802443776

rem 1-1chat
adb shell am start -a android.intent.action.SENDTO -d sms:%User2% --es sms_body  "%time%"
ping -n 1 127.1 >nul
rem adb shell input text "%time%"
ping -n 1 127.1 >nul

adb shell input tap 1000 1800
ping -n 1 127.1 >nul

rem 调用发各种消息内容的脚本
call message_content.bat

call kill_logcat.bat
