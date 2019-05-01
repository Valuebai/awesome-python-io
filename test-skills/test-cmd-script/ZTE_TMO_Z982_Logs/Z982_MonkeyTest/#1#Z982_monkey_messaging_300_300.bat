::功能：跑monkey测试
::使用：直接双击这个bat脚本
::from: lhb,2017-05-19

adb wait-for-device
adb root
adb wait-for-device
adb remount
adb wait-for-device

adb shell monkey -p com.android.messaging --ignore-crashes --ignore-timeouts --ignore-security-exceptions --pct-trackball 0 --pct-nav 0 --pct-majornav 0 --pct-anyevent 0 -v -v -v --throttle 300 -s 300 1200000000 > monkeylifecenter.log

::monkey -p 包 名 --ignore-crashes --ignore-timeouts --ignore-security-exceptions --pct-trackball 0 --pct-nav 0 --pct-majornav 0 --pct-anyevent 0 -v -v -v --throttle 500 1200000000 > /mnt/sdcard/monkeylifecenter.log 2>&1 &
