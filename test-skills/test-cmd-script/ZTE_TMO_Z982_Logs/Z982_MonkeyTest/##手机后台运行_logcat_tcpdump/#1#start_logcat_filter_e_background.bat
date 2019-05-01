adb wait-for-device
adb root
adb wait-for-device
adb remount

ping -n 1 127.1 >nul

:1
adb shell "logcat *:E >/sdcard/logcat_filter_e.txt &"
goto 1

pause