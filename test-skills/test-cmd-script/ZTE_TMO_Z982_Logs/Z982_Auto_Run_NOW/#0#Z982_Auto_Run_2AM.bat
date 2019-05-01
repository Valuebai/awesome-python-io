@echo ******************** >>%cd%\TestResult.txt
@echo	 DailyAutoTest >>%cd%\TestResult.txt
@echo ******************** >>%cd%\TestResult.txt

::===========================================================
@echo Run now...
@start Z982_Screen_Record_3min_pull.bat
@echo %date%%time% take video>>%cd%\TestResult.txt
:StartTime
@set StartTime=%time:~0,2%%time:~3,2%
::@echo %StartTime% 

::====================================================
::开启运行脚本
:Run
@echo %date%%time% auto run >>%cd%\TestResult.txt
@echo timeout /t 5
@echo ********************
@echo	   start run 
@echo ********************

goto UnlockPhone
:RunOK
::记录当前路径
@echo path:%cd%
@set dir=%cd%
set flag=0

:RunBat
::进入Z盘下自动编译好的代码路径
cd F:\luhuibo\Z982_Auto_Run
@F:
::启动里面的install脚本安装版本
@echo path:%cd%
call #1#Z982_Run.bat
set Z982_Run_Time=%time:~0,2%%time:~3,2%
set /a flag=%flag%+1
::返回这个脚本的所以路径，如有移动脚本，修改f:盘为其他盘
cd %dir%
@f:
@echo path:%cd%

echo flag=====%flag%
@if %flag% equ 1 (goto RunBat) else @echo no
@if %flag% equ 2 (goto RunBat) else @echo 222no
@if %flag% equ 3 (goto ReBoot) else @echo 333no

pause

::goto Analyze
::goto Timeout


::====================================================
::重启手机后运行Run
:ReBoot

@echo %date%%time% devices reboot>>Z:\build_tmo_version\DailyTestResult.txt
adb reboot
timeout /t 30
goto Run

::====================================================
::如果时间到了1个小时，重启手机
:Timeout

set Timeout_Time=%time:~0,2%%time:~3,2%
set set /a Diff=%Timeout_Time%-%Z982_Run_Time%
timeout /t 10
if %Diff% leq 70 (echo 1) else (@goto 重启手机)

pause

::====================================================
::搜索RCS_Logs_AutoRun中的日志
::输出结果到Z:\build_tmo_version\DailyTestResult.txt
:Analyze

@echo %date%%time% devices pull logs and analyze >>Z:\build_tmo_version\DailyTestResult.txt
@echo ********************************** >>Z:\build_tmo_version\DailyTestResult.txt
cd F:\luhuibo\Z982_Auto_Run
call #2#After_Run_Pull_logs_ToSave.bat
timeout /t 18
::分析的操作

@echo ********************************** >>Z:\build_tmo_version\DailyTestResult.txt
@echo %date%的RCS版本自动测试通过，日志未发现异常 >>Z:\build_tmo_version\DailyTestResult.txt
@echo ********************************** >>Z:\build_tmo_version\DailyTestResult.txt
::
adb shell rm -rf /sdcard/Android/data/com.suntek.mway.rcs.app.service/logs/
goto ReBoot

::====================================================
:: 解锁手机
:UnlockPhone
rem 按电源键
adb shell input keyevent 26
ping -n 2 127.1 >nul
rem 解锁
adb shell input keyevent 82
ping -n 2 127.1 >nul
adb shell input swipe 540 1800 540 1800 6000
rem 按home键
adb shell input keyevent 3
ping -n 1 127.1 >nul

goto RunOK