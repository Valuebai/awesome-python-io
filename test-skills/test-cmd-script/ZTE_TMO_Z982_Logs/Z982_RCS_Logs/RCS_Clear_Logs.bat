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

adb shell rm -rf /sdcard/Android/data/com.suntek.mway.rcs.app.plugin/

adb shell rm -rf /data/data/com.suntek.mway.rcs.app.service/databases/

adb shell rm -rf /data/anr/

adb shell rm -rf data/data/com.android.providers.telephony/databases/
adb shell rm -rf data/data/com.suntek.mway.rcs.app.service/databases/
adb shell rm -rf /data/data/com.android.providers.contacts/databases/

adb shell rm -rf /data/tombstones/
adb shell rm -rf /data/log/core/

echo device will reboot
pause

adb reboot