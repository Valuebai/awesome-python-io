adb wait-for-device
adb root
adb wait-for-device
adb remount
adb wait-for-device
:: get current flord path.
:: remove service config file.

set DAILYDIR=%cd%\zAllLogs_%DATE:~0,10%_%TIME:~0,2%.%TIME:~3,2%.%TIME:~6,2%
set CurrentDir=%cd%
echo %DAILYDIR%
echo "%date%%time% start to exec"

::-------------mkdir Folder--------------------------
if not exist %DAILYDIR% md %DAILYDIR%
cd %DAILYDIR%

adb pull /storage/emulated/0/Android/data/com.suntek.mway.rcs.app.service/ %DAILYDIR%
adb pull data/data/com.android.providers.telephony/databases/mmssms.db %DAILYDIR%
adb pull /sdcard/zdemo.mp4 %DAILYDIR%
::adb pull /sdcard/Pictures/Screenshots %DAILYDIR%
adb pull /sdcard/any.pcap %DAILYDIR%

move %CurrentDir%\logcat.txt %DAILYDIR%
::move C:\rcs\demo.mp4 %DAILYDIR%
