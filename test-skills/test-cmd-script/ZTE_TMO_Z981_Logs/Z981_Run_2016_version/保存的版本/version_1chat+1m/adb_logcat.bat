rem Create Daily Folder
set DAILYDIR=%cd%\%DATE:~0,10%
if not exist %DAILYDIR% md %DAILYDIR%
cd %DAILYDIR%
set File=%TIME:~0,2%%TIME:~3,2%%TIME:~6,2%
adb logcat -v time > logcat_%File%.log
exit