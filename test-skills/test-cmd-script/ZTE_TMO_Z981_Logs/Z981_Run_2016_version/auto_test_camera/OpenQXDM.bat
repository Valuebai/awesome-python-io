adb root
adb wait-for-device
adb remount
adb wait-for-device

adb shell setprop persist.sys.usb.config diag,adb
pause

adb shell setprop persist.sys.usb.config diag,serial_smd,rmnet_qti_bam,adb
pause

adb shell sync
pause
