rem ���͸������ݵ���Ϣ

start adb_logcat.bat
start screen_record.bat

::================================::================================
::��ʱ1s,2s,3s,5s����,%Delay_1s%  
set Delay_1s=ping -n 1 127.1 >nul
set Delay_2s=ping -n 2 127.1 >nul
set Delay_3s=ping -n 3 127.1 >nul
set Delay_5s=ping -n 5 127.1 >nul
set Delay_7s=ping -n 7 127.1 >nul

::����ʱ������ %InputTime%
set Input_Time=adb shell input text "%time%"

::����ȷ�Ϸ��Ͱ�ť/�л������ť/¼����ť %Send_bottom%
set Send_mid=adb shell input tap 1000 1150
set Send_bottom=adb shell input tap 1000 1800

::��ס������¼����ť %Input_Record%
set Input_Record=adb shell input swipe 560 1800 560 1800 10000

::���������ť  %Click_Add%  %Add_PicVideo_one% Add=Attachment
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

::����Android Keycode  %KEYCODE_DPAD_DOWN%  %KEYCODE_ENTER%
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

::=======================================================ѡ��file�е�ͼƬ����
rem ѡ��file�е�ͼƬ����
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

::=======================================================ѡ��file�е���Ƶ����
rem ѡ��file�е���Ƶ����
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

::=======================================================ѡ��file�е���Ƶ����
rem ѡ��file�е���Ƶ����
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

::=======================================================ѡ��file�е�vcard����
rem ѡ��file�е�vcard����
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