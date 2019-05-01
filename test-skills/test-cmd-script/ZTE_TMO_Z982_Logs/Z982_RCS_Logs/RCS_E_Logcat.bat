adb wait-for-device
adb root
adb wait-for-device
adb remount
adb wait-for-device
:: get current flord path.
:: remove service config file.

adb logcat *:E >E_logcat.txt

