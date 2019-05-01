rem Create Daily Folder

set DAILYDIR=%cd%\%DATE:~0,4%%DATE:~5,2%%DATE:~8,2%
if not exist %DAILYDIR% md %DAILYDIR%
cd %DAILYDIR%
if not exist record md record
cd record
:2
set File=%TIME:~0,2%%TIME:~3,2%%TIME:~6,2%
adb wait-for-device shell screenrecord --size 480x640 --bit-rate 1000000 /sdcard/zdemo.mp4
adb wait-for-device pull /sdcard/zdemo.mp4 "%File%"_screen_record.mp4
goto 2
exit