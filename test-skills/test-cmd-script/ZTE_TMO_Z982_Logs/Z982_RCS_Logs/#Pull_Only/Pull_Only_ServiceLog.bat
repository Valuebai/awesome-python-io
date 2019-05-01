adb wait-for-device
adb root
adb wait-for-device
adb remount
adb wait-for-device
:: get current flord path.
:: remove service config file.

set DAILYDIR=%cd%\RcsServicesLogs_%DATE:~0,10%

adb pull /sdcard/Android/data/com.suntek.mway.rcs.app.service/ %DAILYDIR%   

pause