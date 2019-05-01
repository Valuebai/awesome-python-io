Z981_Run_2017版本：整理代理名称和逻辑，方便使用
1、修改Z981_1_1chat.bat

set  User1=14802443776
set  User2=17029379475
set  User3=17029341868

里面有类似UserX的号码，修改号码：User18

::==========================================================修改下面的User24
rem 发送1-1消息
adb shell am start -a android.intent.action.SENDTO -d sms:"%User24%" --es sms_body  "%time%"


2、修改1号码：Z981_group_chat中的2个号码：User18和User18
::===========================================================修改下面的2个号码
rem 群聊
adb shell am start -a android.intent.action.SENDTO -d sms:"%User24%,%User3%" --es sms_body  "%time%"


3、直接执行#1#，再关闭所有窗口，执行#2#