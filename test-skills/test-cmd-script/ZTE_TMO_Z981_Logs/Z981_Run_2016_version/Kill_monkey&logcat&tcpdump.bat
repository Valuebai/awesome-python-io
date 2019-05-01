adb root
adb remount

adb shell "pid=`ps | grep tcpdump` && kill -9 $pid"

adb shell "pid=`ps | grep logcat` && kill -9 $pid"

adb shell "pid=`ps | grep monkey` && kill -9 $pid"
