rem �ڵ�ǰ�Ľ�������ѭ�����͸������ݵ���Ϣ����Ҫ��ĳ�����棩

start adb_logcat.bat
start screen_record.bat

::================================::================================
::��ʱ1s,2s,3s,5s����,%Delay_1s%  
set Delay_1s=ping -n 1 127.1 >nul
set Delay_2s=ping -n 2 127.1 >nul
set Delay_3s=ping -n 3 127.1 >nul
set Delay_5s=ping -n 5 127.1 >nul
set Delay_7s=ping -n 7 127.1 >nul
set Delay_10s=ping -n 10 127.1 >nul

::����ʱ������ %InputTime%
set Input_Time=adb shell input text "%time%"

::����ȷ�Ϸ��Ͱ�ť/�л������ť/¼����ť %Send_bottom%
set Send_mid=adb shell input tap 1000 1150
set Send_bottom=adb shell input tap 1000 1800
set Send_msg_all_shurufa_up=adb shell input tap 980 720

::��ס������¼����ť %Input_Record%
set Input_Record=adb shell input swipe 560 1800 560 1800 10000

::���������ť  %Click_Add%  %Add_PicVideo_1% Add=Attachment
set Click_Add=adb shell input tap 80 1800
set Add_PicVideo_1=adb shell input tap 300 290
set Add_PicVideo_2=adb shell input tap 660 290
set Add_PicVideo_3=adb shell input tap 1005 290
set Add_PicVideo_4=adb shell input tap 300 690
set Add_PicVideo_5=adb shell input tap 660 690
set Add_PicVideo_6=adb shell input tap 1005 690
set Add_PicVideo_ok=adb shell input tap 1005 150

set Add_AudioVcard_1=adb shell input tap 650 350
set Add_AudioVcard_2=adb shell input tap 650 540
set Add_AudioVcard_3=adb shell input tap 650 730
set Add_AudioVcard_4=adb shell input tap 650 920
set Add_AudioVcard_5=adb shell input tap 650 1110
set Add_AudioVcard_6=adb shell input tap 650 1300
set Add_AudioVcard_ok=adb shell input tap 1015 155

set Add_Files=adb shell input tap 288 1720
set Add_Files_Pic=adb shell input tap 176 520
set Add_Files_Vedio=adb shell input tap 900 520
set Add_Files_PicVedio_1=adb shell input tap 180 420
set Add_Files_PicVedio_2=adb shell input tap 520 420
set Add_Files_PicVedio_3=adb shell input tap 880 420
set Add_Files_PicVedio_4=adb shell input tap 180 840
set Add_Files_PicVedio_5=adb shell input tap 520 840
set Add_Files_PicVedio_6=adb shell input tap 880 840

set Add_Files_Audio=adb shell input tap 540 520
set Add_Files_Vcard=adb shell input tap 900 850

set Add_Files_AudioVcard_1=adb shell input tap 520 330
set Add_Files_AudioVcard_2=adb shell input tap 520 530
set Add_Files_AudioVcard_3=adb shell input tap 520 730
set Add_Files_AudioVcard_4=adb shell input tap 520 930
set Add_Files_AudioVcard_5=adb shell input tap 520 1130
set Add_Files_AudioVcard_6=adb shell input tap 520 1330

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

::=============================���뵱ǰ���ں�ʱ�䷢��
rem ���뵱ǰ���ڲ�����
%Delay_2s%
%Input_Time%
%Delay_2s%  
%Send_bottom%
%Delay_2s%

::=============================���뵱ǰ���ں�ʱ�䷢��
rem �ٴ����뵱ǰ���ں�ʱ�䷢��
%Delay_2s%
%Input_Time%
%Delay_2s% 
%Send_bottom%
%Delay_2s% 

::=======================================================����¼�Ƶ���Ƶ1
rem ����¼�Ƶ���Ƶ
%Delay_1s% 
%Send_bottom%
rem ���¼����ť
%Delay_2s% 
%Input_Record%
%Delay_3s% 

::=======================================================����¼�Ƶ���Ƶ2
rem ���¼����ť
%Delay_1s% 
%Input_Record%
%Delay_3s% 

