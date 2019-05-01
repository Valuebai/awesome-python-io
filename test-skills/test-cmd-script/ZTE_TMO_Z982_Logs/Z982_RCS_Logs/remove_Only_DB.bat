adb wait-for-device
adb root
adb wait-for-device
adb remount
adb wait-for-device
:: get current flord path.
:: remove service config file.



adb shell rm -rf data/user_de/0/com.android.providers.telephony/databases/mmssms.db
adb shell rm -rf data/data/com.android.messaging/databases

pause

adb reboot