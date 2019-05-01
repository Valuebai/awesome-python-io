version:Z982_Auto_Run版本：优化容易跑偏的问题

功能：实现Z982手机的功能自动化测试，循环点击发送1-1和群聊的各类消息，无论在不在线
使用：
1. Z982的手机必须root、remount成功，执行脚本过程中手机必须连接电脑
2. 手机至少有几个测试素材

rem //3. phone，contacts，messaging在桌面下发依次按照1/2/3顺序排列

:: 请确认上面的操作完成
::============================================================

1、修改Z981_1_1chat.bat中的号码

set  User1=14802443776
set  User2=17029379475

里面有类似UserX的号码，修改号码：User18

::==========================================================修改下面的User24
rem 发送1-1消息
adb shell am start -a android.intent.action.SENDTO -d sms:"%User24%" --es sms_body  "%time%"


2、修改群聊Z982_group_chat.bat中的号码：Z981_group_chat中的2个号码：User18和User18
::===========================================================修改下面的2个号码
rem 群聊
adb shell am start -a android.intent.action.SENDTO -d sms:"%User24%,%User3%" --es sms_body  "%time%"


3、直接执行#1#Z982_Run.bat即可运行1-1和群聊，再关闭所有窗口，执行#2#After_Run_Pull_logs_ToSave.bat和#2#ZTE_AndroidAutocopy.bat进行人工分析和检查UI（如果想单独运行1-1或者群聊，双击对应的脚本即可）