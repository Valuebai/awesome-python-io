adb wait-for-device
adb root
adb wait-for-device
adb remount
adb wait-for-device
:: get current flord path.
:: remove service config file.


echo These commands will clear the logs, please do it carefully!


pause

adb shell rm -rf /sdcard/Android/data/com.suntek.mway.rcs.app.service/logs/

adb shell rm -rf /data/data/com.suntek.mway.rcs.app.service/databases

pause