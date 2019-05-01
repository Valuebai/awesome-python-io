adb wait-for-device
adb root
adb wait-for-device
adb remount
adb wait-for-device
:: get current flord path.
:: remove service config file.

set DAILYDIR=%cd%\Save_Photo_Vedio

adb pull /sdcard/Download %DAILYDIR%
::adb pull /storage/emulated/0/rcs %DAILYDIR%

::adb pull /sdcard/Android/data/com.android.mms/cache/ %DAILYDIR%

