adb wait-for-device
adb root
adb wait-for-device
adb remount
adb wait-for-device
:: get current flord path.
:: remove service config file.

set DAILYDIR=%DATE:~0,10%_%TIME:~0,2%_%TIME:~3,2%_%TIME:~6,2%
echo %DAILYDIR%

ren C:\rcs\demo.mp4 %DAILYDIR%_demo.mp4

