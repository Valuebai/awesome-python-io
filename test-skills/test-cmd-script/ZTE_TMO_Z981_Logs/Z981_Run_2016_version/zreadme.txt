Z981_Run_2017�汾������������ƺ��߼�������ʹ��
1���޸�Z981_1_1chat.bat

set  User1=14802443776
set  User2=17029379475
set  User3=17029341868

����������UserX�ĺ��룬�޸ĺ��룺User18

::==========================================================�޸������User24
rem ����1-1��Ϣ
adb shell am start -a android.intent.action.SENDTO -d sms:"%User24%" --es sms_body  "%time%"


2���޸�1���룺Z981_group_chat�е�2�����룺User18��User18
::===========================================================�޸������2������
rem Ⱥ��
adb shell am start -a android.intent.action.SENDTO -d sms:"%User24%,%User3%" --es sms_body  "%time%"


3��ֱ��ִ��#1#���ٹر����д��ڣ�ִ��#2#