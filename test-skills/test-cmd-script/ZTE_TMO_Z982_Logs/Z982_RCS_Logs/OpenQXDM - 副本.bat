adb root
adb wait-for-device
adb remount
adb wait-for-device


echo 将执行下面命令
echo adb shell setprop persist.sys.usb.config diag,adb

adb shell setprop persist.sys.usb.config diag,adb
pause

echo 将执行下面命令
echo adb shell setprop persist.sys.usb.config diag,serial_smd,rmnet_qti_bam,adb

adb shell setprop persist.sys.usb.config diag,serial_smd,rmnet_qti_bam,adb
pause

echo 将执行下面命令
echo adb shell sync

adb shell sync
pause
