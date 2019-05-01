adb wait-for-device
adb root
adb wait-for-device
adb remount

ping -n 1 127.1 >nul

:1
adb shell "tcpdump -i any -s 0 -w /sdcard/any.pcap &"
goto 1

pause