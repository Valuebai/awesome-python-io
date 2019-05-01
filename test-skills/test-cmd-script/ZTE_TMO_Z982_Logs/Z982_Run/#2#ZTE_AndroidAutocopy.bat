set LOG_DIR=%cd%\TMO_Z982_ZTE_Logs\AndroidAutoCopyLog
FOR /L %%i in (1 1 1000) do (
if not exist %LOG_DIR%\adblog%%i\logcat\logcat_events.txt (
mkdir %LOG_DIR%\adblog%%i
call adb pull /cache/logs/ %LOG_DIR%\adblog%%i
call adb pull /sdcard/sd_logs/ %LOG_DIR%\adblog%%i\sd_logs_sdcard\
call adb pull /data/local/logs/sd_logs/ %LOG_DIR%\adblog%%i\sd_logs\
call explorer.exe %LOG_DIR%\adblog%%i
pause
exit
)
)



