adb wait-for-device
adb root
adb wait-for-device
adb remount
adb wait-for-device
:: get current flord path.
:: remove service config file.

set DAILYDIR=%cd%\DB
echo %DAILYDIR%
echo "%date%%time% start to exec"

::-------------mkdir Folder--------------------------
if not exist %DAILYDIR% md %DAILYDIR%
cd %DAILYDIR%

::7.0的路径
adb pull /data/user_de/0/com.android.providers.telephony/databases/mmssms.db mmssms.db %DAILYDIR%
adb pull data/data/com.android.messaging/databases %DAILYDIR%

::6.0的路径
::adb pull data/data/com.android.providers.telephony/databases/mmssms.db %DAILYDIR%

adb pull data/data/com.suntek.mway.rcs.app.service/databases/rcs.db %DAILYDIR%

adb pull /data/data/com.android.providers.contacts/databases/contacts2.db %DAILYDIR%

adb pull /data/data/com.android.providers.contacts/databases/profile.db %DAILYDIR%
