adb wait-for-device
adb root
adb wait-for-device
adb remount
adb wait-for-device

::抓取网络包
start RCS_Start_Tcpdump.bat

::录制3分钟视频，3分钟导出一个视频
start RCS_Screen_Record_3min_pull.bat

::抓Logcat相关日志
start RCS_Start_Logcat.bat


pause
