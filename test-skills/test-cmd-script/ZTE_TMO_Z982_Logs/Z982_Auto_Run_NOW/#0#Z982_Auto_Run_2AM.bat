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
::�������нű�
:Run
@echo %date%%time% auto run >>%cd%\TestResult.txt
@echo timeout /t 5
@echo ********************
@echo	   start run 
@echo ********************

goto UnlockPhone
:RunOK
::��¼��ǰ·��
@echo path:%cd%
@set dir=%cd%
set flag=0

:RunBat
::����Z�����Զ�����õĴ���·��
cd F:\luhuibo\Z982_Auto_Run
@F:
::���������install�ű���װ�汾
@echo path:%cd%
call #1#Z982_Run.bat
set Z982_Run_Time=%time:~0,2%%time:~3,2%
set /a flag=%flag%+1
::��������ű�������·���������ƶ��ű����޸�f:��Ϊ������
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
::�����ֻ�������Run
:ReBoot

@echo %date%%time% devices reboot>>Z:\build_tmo_version\DailyTestResult.txt
adb reboot
timeout /t 30
goto Run

::====================================================
::���ʱ�䵽��1��Сʱ�������ֻ�
:Timeout

set Timeout_Time=%time:~0,2%%time:~3,2%
set set /a Diff=%Timeout_Time%-%Z982_Run_Time%
timeout /t 10
if %Diff% leq 70 (echo 1) else (@goto �����ֻ�)

pause

::====================================================
::����RCS_Logs_AutoRun�е���־
::��������Z:\build_tmo_version\DailyTestResult.txt
:Analyze

@echo %date%%time% devices pull logs and analyze >>Z:\build_tmo_version\DailyTestResult.txt
@echo ********************************** >>Z:\build_tmo_version\DailyTestResult.txt
cd F:\luhuibo\Z982_Auto_Run
call #2#After_Run_Pull_logs_ToSave.bat
timeout /t 18
::�����Ĳ���

@echo ********************************** >>Z:\build_tmo_version\DailyTestResult.txt
@echo %date%��RCS�汾�Զ�����ͨ������־δ�����쳣 >>Z:\build_tmo_version\DailyTestResult.txt
@echo ********************************** >>Z:\build_tmo_version\DailyTestResult.txt
::
adb shell rm -rf /sdcard/Android/data/com.suntek.mway.rcs.app.service/logs/
goto ReBoot

::====================================================
:: �����ֻ�
:UnlockPhone
rem ����Դ��
adb shell input keyevent 26
ping -n 2 127.1 >nul
rem ����
adb shell input keyevent 82
ping -n 2 127.1 >nul
adb shell input swipe 540 1800 540 1800 6000
rem ��home��
adb shell input keyevent 3
ping -n 1 127.1 >nul

goto RunOK