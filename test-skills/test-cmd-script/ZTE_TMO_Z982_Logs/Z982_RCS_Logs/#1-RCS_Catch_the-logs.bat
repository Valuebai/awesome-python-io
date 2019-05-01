::功能：抓取Z982手机的主要日志
::使用：直接双击这个bat脚本，然后关闭所有窗口。根据自己的需要注释代码，注意不要删除同级目录下的bat脚本
::from: lhb,2017-05-19

adb wait-for-device
adb root
adb wait-for-device
adb remount
adb wait-for-device

::抓取网络包
start RCS_Start_Tcpdump.bat

::录制3分钟视频，3分钟导出一个视频
start RCS_Screen_Record_3min_pull.bat

::录制3分钟视频，录制的视频保存到手机中直接被拉出来
::start RCS_Start_Video.bat

::抓Logcat相关日志
start RCS_Start_Logcat.bat
::start RCS_Start_Events.bat
start RCS_Start_Radio.bat
::start RCS_Start_System.bat
::start RCS_Start_kernel_log.bat
::start RCS_Start_bugreport.bat

::抓取开机日志
::RCS_Start_dmesg.bat  


pause
