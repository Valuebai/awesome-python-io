::adb wait-for-device
::adb root
::adb wait-for-device
::adb remount
::adb wait-for-device

set DAILYDIR=%cd%\Screenshots

adb pull /sdcard/Pictures/Screenshots %DAILYDIR%

