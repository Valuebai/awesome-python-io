rem 在当前的界面中死循环发送900+文本和1000+文本（需要打开某个界面）
rem 发送大图片、视频和附件的时候需要重命名，在前面加上@

start adb_logcat.bat
start screen_record.bat

::================================::================================
::延时1s,2s,3s,5s命令,%Delay_1s%  
set Delay_1s=ping -n 1 127.1 >nul
set Delay_2s=ping -n 2 127.1 >nul
set Delay_3s=ping -n 3 127.1 >nul
set Delay_5s=ping -n 5 127.1 >nul
set Delay_7s=ping -n 7 127.1 >nul
set Delay_10s=ping -n 10 127.1 >nul

::最终确认发送按钮/切换输入框按钮/录音按钮 %Send_bottom%
set Send_mid=adb shell input tap 1000 1150
set Send_bottom=adb shell input tap 1000 1800
set Send_msg_all_shurufa_up=adb shell input tap 980 720

::按住输入框的录音按钮 %Input_Record%
set Input_Record=adb shell input swipe 560 1800 560 1800 10000

::点击附件按钮  %Click_Add%  %Add_PicVideo_1% Add=Attachment
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


set text1=" @@@#@#@#@##@#@#=!!!???,,,,======___---\\\\*****(((()))))^^^^^%%%%%$$$$$::::{}{}{}[][][][@@@#@#@#@##@#@#=!!!???,,,,======___---\\\\*****(((()))))^^^^^%%%%%$$$$$::::{}{}{}[][][][@@@#@#@#@##@#@#=!!!???,,,,======___---\\\\*****(((()))))^^^^^%%%%%$$$$$::::{}{}{}[][][][@@@#@#@#@##@#@#=!!!???,,,,======___---\\\\*****(((()))))^^^^^%%%%%$$$$$::::{}{}{}[][][][@@@#@#@#@##@#@#=!!!???,,,,======___---\\\\*****(((()))))^^^^^%%%%%$$$$$::::{}{}{}[][][]"

set text2="[12312343546567576787809809876543245876543213456743212245798231234354656757678780980987654324587654321345674321224579843245768934523556787654333333333333333333[1231234354656757678780980987654324587654321345674321224579823123435465675767878098098765432458765432134567432122457984324576893452355678765433333333333333333333"

::输入时间命令 %InputTime%
set Input_Time=adb shell input text "%time%"
set Input_900byte=adb shell input text %text1%
set Input_1100byte=adb shell input text %text2%


:1
rem =====================================================
rem 输入900多字节的
rem input text1
adb shell input text %text1%
%Delay_1s%
rem input text1
adb shell input tap 650 1860
adb shell input text %text1%
rem input text1
adb shell input tap 555 1650
adb shell input text %text1%
rem input text2
adb shell input tap 555 1650
%Delay_1s%
adb shell input text %text2%
rem send the message
%Send_msg_all_shurufa_up%
rem 返回键
%KEYCODE_BACK%


rem =====================================================
rem 输入1000多字节的
rem input text1
adb shell input text %text1%
%Delay_1s%
rem input text1
adb shell input tap 650 1860
adb shell input text %text1%
rem input text1
adb shell input tap 555 1650
adb shell input text %text1%
rem input text2
adb shell input tap 555 1650
%Delay_1s%
adb shell input text %text2%
%Delay_1s%
adb shell input text "0987654324587654321345674321224579843245768934523556787654333333333333333333[12312343546567576787809809876543245"
%Delay_3s%
rem send the message
%Send_msg_all_shurufa_up%
rem 返回键
%KEYCODE_BACK%




rem =====================================================
rem 选择2个大图片发送
rem 点击附件
%Click_Add% 
%Delay_1s% 
rem 向下移动
%KEYCODE_DPAD_DOWN%
rem 回车选择
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


::=======================================================选择2个视频并发送  
rem 选择视频并发送
%Click_Add%
rem tap attach button
%Delay_1s%
%KEYCODE_DPAD_DOWN%
rem 向下移动
%KEYCODE_DPAD_DOWN%
rem 向下移动
%KEYCODE_DPAD_DOWN%
rem 向下移动
%KEYCODE_ENTER%
rem 回车选择

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
%Add_Files_AudioVcard_1%
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
%Add_Files_PicVedio_1%
%Send_bottom%
rem tap Send_bottom button
%Delay_3s%

goto 1
