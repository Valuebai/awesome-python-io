set DAILYDIR=%cd%\%DATE:~6,10%
echo %DAILYDIR%

start screen_record.bat

adb shell monkey -p com.android.mms --throttle 300 -s 300 --ignore-crashes --ignore-timeouts --ignore-security-exceptions --ignore-native-crashes --monitor-native-crashes --pct-syskeys 0 -v -v -v 900000 > G:\Run\MonkeyTest/zmonkey_log_20160829.txt
