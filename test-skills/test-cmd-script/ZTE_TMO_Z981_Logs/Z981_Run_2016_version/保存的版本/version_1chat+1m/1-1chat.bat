rem 开始抓取adb log
start %cd%\adb_logcat.bat


rem 1-1chat
adb shell am start -a android.intent.action.SENDTO -d sms:%User5% --es sms_body  "%time%"
ping -n 1 127.1 >nul
rem adb shell input text "%time%"
ping -n 1 127.1 >nul

adb shell input tap 1000 1800
ping -n 1 127.1 >nul

rem 调用发各种消息内容的脚本
call message_content.bat

call kill_logcat.bat
