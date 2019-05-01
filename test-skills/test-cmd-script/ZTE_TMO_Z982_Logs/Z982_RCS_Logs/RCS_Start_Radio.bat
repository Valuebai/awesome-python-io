adb wait-for-device
adb root
adb wait-for-device
adb remount
adb wait-for-device
:: get current flord path.
:: remove service config file.


::Radio Log
adb logcat -b radio -v time > log_radio.txt