::=======================================================ѡ��2��ͼƬ������
rem �������
%Click_Add% 
%Delay_1s% 
rem �����ƶ�
%KEYCODE_DPAD_DOWN%
rem �س�ѡ��
%KEYCODE_ENTER%
%Delay_3s% 

rem select the first one
%Add_PicVideo_1%
%Delay_2s% 
rem select the second one
%Add_PicVideo_2%
%Delay_2s% 

rem tap ok button
%Add_PicVideo_ok%
%Delay_2s% 
rem tap Send_bottom button
%Send_bottom%
%Delay_3s% 


::=======================================================ѡ��������Ƭ������1
rem ѡ��������Ƭ������
rem tap attach button
%Click_Add%
%Delay_1s% 
rem �����ƶ�
%KEYCODE_DPAD_DOWN%
rem �����ƶ�
%KEYCODE_DPAD_DOWN%
rem �س�ѡ��
%KEYCODE_ENTER%
%Delay_3s%
rem ������հ�ť
%Take_PicVideoAudio%
%Delay_3s%
rem ���ȷ�ϰ�ť
%Take_PicVideo_ok%
%Delay_3s%
rem tap Send_bottom buttom
%Send_bottom%
%Delay_3s%

::=======================================================ѡ��������Ƭ������2
rem ѡ��������Ƭ������
rem tap attach button
%Click_Add%
%Delay_1s% 
rem �����ƶ�
%KEYCODE_DPAD_DOWN%
rem �����ƶ�
%KEYCODE_DPAD_DOWN%
rem �س�ѡ��
%KEYCODE_ENTER%
%Delay_3s%
rem ������հ�ť
%Take_PicVideoAudio%
%Delay_3s%
rem ���ȷ�ϰ�ť
%Take_PicVideo_ok%
%Delay_3s%
rem tap Send_bottom buttom
%Send_bottom%
%Delay_3s%


::=======================================================ѡ��2����Ƶ������  
rem ѡ����Ƶ������
%Click_Add%
rem tap attach button
%Delay_1s%
%KEYCODE_DPAD_DOWN%
rem �����ƶ�
%KEYCODE_DPAD_DOWN%
rem �����ƶ�
%KEYCODE_DPAD_DOWN%
rem �����ƶ�
%KEYCODE_ENTER%
rem �س�ѡ��

rem select the first one
%Delay_3s%
%Add_PicVideo_1%
rem select the second one
%Delay_3s%
%Add_PicVideo_2%
rem tap ok button
%Delay_3s%
%Add_PicVideo_ok%
rem tap Send_bottom button
%Delay_3s%
%Send_bottom%
%Delay_3s%

::=======================================================ѡ��������Ƶ������1
rem ѡ��������Ƶ������
rem tap attach button
%Click_Add%
%Delay_1s%

rem �����ƶ�
%KEYCODE_DPAD_DOWN%
rem �����ƶ�
%KEYCODE_DPAD_DOWN%
rem �����ƶ�
%KEYCODE_DPAD_DOWN%
rem �����ƶ�
%KEYCODE_DPAD_DOWN%
rem �س�ѡ��
%KEYCODE_ENTER%
%Delay_3s%

rem ������㰴ť
%Take_PicVideoAudio%
%Delay_7s%
rem ���ֹͣ����
%Take_PicVideoAudio%
%Delay_3s%
rem ���ȷ�ϰ�ť
%Take_PicVideo_ok%
%Delay_3s%
%Send_bottom%
rem tap Send_bottom button
%Delay_3s%

::=======================================================ѡ��������Ƶ������2
rem ѡ��������Ƶ������
rem tap attach button
%Click_Add%
%Delay_1s%

rem �����ƶ�
%KEYCODE_DPAD_DOWN%
rem �����ƶ�
%KEYCODE_DPAD_DOWN%
rem �����ƶ�
%KEYCODE_DPAD_DOWN%
rem �����ƶ�
%KEYCODE_DPAD_DOWN%
rem �س�ѡ��
%KEYCODE_ENTER%
%Delay_3s%

rem ������㰴ť
%Take_PicVideoAudio%
%Delay_7s%
rem ���ֹͣ����
%Take_PicVideoAudio%
%Delay_3s%
rem ���ȷ�ϰ�ť
%Take_PicVideo_ok%
%Delay_3s%
%Send_bottom%
rem tap Send_bottom button
%Delay_3s%

