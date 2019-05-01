rem test
@echo off

ECHO -------------------------------------

ECHO.        Analysis logcat log                

ECHO.           AUTHOR:YWH                      

ECHO.           Version:V1.0                    

ECHO.         Time:2016.08.17                  

ECHO --------------------------------------

if exist error_detail.txt del /F error_detail.txt



ECHO -----------start analysis---------------


for /f "delims=" %%i in ('Dir /s /b /a-d *.log') do (
type "%%i"|Findstr /M /I "fatal exception" && echo "%%i" >>error_detail.txt
type "%%i"|Findstr /N /I "fatal exception" >>error_detail.txt
)

ECHO -----------finish analysis---------------



start error_detail.txt

pause