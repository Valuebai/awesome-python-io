adb wait-for-device
adb root
adb wait-for-device
adb remount
adb wait-for-device
:: get current flord path.
:: remove service config file.

set i=1
set DAILYDIR=C:\rcs\RcsServicesLogs_%%i
echo %DAILYDIR%

FOR /L %%i in (1 1 1000) do (
echo %%i
set DAILYDIR=C:\rcs\z_RcsServicesLogs_%%i
echo %DAILYDIR%
adb pull /storage/emulated/0/Android/data/com.suntek.mway.rcs.app.service/ %DAILYDIR%
pause

)






   

