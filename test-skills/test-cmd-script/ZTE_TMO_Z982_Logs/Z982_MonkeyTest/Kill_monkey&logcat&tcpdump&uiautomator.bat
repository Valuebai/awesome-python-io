adb wait-for-device
adb root
adb wait-for-device
adb remount
adb wait-for-device

adb shell "pid=`ps | grep uiautomator` && kill -9 $pid"

adb shell "pid=`ps | grep tcpdump` && kill -9 $pid"

adb shell "pid=`ps | grep logcat` && kill -9 $pid"

adb shell "pid=`ps | grep monkey` && kill -9 $pid"

adb shell "pid=`ps | grep uiautomator` && kill -9 $pid"

adb shell "pid=`ps | grep tcpdump` && kill -9 $pid"

adb shell "pid=`ps | grep logcat` && kill -9 $pid"

adb shell "pid=`ps | grep monkey` && kill -9 $pid"


pause