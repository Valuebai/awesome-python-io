adb wait-for-device
adb root
adb wait-for-device
adb remount
adb wait-for-device

adb pull /sdcard/logcat_all.txt %cd%

pause