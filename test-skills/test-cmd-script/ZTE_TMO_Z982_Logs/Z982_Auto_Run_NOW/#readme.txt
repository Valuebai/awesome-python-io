version:Z982_Auto_Run�汾���Ż�������ƫ������

���ܣ�ʵ��Z982�ֻ��Ĺ����Զ������ԣ�ѭ���������1-1��Ⱥ�ĵĸ�����Ϣ�������ڲ�����
ʹ�ã�
1. Z982���ֻ�����root��remount�ɹ���ִ�нű��������ֻ��������ӵ���
2. �ֻ������м��������ز�

rem //3. phone��contacts��messaging�������·����ΰ���1/2/3˳������

:: ��ȷ������Ĳ������
::============================================================

1���޸�Z981_1_1chat.bat�еĺ���

set  User1=14802443776
set  User2=17029379475

����������UserX�ĺ��룬�޸ĺ��룺User18

::==========================================================�޸������User24
rem ����1-1��Ϣ
adb shell am start -a android.intent.action.SENDTO -d sms:"%User24%" --es sms_body  "%time%"


2���޸�Ⱥ��Z982_group_chat.bat�еĺ��룺Z981_group_chat�е�2�����룺User18��User18
::===========================================================�޸������2������
rem Ⱥ��
adb shell am start -a android.intent.action.SENDTO -d sms:"%User24%,%User3%" --es sms_body  "%time%"


3��ֱ��ִ��#1#Z982_Run.bat��������1-1��Ⱥ�ģ��ٹر����д��ڣ�ִ��#2#After_Run_Pull_logs_ToSave.bat��#2#ZTE_AndroidAutocopy.bat�����˹������ͼ��UI������뵥������1-1����Ⱥ�ģ�˫����Ӧ�Ľű����ɣ