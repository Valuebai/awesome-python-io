adb wait-for-device
adb root
adb wait-for-device
adb remount
adb wait-for-device
:: get current flord path.
:: remove service config file.



set DAILYDIR=E:\T-mobile\Run\zLogs_
if not exist %DAILYDIR% md %DAILYDIR%
cd %DAILYDIR%
echo %DAILYDIR%
echo "%date%%time% start to exec"

adb pull /storage/emulated/0/Android/data/com.suntek.mway.rcs.app.service/ %DAILYDIR%
adb pull data/data/com.android.providers.telephony/databases/mmssms.db %DAILYDIR%
adb pull /sdcard/zdemo.mp4 %DAILYDIR%
adb pull /sdcard/Pictures/Screenshots %DAILYDIR%
adb pull /sdcard/any.pcap %DAILYDIR%

move E:\T-mobile\Run\logcat.txt %DAILYDIR%

pause
