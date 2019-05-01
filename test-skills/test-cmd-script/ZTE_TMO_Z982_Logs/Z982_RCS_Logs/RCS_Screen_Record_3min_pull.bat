::功能：每3分钟导出一个视频到文件夹，如果时间不满3分钟，则不导出文件夹，存放在手机中
::使用：直接双击这个bat脚本
::from: lhb,2017-05-19

adb wait-for-device
adb root
adb wait-for-device
adb remount
adb wait-for-device

::设置当前路径作为日志保存的路径
set DAILYDIR=%cd%\%DATE:~0,4%%DATE:~5,2%%DATE:~8,2%

::判断是否存在路径并cd进入
if not exist %DAILYDIR% md %DAILYDIR%
cd %DAILYDIR%

::判断是否存在record路径并创建后cd进入
if not exist record md record
cd record

::设置goto标志
:2
::设置File变量
set File=%TIME:~0,2%%TIME:~3,2%%TIME:~6,2%

::执行录屏命令
adb shell screenrecord --size 480x640 --bit-rate 1000000 /sdcard/zdemo.mp4

::3分钟后，将视频导出
adb pull /sdcard/zdemo.mp4 "%File%"_screen_record.mp4

::进入死循环
goto 2
exit