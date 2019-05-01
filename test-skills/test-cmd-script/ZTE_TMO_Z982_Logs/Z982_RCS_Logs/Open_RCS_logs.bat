adb root
adb wait-for-device
adb remount
adb wait-for-device

echo 将执行下面命令
echo adb shell setprop persist.sys.rcs.log.level 1

adb shell setprop persist.sys.rcs.log.level 1
pause

echo 将执行下面命令
echo adb shell am broadcast -a com.suntek.mway.rcs.ACTION_SET_RCS_ENABLED —ei enabled 1

adb shell am broadcast -a com.suntek.mway.rcs.ACTION_SET_RCS_ENABLED —ei enabled 1

pause

::adb shell am broadcast -a com.suntek.mway.rcs.app.service.framework.ReloadLog

::adb shell am broadcast -a com.suntek.mway.rcs.app.service.ChangeLogLevel --ez isWriteFile true
