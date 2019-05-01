adb wait-for-device
adb root
adb wait-for-device
adb remount
adb wait-for-device


set DAILYDIR=%cd%\odex

adb pull /system/app/NaRcsService/ %DAILYDIR%

