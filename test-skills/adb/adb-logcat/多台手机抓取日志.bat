adb wait-for-device
adb root
adb wait-for-device
adb remount
adb wait-for-device
:: get current flord path.
:: remove service config file.

echo ����ץȡ�ֻ���־���豸��
pause

set DAILYDIR=%cd%\Logs_�豸

::1_848ecafd �Ƕ�Ӧ���豸�ţ���ע���޸�

adb -s 1_848ecafd pull /sdcard/Pictures/Screenshots %DAILYDIR%

adb -s 1_848ecafd pull /sdcard//Android/data/com.suntek.mway.rcs.app.service/ %DAILYDIR%

adb -s 1_848ecafd logcat -v time >logcat.txt

adb -s 1_848ecafd shell dumpsys meminfo | find "mms"
adb -s 1_848ecafd shell dumpsys cpuinfo | find "mms"





















