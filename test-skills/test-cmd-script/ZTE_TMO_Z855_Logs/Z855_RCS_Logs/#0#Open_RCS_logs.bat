adb wait-for-device
adb root
adb wait-for-device
adb remount
adb wait-for-device

adb shell setprop persist.sys.rcs.log.level 1
::adb shell am broadcast -a com.suntek.mway.rcs.ACTION_SET_RCS_ENABLED —ei enabled 1

reboot

