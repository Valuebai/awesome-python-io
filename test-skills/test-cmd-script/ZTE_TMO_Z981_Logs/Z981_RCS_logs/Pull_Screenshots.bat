adb wait-for-device
adb root
adb wait-for-device
adb remount
adb wait-for-device
:: get current flord path.
:: remove service config file.

set DAILYDIR=%cd%\Screenshots

adb pull /sdcard/Pictures/Screenshots %DAILYDIR%

