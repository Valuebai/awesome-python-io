::======================================================================
rem 定义收件人变量
set  User1=14802443776
set  User2=17029379475
set  User3=17029341868
set  User4=17029454865
set  User5=17029455361
set  User6=17029341703
set  User7=17029341856
set  User8=14802443740
set  User9=14802443598
set  User10=17029453883
set  User11=17029341864
set  User12=14802443726
set  User13=17029341860
set  User14=14802443570
set  User15=17029341867
set  User16=13235614865
set  User17=13237654940
set  User18=13237654937
set  User19=13239758527
set  User20=13239758534
set  User21=13238426623
set  User22=14242792781
set  User23=14255021438
set  User24=13236816626
set  User25=13233845664
set  User26=14255891575
set  User27=14255891576

set  User28=14253657889
set  User29=14253726795
set  User30=14254354110
set  User31=14253659570
set  User32=14253726021
set  User33=13109854575


:: 目前会给2个号码发送消息，请修改在线的号码（14255891575、14255891576文豪的号码经常在线）
::==========================================================修改下面的UserX
rem 发送1-1消息
adb shell am start -a android.intent.action.SENDTO -d sms:"%User32%" --es sms_body  "111"
ping -n 3 127.1 >nul

call Z982_message_content.bat

rem 发送1-1消息，建立新的1-1会话
adb shell am start -a android.intent.action.SENDTO -d sms:"%User27%" --es sms_body  "111"
ping -n 3 127.1 >nul

call Z982_message_content.bat