::=======================================================ѡ��2����Ƶ������
rem ѡ������Ƶ������
rem tap attach button
%Click_Add%
%Delay_1s%

rem �����ƶ�
%KEYCODE_DPAD_DOWN%
rem �����ƶ�
%KEYCODE_DPAD_DOWN%
rem �����ƶ�
%KEYCODE_DPAD_DOWN%
rem �����ƶ�
%KEYCODE_DPAD_DOWN%
rem �����ƶ�
%KEYCODE_DPAD_DOWN%
rem �س�ѡ��
%KEYCODE_ENTER%

rem select the first one
%Delay_3s%
%Add_AudioVcard_1%
rem select the second one
%Delay_3s%
%Add_AudioVcard_2%
rem tap ok button
%Delay_3s%
%Add_AudioVcard_ok%
rem tap Send_bottom button
%Delay_3s%
%Send_bottom%
%Delay_3s%


::=======================================================ѡ��¼����Ƶ������1
rem ѡ��¼����Ƶ������
%Click_Add%
%Delay_1s%

rem �����ƶ�
%KEYCODE_DPAD_DOWN%
rem �����ƶ�
%KEYCODE_DPAD_DOWN%
rem �����ƶ�
%KEYCODE_DPAD_DOWN%
rem �����ƶ�
%KEYCODE_DPAD_DOWN%
rem �����ƶ�
%KEYCODE_DPAD_DOWN%
rem �����ƶ�
%KEYCODE_DPAD_DOWN%
rem �س�ѡ��
%KEYCODE_ENTER%
%Delay_3s%

rem �����ʼ��ť
%Take_PicVideoAudio%
%Delay_7s%
rem ���ֹͣ
%Take_Audio_ok%
%Delay_3s%
rem tap Send_bottom button
%Send_bottom%
%Delay_3s%

::=======================================================ѡ��¼����Ƶ������2
rem ѡ��¼����Ƶ������
%Click_Add%
%Delay_1s%

rem �����ƶ�
%KEYCODE_DPAD_DOWN%
rem �����ƶ�
%KEYCODE_DPAD_DOWN%
rem �����ƶ�
%KEYCODE_DPAD_DOWN%
rem �����ƶ�
%KEYCODE_DPAD_DOWN%
rem �����ƶ�
%KEYCODE_DPAD_DOWN%
rem �����ƶ�
%KEYCODE_DPAD_DOWN%
rem �س�ѡ��
%KEYCODE_ENTER%
%Delay_3s%

rem �����ʼ��ť
%Take_PicVideoAudio%
%Delay_7s%
rem ���ֹͣ
%Take_Audio_ok%
%Delay_3s%
rem tap Send_bottom button
%Send_bottom%
%Delay_3s%

::=======================================================ѡ��2��v-card������  
rem tap attach button
%Click_Add%
%Delay_1s%

rem �����ƶ�
%KEYCODE_DPAD_DOWN%
rem �����ƶ�
%KEYCODE_DPAD_DOWN%
rem �����ƶ�
%KEYCODE_DPAD_DOWN%
rem �����ƶ�
%KEYCODE_DPAD_DOWN%
rem �����ƶ�
%KEYCODE_DPAD_DOWN%
rem �����ƶ�
%KEYCODE_DPAD_DOWN%
rem �����ƶ�
%KEYCODE_DPAD_DOWN%
rem �����ƶ�
%KEYCODE_DPAD_DOWN%
rem �����ƶ�
%KEYCODE_DPAD_DOWN%

rem �س�ѡ��
%KEYCODE_ENTER%

rem select the first one
%Delay_3s%
%Add_AudioVcard_1%

rem select the second one
%Delay_3s%
%Add_AudioVcard_2%

rem tap ok button
%Delay_3s%
%Add_AudioVcard_ok%

rem tap Send_bottom button
%Delay_3s%
%Send_bottom%
%Delay_3s%

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
%Add_Files_PicVedio_1%
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
%Add_Files_AudioVcard_1%
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
%Add_Files_PicVedio_1%
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
%Add_Files_AudioVcard_1%
%Delay_3s%
%Send_bottom%
rem tap Send_bottom button
%Delay_3s%





goto 1