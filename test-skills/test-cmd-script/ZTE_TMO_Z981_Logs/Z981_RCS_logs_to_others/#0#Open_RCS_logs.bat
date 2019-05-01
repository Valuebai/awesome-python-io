adb root
adb wait-for-device
adb remount
adb wait-for-device

adb shell setprop persist.sys.rcs.log.level 1
pause


::adb shell am broadcast -a com.suntek.mway.rcs.app.service.framework.ReloadLog

::adb shell am broadcast -a com.suntek.mway.rcs.app.service.ChangeLogLevel --ez isWriteFile true
