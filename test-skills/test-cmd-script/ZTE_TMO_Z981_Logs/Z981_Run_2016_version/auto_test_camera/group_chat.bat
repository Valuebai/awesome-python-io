rem ��ʼץȡadb log
start %cd%\adb_logcat.bat
::start %cd%\tcpdump.bat


rem Ⱥ��
adb shell am start -a android.intent.action.SENDTO -d sms:"%User16%,%User3%" --es sms_body  "%time%"
rem adb shell input text "%time%"
ping -n 1 127.1 >nul
adb shell input tap 1000 1800
ping -n 10 127.1 >nul

call message_content.bat

call kill_logcat.bat
::call kill_tcpdump.bat