1、先执行#1#执行脚本后，直接拔线或退出（会直接覆盖以前的日志）
	#1#start_logcat_all_background-->>抓的全日志，如果手机内存台太小，请谨慎使用
	#1#start_logcat_filter_e_background-->>抓的EROOR以上的日志，一般不会占用手机内存
	#1#start_tcpdump_background-->>抓取网络包
	
2、#1#脚本运行成功的标识，“一闪一闪的”（没有看到pause出来就算运行成功），拔线后到手机内存根目录检查是否运行成功，没有在执行1

3、用Kill_monkey&logcat&tcpdump.bat干掉进程，否则会一直在手机后台运行，直到关机才结束

4、再导出日志（会覆盖当前存在的日志，注意备份之前的日志）
#2#pull_logcat_all_background
#2#pull_logcat_filter_e_background
#2#pull_Only_Tcpdump