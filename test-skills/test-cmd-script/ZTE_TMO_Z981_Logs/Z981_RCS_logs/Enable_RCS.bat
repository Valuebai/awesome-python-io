adb root
adb wait-for-device
adb remount
adb wait-for-device

adb shell am broadcast -a com.suntek.mway.rcs.ACTION_SET_RCS_ENABLED —ei enabled 1

pause

adb shell setprop persist.sys.rcs.enabled 1

pause