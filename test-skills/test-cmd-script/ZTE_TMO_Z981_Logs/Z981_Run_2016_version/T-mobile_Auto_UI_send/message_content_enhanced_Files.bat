rem 发送各种内容的消息

start adb_logcat.bat
start screen_record.bat

::================================::================================
::延时1s,2s,3s,5s命令,%Delay_1s%  
set Delay_1s=ping -n 1 127.1 >nul
set Delay_2s=ping -n 2 127.1 >nul
set Delay_3s=ping -n 3 127.1 >nul
set Delay_5s=ping -n 5 127.1 >nul
set Delay_7s=ping -n 7 127.1 >nul

::输入时间命令 %InputTime%
set Input_Time=adb shell input text "%time%"

::最终确认发送按钮/切换输入框按钮/录音按钮 %Send_bottom%
set Send_mid=adb shell input tap 1000 1150
set Send_bottom=adb shell input tap 1000 1800

::按住输入框的录音按钮 %Input_Record%
set Input_Record=adb shell input swipe 560 1800 560 1800 10000

::点击附件按钮  %Click_Add%  %Add_PicVideo_one% Add=Attachment
set Click_Add=adb shell input tap 80 1800
set Add_PicVideo_one=adb shell input tap 300 290
set Add_PicVideo_two=adb shell input tap 660 290
set Add_PicVideo_ok=adb shell input tap 1005 150

set Add_AudioVcard_one=adb shell input tap 650 350
set Add_AudioVcard_two=adb shell input tap 650 540
set Add_AudioVcard_ok=adb shell input tap 1015 155

set Add_Files=adb shell input tap 288 1720
set Add_Files_Pic=adb shell input tap 176 520
set Add_Files_Pic_one=adb shell input tap 180 420
set Add_Files_Audio=adb shell input tap 540 520
set Add_Files_Audio_one=adb shell input tap 520 330
set Add_Files_Vedio=adb shell input tap 900 520
set Add_Files_Vedio_one=adb shell input tap 180 420
set Add_Files_Vcard=adb shell input tap 900 850
set Add_Files_Vcard_one=adb shell input tap 520 330

set Take_PicVideoAudio=adb shell input tap 540 1810
set Take_PicVideo_ok=adb shell input tap 960 1810
set Take_Audio_ok=adb shell input tap 835 1715

::设置Android Keycode  %KEYCODE_DPAD_DOWN%  %KEYCODE_ENTER%
set KEYCODE_HOME=adb shell input keyevent 3
set KEYCODE_BACK=adb shell input keyevent 4
set KEYCODE_CALL=adb shell input keyevent 5

set KEYCODE_DPAD_UP=adb shell input keyevent 19
set KEYCODE_DPAD_DOWN=adb shell input keyevent 20
set KEYCODE_DPAD_LEFT=adb shell input keyevent 21
set KEYCODE_DPAD_RIGHT=adb shell input keyevent 22
set KEYCODE_DPAD_CENTER=adb shell input keyevent 23
set KEYCODE_ENTER=adb shell input keyevent 66



:1

::=======================================================选择file中的图片发送
rem 选择file中的图片发送
rem tap attach button
%Click_Add%
%Delay_1s%

%Add_Files%
%Delay_3s%

rem select image
%Add_Files_Pic%
%Delay_3s%
rem select the first one
%Add_Files_Pic_one%
%Delay_3s%
%Send_bottom%
rem tap Send_bottom button
%Delay_3s%

::=======================================================选择file中的音频发送
rem 选择file中的音频发送
rem tap attach button
%Click_Add%
%Delay_1s%

%Add_Files%
%Delay_3s%

rem select audio
%Add_Files_Audio%
%Delay_3s%
rem select the first one
%Add_Files_Audio_one%
%Delay_3s%
%Send_bottom%
rem tap Send_bottom button
%Delay_3s%

::=======================================================选择file中的视频发送
rem 选择file中的视频发送
rem tap attach button
%Click_Add%
%Delay_1s%

%Add_Files%
%Delay_3s%

rem select video
%Add_Files_Vedio%
%Delay_3s%
rem select the first one
%Add_Files_Vedio_one%
%Send_bottom%
rem tap Send_bottom button
%Delay_3s%

::=======================================================选择file中的vcard发送
rem 选择file中的vcard发送
rem tap attach button
%Click_Add%
%Delay_1s%

%Add_Files%
%Delay_3s%

rem select documents
%Add_Files_Vcard%
%Delay_3s%
rem select the first one
%Add_Files_Vcard_one%
%Delay_3s%
%Send_bottom%
rem tap Send_bottom button
%Delay_3s%

goto 1