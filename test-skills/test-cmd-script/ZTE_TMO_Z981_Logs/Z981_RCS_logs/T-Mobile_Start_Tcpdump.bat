adb wait-for-device
adb root
adb wait-for-device
adb remount
adb wait-for-device
:: get current flord path.
:: remove service config file.

adb shell tcpdump -i any -s 0 -w /sdcard/any.pcap
