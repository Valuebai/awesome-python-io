:: 功能：杀掉手机运行的 uiautomator、tcpdump、logcat、monkey、screenrecord进程
:: 使用：直接双击执行
:: from: lhb, 2017-05-23


adb wait-for-device
adb root
adb wait-for-device
adb remount
adb wait-for-device

adb shell "pid=`ps | grep uiautomator` && kill -9 $pid"

adb shell "pid=`ps | grep tcpdump` && kill -9 $pid"

adb shell "pid=`ps | grep logcat` && kill -9 $pid"

adb shell "pid=`ps | grep monkey` && kill -9 $pid"

adb shell "pid=`ps | grep screenrecord` && kill -9 $pid"


::================================================================

adb shell "pid=`ps | grep uiautomator` && kill -9 $pid"

adb shell "pid=`ps | grep tcpdump` && kill -9 $pid"

adb shell "pid=`ps | grep logcat` && kill -9 $pid"

adb shell "pid=`ps | grep monkey` && kill -9 $pid"

adb shell "pid=`ps | grep screenrecord` && kill -9 $pid"


pause