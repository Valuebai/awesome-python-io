SET Obj_Length=2
  
SET Obj[0].Name=14802443776
SET Obj[1].Name=17029379475
SET Obj[2].Name=17029341868
SET Obj[3].Name=17029454865
SET Obj[4].Name=17029455361
SET Obj[5].Name=17029341703
SET Obj[6].Name=17029341856
SET Obj[7].Name=14802443740
SET Obj[8].Name=14802443929
SET Obj[9].Name=17029453883
SET Obj[10].Name=17029341864
SET Obj[11].Name=14802443726
SET Obj[12].Name=17029341860
SET Obj[13].Name=14802443570
SET Obj[14].Name=17029341867
SET Obj[15].Name=14252365575
SET Obj[16].Name=14253015557
SET Obj[17].Name=14254350198
SET Obj[18].Name=14252365825
SET Obj[19].Name=14802443598



SET Obj_Index=0

:LoopStart

SET Obj_Current.Name=0
  
FOR /F "usebackq delims==. tokens=1-3" %%I IN (`SET Obj[%Obj_Index%]`) DO (
  SET Obj_Current.%%J=%%K
)
ECHO Name = %Obj_Current.Name%
SET /A Obj_Index=%Obj_Index% + 1


rem 按home键
ping -n 1 127.1 >nul
adb shell input keyevent 3
ping -n 1 127.1 >nul
rem 点击进入联系人
adb shell input tap 340 1800
rem 添加联系人
adb shell input tap 945 1785
rem 点击输入号码
adb shell input tap 280 1240 
ping -n 1 127.1 >nul
adb shell input text "%Obj_Current.Name%"
ping -n 1 127.1 >nul
rem 确认添加联系人
adb shell input tap 1015 155
ping -n 1 127.1 >nul


if %Obj_Index%==20 exit
GOTO LoopStart

