adb wait-for-device
adb root
adb wait-for-device
adb remount
adb wait-for-device
:: get current flord path.
:: remove service config file.

::设置当前路径
set CurrentDir=%cd%

::定义变量DAILYDIR为当前时间值
set i=1
set DAILYDIR=%cd%\zAllLogs_[description][time][version]

set DAILYDIR_slog=%cd%\zAllLogs_[description][time][version]\slog
set DAILYDIR_dropbox=%cd%\zAllLogs_[description][time][version]\dropbox
set DAILYDIR_tombstones=%cd%\zAllLogs_[description][time][version]\tombstones
set DAILYDIR_core=%cd%\zAllLogs_[description][time][version]\core
set DAILYDIR_anr=%cd%\zAllLogs_[description][time][version]\anr

echo %DAILYDIR%

echo "%date%%time% start to exec"

::-------------mkdir Folder--------------------------
::if not exist %DAILYDIR% md %DAILYDIR%
if exist %cd%\zAllLogs_[description][time][version] (
echo the files exist!!
echo the files exist!!
echo the files exist!!
echo zAllLogs_[description][time][version] exist!!
echo zAllLogs_[description][time][version] exist!!
echo zAllLogs_[description][time][version] exist!!
echo zAllLogs_[description][time][version] exist!!
echo zAllLogs_[description][time][version] exist!!
echo zAllLogs_[description][time][version] exist!!
echo please rename it!!
echo please rename it!!
echo please rename it!!
echo please rename it!!
echo please rename it!!
echo please rename it!!
pause
pause
pause

if exist %cd%\zAllLogs_[description][time][version] exit
) else (
md %DAILYDIR%
)
::-------------mkdir Folder--------------------------
echo %DAILYDIR%

cd %DAILYDIR%


adb pull /sdcard/any.pcap %DAILYDIR%

adb pull /sdcard/Android/data/com.suntek.mway.rcs.app.service/ %DAILYDIR%
adb pull /sdcard/Android/data/com.suntek.mway.rcs.app.plugin/ %DAILYDIR%

adb pull data/data/com.android.providers.telephony/databases/mmssms.db %DAILYDIR%
adb pull data/data/com.suntek.mway.rcs.app.service/databases/rcs.db %DAILYDIR%
adb pull /data/data/com.android.providers.contacts/databases/profile.db %DAILYDIR%
adb pull /data/data/com.android.providers.contacts/databases/contacts2.db %DAILYDIR%
::contacts太大，需要时再打开

adb pull /sdcard/zdemo.mp4 %DAILYDIR%

::拉开机日志

if exist %cd%\zAllLogs_[description][time][version]\anr exit
) else (
md %DAILYDIR_anr%
)
adb pull /data/anr %DAILYDIR_anr%
cd ..


if exist %cd%\zAllLogs_[description][time][version]\core exit
) else (
md %DAILYDIR_core%
)
adb pull /data/log/core %DAILYDIR_core%
cd ..


if exist %cd%\zAllLogs_[description][time][version]\tombstones exit
) else (
md %DAILYDIR_tombstones%
)
adb pull /data/tombstones %DAILYDIR_tombstones%
cd ..


if exist %cd%\zAllLogs_[description][time][version]\dropbox exit
) else (
md %DAILYDIR_dropbox%
)
adb pull /data/system/dropbox %DAILYDIR_dropbox%
cd ..


if exist %cd%\zAllLogs_[description][time][version]\slog exit
) else (
md %DAILYDIR_slog%
)
adb pull /data/slog %DAILYDIR_slog%
cd ..

::adb pull /sdcard/Pictures/Screenshots %DAILYDIR%

move %CurrentDir%\logcat.txt %DAILYDIR%
move %CurrentDir%\log_radio.txt %DAILYDIR%
move %CurrentDir%\log_events.txt %DAILYDIR%
move %CurrentDir%\log_system.txt %DAILYDIR%
move %CurrentDir%\log_kmsg.txt %DAILYDIR%
move %CurrentDir%\log_bugreport.txt %DAILYDIR%
move %CurrentDir%\log_dmesg_kernel.txt %DAILYDIR%

echo "press any key to exit"
pause
