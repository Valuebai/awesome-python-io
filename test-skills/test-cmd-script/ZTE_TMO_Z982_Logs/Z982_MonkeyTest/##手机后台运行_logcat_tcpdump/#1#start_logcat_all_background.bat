adb wait-for-device
adb root
adb wait-for-device
adb remount

ping -n 1 127.1 >nul

:1
adb shell "logcat -v time >/sdcard/logcat_all.txt &"
goto 1

pause