rem ��ʼץȡadb log
start %cd%\Z981_logcat.bat
::start %cd%\tcpdump.bat


rem Ⱥ��
adb shell am start -a android.intent.action.SENDTO -d sms:"%User18%,%User3%" --es sms_body  "%time%"
rem adb shell input text "%time%"
ping -n 1 127.1 >nul
adb shell input tap 1000 1800
ping -n 10 127.1 >nul

call Z981_message_content.bat

call Kill_monkey&logcat&tcpdump.bat
::call kill_tcpdump.bat