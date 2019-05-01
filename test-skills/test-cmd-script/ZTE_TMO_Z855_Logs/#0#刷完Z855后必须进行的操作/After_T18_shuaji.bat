adb wait-for-device
adb root
adb wait-for-device
adb remount
adb wait-for-device

pause

adb shell settings put global captive_portal_detection_enabled 0

adb shell setprop persist.sys.rcs.log.level 1
adb shell am broadcast -a com.suntek.mway.rcs.app.service.framework.ReloadLog

adb shell setprop persist.ims.disableADBLogs 0 
adb shell setprop persist.ims.disableDebugLogs 0 
adb shell setprop persist.ims.disableQXDMLogs 0
adb shell setprop persist.ims.disableIMSLogs 0 

adb shell settings put global captive_portal_detection_enabled 0

adb push 00001.vcf /sdcard/

adb install -r QQtongbuzhushou_1450.apk

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

adb reboot disemmcwp
