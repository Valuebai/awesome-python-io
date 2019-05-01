adb root
adb wait-for-device
adb remount
adb wait-for-device

SET Obj_Length=2
  
SET Obj[0].Name=14255021438
SET Obj[1].Name=14802443740 
SET Obj[2].Name=17029341868
SET Obj[3].Name=17029454865
SET Obj[4].Name=17029455361
SET Obj[5].Name=17029341703
SET Obj[6].Name=17029341856
SET Obj[7].Name=14802443598
SET Obj[8].Name=14802443929
SET Obj[9].Name=17029453883
SET Obj[10].Name=17029341864
SET Obj[11].Name=13237654940
SET Obj[12].Name=17029341860
SET Obj[13].Name=14802443570
SET Obj[14].Name=17029341867
SET Obj[15].Name=14252365575
SET Obj[16].Name=14253015557
SET Obj[17].Name=13237654937
SET Obj[18].Name=13235614865
SET Obj[19].Name=11112222
SET Obj[21].Name=13239758527
SET Obj[22].Name=13239758534
SET Obj[23].Name=13238426623
SET Obj[24].Name=14242792781
SET Obj[25].Name=14255021438
SET Obj[26].Name=13236816626
SET Obj[27].Name=13233845664
SET Obj[28].Name=14255891575
SET Obj[29].Name=14255891576

SET Obj_Index=0

:LoopStart

SET Obj_Current.Name=0
  
FOR /F "usebackq delims==. tokens=1-3" %%I IN (`SET Obj[%Obj_Index%]`) DO (
  SET Obj_Current.%%J=%%K
)
ECHO Name = %Obj_Current.Name%
SET /A Obj_Index=%Obj_Index% + 1


@echo rem 按home键
ping -n 1 127.1 >nul
adb shell input keyevent 3
ping -n 1 127.1 >nul
@echo rem 点击进入联系人
adb shell input tap 340 1800
@echo rem 添加联系人
adb shell input tap 945 1785
@echo rem 点击输入号码
adb shell input tap 280 1240 
ping -n 1 127.1 >nul
adb shell input text "%Obj_Current.Name%"
ping -n 1 127.1 >nul
@echo rem 确认添加联系人
adb shell input tap 1015 155
ping -n 1 127.1 >nul


if %Obj_Index%==30 exit

GOTO LoopStart

