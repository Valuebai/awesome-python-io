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

pause

adb shell rm -rf /data/data/com.suntek.mway.rcs.app.service/databases

adb shell rm -rf /data/anr

adb shell rm -rf /sdcard/Pictures/Screenshots

pause