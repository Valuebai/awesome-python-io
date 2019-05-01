rem Create Daily Folder
set DAILYDIR=%cd%\%DATE:~0,10%
if not exist %DAILYDIR% md %DAILYDIR%
cd %DAILYDIR%
if not exist logcat md logcat
cd logcat
set File=%TIME:~0,2%%TIME:~3,2%%TIME:~6,2%
::adb pull data/data/com.android.providers.telephony  %cd%\
adb logcat -v time > "%File%"_logcat.log
exit