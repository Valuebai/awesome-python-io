rem ��ʼץȡadb log
start %cd%\Z981_logcat.bat
::start %cd%\tcpdump.bat



rem 1-1chat
adb shell am start -a android.intent.action.SENDTO -d sms:%User18% --es sms_body  "%time%"
ping -n 1 127.1 >nul
rem adb shell input text "%time%"

adb shell input keyevent 4
ping -n 1 127.1 >nul
adb shell am start -a android.intent.action.SENDTO -d sms:%User18% --es sms_body  "%time%"
ping -n 1 127.1 >nul

adb shell input tap 1000 1800
ping -n 1 127.1 >nul


rem ���÷�������Ϣ���ݵĽű�
call Z981_message_content.bat

call Kill_monkey&logcat&tcpdump.bat
::call kill_tcpdump.bat

