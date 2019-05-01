adb wait-for-device
adb root
adb wait-for-device
adb remount
adb wait-for-device
:: get current flord path.
:: remove service config file.

echo 请检查抓取手机日志的设备号
pause

set DAILYDIR=%cd%\Logs_设备

::1_848ecafd 是对应的设备号，请注意修改

adb -s 1_848ecafd pull /sdcard/Pictures/Screenshots %DAILYDIR%

adb -s 1_848ecafd pull /sdcard//Android/data/com.suntek.mway.rcs.app.service/ %DAILYDIR%

adb -s 1_848ecafd logcat -v time >logcat.txt

adb -s 1_848ecafd shell dumpsys meminfo | find "mms"
adb -s 1_848ecafd shell dumpsys cpuinfo | find "mms"





















