adb wait-for-device
adb root
adb wait-for-device
adb remount
adb wait-for-device
:: get current flord path.
:: remove service config file.

set i=1
set DAILYDIR=%cd%\RcsServicesLogs
echo %DAILYDIR%

FOR /L %%i in (1 1 1000) do (
echo %%i
echo %DAILYDIR%
adb pull /sdcard/Android/data/com.suntek.mway.rcs.app.service/ %DAILYDIR%
pause

)






   

