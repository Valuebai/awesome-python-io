set pid=
for /f "tokens=2" %%i in ('adb shell ps^|findstr "logcat"') do (set pid="%%i")
if "%pid%" NEQ ""  (adb shell kill %pid%)


:: set str=""
:: set pid=
:: for /f "delims=" %%i in ('adb shell ps^|findstr "logcat"') do (set str="%%i")
:: if %str% NEQ ""  (for /f "tokens=1,*" %%a in (%str%) do (set str="%%b"))
:: if %str% NEQ ""  (for /f "tokens=1,*" %%a in (%str%) do (set pid=%%a))
:: if "%pid%" NEQ ""  (adb shell kill %pid%)
:: set str=""
:: set pid=
:: for /f "delims=" %%i in ('adb shell ps^|findstr "logcat"') do (set str="%%i")
:: if %str% NEQ ""  (for /f "tokens=1,*" %%a in (%str%) do (set str="%%b"))
:: if %str% NEQ ""  (for /f "tokens=1,*" %%a in (%str%) do (set pid=%%a))
:: if "%pid%" NEQ ""  (adb shell kill %pid%)