adb root
adb remount

adb shell "pid=`ps | grep monkey` && kill -9 $pid"
