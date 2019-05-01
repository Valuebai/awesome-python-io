adb wait-for-device
adb root
adb wait-for-device
adb remount
adb wait-for-device
@echo *****************************
@echo %date%%time%
@echo          Pull logs 
@echo *****************************

::设置当前路径
::如何需要设置其他路径，替换%cd%
set CurrentDir=%cd%

::定义RCSLOGDIR
@set RCSLOGDIR=%cd%\RCS_Logs_AutoRun
@echo %RCSLOGDIR%

::---------------mkdir Folder---------------
if not exist %RCSLOGDIR% md %RCSLOGDIR%
@echo current dir:%RCSLOGDIR%
@cd %RCSLOGDIR%


::---------------Pull Logs---------------
adb pull /sdcard/any.pcap %RCSLOGDIR%

adb pull /sdcard/Android/data/com.suntek.mway.rcs.app.service/ %RCSLOGDIR%
adb pull /sdcard/Android/data/com.suntek.mway.rcs.app.plugin/ %RCSLOGDIR%

adb pull data/data/com.android.providers.telephony/databases/mmssms.db %RCSLOGDIR%
adb pull data/data/com.suntek.mway.rcs.app.service/databases/rcs.db %RCSLOGDIR%
adb pull /data/data/com.android.providers.contacts/databases/profile.db %RCSLOGDIR%
adb pull /data/data/com.android.providers.contacts/databases/contacts2.db %RCSLOGDIR%

::---------------Pull Video&Pic---------------
adb pull /sdcard/zdemo.mp4 %RCSLOGDIR%
adb shell screencap -p /sdcard/screen.png
adb pull /sdcard/screen.png %RCSLOGDIR%


