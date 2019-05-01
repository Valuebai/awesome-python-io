1、执行#1#Z982_monkey_500_500.bat，注意是否执行成功（执行成功后可直接拔线）

2、如需让手机拔线后抓取logcat、tcpdump等日志，请参考《##手机后台运行_logcat_tcpdump》

3、RCS_Screen_Record_3min_pull.bat--这个是拉视频的脚本，每超过3分钟，拉视频到电脑，未超过3分钟的视频保存在手机里面（手机必须连接电脑）

4、直接执行类似下面*.bat命令，杀死monkey、logcat等相关命令（此过程可能引起Z982重启）
Kill_monkey_only.bat
Kill_monkey&logcat&tcpdump&uiautomator&screenrecord.bat

5、拉取并保存Monkey日志，执行2个脚本，拉取ZTE的日志
#2#Pull_logs_After_Monkey_ToSave.bat
#2#ZTE_AndroidAutocopy.bat