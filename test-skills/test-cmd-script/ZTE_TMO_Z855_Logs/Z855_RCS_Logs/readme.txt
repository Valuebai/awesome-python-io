1、抓取RCS日志，必须开启命令后重启
adb shell setprop persist.sys.rcs.log.level 1
可直接执行#0-Open_RCS_logs.bat

2、先执行#1-RCS_Catch_the-logs.bat，进行复现的操作，然后关闭所有窗口，执行#2-Move_logs_ToSave.bat拉取并保存日志

注意点：
（1）此脚本运行在windows环境下
（2）执行#2后，日志保存到文件夹zAllLogs_[description][time][version]中，如果再次执行#2，会提醒存在该文件，需重命名
（3）#2只拉取手机中的一个视频到文件夹中，如果操作大于3分钟，请到record文件夹下查找
RCS_Screen_Record_3min_pull.bat--这个是拉视频的脚本，每超过3分钟，拉视频到电脑，未超过3分钟的视频保存在手机里面
（4）将此脚本放到正常的路径，最好英文，不带特殊字符的路径


