adb root
adb wait-for-device
adb remount
adb wait-for-device

rem ��rcs��־
adb shell setprop persist.sys.rcs.log.level 1

start Push_Test_files_To_Phone.bat
start T-mobile_Add_contacts.bat