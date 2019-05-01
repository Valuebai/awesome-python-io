rem 发送各种内容的消息

::=======================================================输入当前日期和时间发送
rem 输入当前日期和时间发送
adb shell input text "%time%"
ping -n 1 127.1 >nul
adb shell input tap 1000 1800
ping -n 1 127.1 >nul

::=======================================================再次输入当前日期和时间发送
rem 再次输入当前日期和时间发送
adb shell input text "%time%"
ping -n 1 127.1 >nul
adb shell input tap 1000 1800
ping -n 1 127.1 >nul

::=======================================================发送录制的音频1
rem 发送录制的音频
ping -n 1 127.1 >nul
adb shell input tap 1000 1800
rem 点击录音按钮
ping -n 1 127.1 >nul
adb shell input swipe 560 1800 560 1800 10000
ping -n 3 127.1 >nul

::=======================================================再次输入当前日期和时间发送
rem 再次输入当前日期和时间发送
adb shell input text "%time%"
ping -n 1 127.1 >nul
adb shell input tap 1000 1800
ping -n 1 127.1 >nul


::=======================================================发送录制的音频2
rem 点击录音按钮
ping -n 1 127.1 >nul
adb shell input swipe 560 1800 560 1800 10000
ping -n 3 127.1 >nul

::=======================================================再次输入当前日期和时间发送
rem 再次输入当前日期和时间发送
adb shell input text "%time%"
ping -n 1 127.1 >nul
adb shell input tap 1000 1800
ping -n 1 127.1 >nul

::=======================================================选择2张图片并发送
rem 点击附件
adb shell input tap 88 1800
rem tap attach button
ping -n 1 127.1 >nul

rem 选择图片并发送
adb shell input keyevent 20
rem 向下移动
adb shell input keyevent 66
rem 回车选择
ping -n 3 127.1 >nul
adb shell input tap 300 290
rem select the first one
ping -n 1 127.1 >nul
adb shell input tap 660 290
rem select the second one
ping -n 1 127.1 >nul
adb shell input tap 980 150
rem tap ok button
ping -n 1 127.1 >nul
adb shell input tap 1000 1800
rem tap send button
ping -n 3 127.1 >nul

::=======================================================再次输入当前日期和时间发送
rem 再次输入当前日期和时间发送
adb shell input text "%time%"
ping -n 1 127.1 >nul
adb shell input tap 1000 1800
ping -n 1 127.1 >nul

::=======================================================选择拍摄照片并发送1
rem 选择拍摄照片并发送
adb shell input tap 80 1800
rem tap attach button
ping -n 1 127.1 >nul
adb shell input keyevent 20
rem 向下移动
adb shell input keyevent 20
rem 向下移动
adb shell input keyevent 66
rem 回车选择
ping -n 3 127.1 >nul
adb shell input tap 540 1810
rem 点击拍照按钮
ping -n 3 127.1 >nul
adb shell input tap 960 1810
rem 点击确认按钮
ping -n 3 127.1 >nul
adb shell input tap 1000 1800
rem tap send button
ping -n 3 127.1 >nul

::=======================================================再次输入当前日期和时间发送
rem 再次输入当前日期和时间发送
adb shell input text "%time%"
ping -n 1 127.1 >nul
adb shell input tap 1000 1800
ping -n 1 127.1 >nul

::=======================================================选择拍摄照片并发送2
rem 选择拍摄照片并发送
adb shell input tap 80 1800
rem tap attach button
ping -n 1 127.1 >nul
adb shell input keyevent 20
rem 向下移动
adb shell input keyevent 20
rem 向下移动
adb shell input keyevent 66
rem 回车选择
ping -n 3 127.1 >nul
adb shell input tap 540 1810
rem 点击拍照按钮
ping -n 3 127.1 >nul
adb shell input tap 960 1810
rem 点击确认按钮
ping -n 3 127.1 >nul
adb shell input tap 1000 1800
rem tap send button
ping -n 3 127.1 >nul

::=======================================================再次输入当前日期和时间发送
rem 再次输入当前日期和时间发送
adb shell input text "%time%"
ping -n 1 127.1 >nul
adb shell input tap 1000 1800
ping -n 1 127.1 >nul

::=======================================================选择2个视频并发送  
rem 选择视频并发送
adb shell input tap 80 1800
rem tap attach button
ping -n 1 127.1 >nul
adb shell input keyevent 20
rem 向下移动
adb shell input keyevent 20
rem 向下移动
adb shell input keyevent 20
rem 向下移动
adb shell input keyevent 66
rem 回车选择


rem select the first one
ping -n 3 127.1 >nul
adb shell input tap 300 300

rem select the second one
ping -n 3 127.1 >nul
adb shell input tap 650 300

rem tap ok button
ping -n 3 127.1 >nul
adb shell input tap 1015 155

rem tap send button
ping -n 3 127.1 >nul
adb shell input tap 1000 1800

ping -n 3 127.1 >nul


::=======================================================再次输入当前日期和时间发送
rem 再次输入当前日期和时间发送
adb shell input text "%time%"
ping -n 1 127.1 >nul
adb shell input tap 1000 1800
ping -n 1 127.1 >nul

::=======================================================选择拍摄视频并发送1
rem 选择拍摄视频并发送
adb shell input tap 80 1800
rem tap attach button
ping -n 1 127.1 >nul
adb shell input keyevent 20
rem 向下移动
adb shell input keyevent 20
rem 向下移动
adb shell input keyevent 20
rem 向下移动
adb shell input keyevent 20
rem 向下移动
adb shell input keyevent 66
rem 回车选择
ping -n 3 127.1 >nul
adb shell input tap 540 1810
rem 点击拍摄按钮
ping -n 7 127.1 >nul
adb shell input tap 540 1810
rem 点击停止拍摄
ping -n 3 127.1 >nul
adb shell input tap 960 1810
rem 点击确认按钮
ping -n 3 127.1 >nul
adb shell input tap 1000 1800
rem tap send button
ping -n 3 127.1 >nul

::=======================================================再次输入当前日期和时间发送
rem 再次输入当前日期和时间发送
adb shell input text "%time%"
ping -n 1 127.1 >nul
adb shell input tap 1000 1800
ping -n 1 127.1 >nul

::=======================================================选择拍摄视频并发送2
rem 选择拍摄视频并发送
adb shell input tap 80 1800
rem tap attach button
ping -n 1 127.1 >nul
adb shell input keyevent 20
rem 向下移动
adb shell input keyevent 20
rem 向下移动
adb shell input keyevent 20
rem 向下移动
adb shell input keyevent 20
rem 向下移动
adb shell input keyevent 66
rem 回车选择
ping -n 3 127.1 >nul
adb shell input tap 540 1810
rem 点击拍摄按钮
ping -n 7 127.1 >nul
adb shell input tap 540 1810
rem 点击停止拍摄
ping -n 3 127.1 >nul
adb shell input tap 960 1810
rem 点击确认按钮
ping -n 3 127.1 >nul
adb shell input tap 1000 1800
rem tap send button
ping -n 3 127.1 >nul

::=======================================================再次输入当前日期和时间发送
rem 再次输入当前日期和时间发送
adb shell input text "%time%"
ping -n 1 127.1 >nul
adb shell input tap 1000 1800
ping -n 1 127.1 >nul

::=======================================================选择2个音频并发送
rem 选择多个音频并发送
adb shell input tap 80 1800
rem tap attach button
ping -n 1 127.1 >nul

rem 向下移动
adb shell input keyevent 20
rem 向下移动
adb shell input keyevent 20
rem 向下移动
adb shell input keyevent 20
rem 向下移动
adb shell input keyevent 20
rem 向下移动
adb shell input keyevent 20

rem 回车选择
adb shell input keyevent 66

rem select the first one
ping -n 3 127.1 >nul
adb shell input tap 650 350

rem select the second one
ping -n 3 127.1 >nul
adb shell input tap 650 540

rem tap ok button
ping -n 3 127.1 >nul
adb shell input tap 1015 155

rem tap send button
ping -n 3 127.1 >nul
adb shell input tap 1000 1800

ping -n 3 127.1 >nul

::=======================================================再次输入当前日期和时间发送
rem 再次输入当前日期和时间发送
adb shell input text "%time%"
ping -n 1 127.1 >nul
adb shell input tap 1000 1800
ping -n 1 127.1 >nul

::=======================================================选择录制音频并发送1
rem 选择录制音频并发送
adb shell input tap 80 1800
rem tap attach button
ping -n 1 127.1 >nul
adb shell input keyevent 20
rem 向下移动
adb shell input keyevent 20
rem 向下移动
adb shell input keyevent 20
rem 向下移动
adb shell input keyevent 20
rem 向下移动
adb shell input keyevent 20
rem 向下移动
adb shell input keyevent 20
rem 向下移动
adb shell input keyevent 66
rem 回车选择
ping -n 3 127.1 >nul
adb shell input tap 540 1810
rem 点击开始按钮
ping -n 7 127.1 >nul
adb shell input tap 835 1715
rem 点击停止
ping -n 3 127.1 >nul
adb shell input tap 1000 1800
rem tap send button
ping -n 3 127.1 >nul

::=======================================================再次输入当前日期和时间发送
rem 再次输入当前日期和时间发送
adb shell input text "%time%"
ping -n 1 127.1 >nul
adb shell input tap 1000 1800
ping -n 1 127.1 >nul

::=======================================================选择录制音频并发送2
rem 选择录制音频并发送
adb shell input tap 80 1800
rem tap attach button
ping -n 1 127.1 >nul
adb shell input keyevent 20
rem 向下移动
adb shell input keyevent 20
rem 向下移动
adb shell input keyevent 20
rem 向下移动
adb shell input keyevent 20
rem 向下移动
adb shell input keyevent 20
rem 向下移动
adb shell input keyevent 20
rem 向下移动
adb shell input keyevent 66
rem 回车选择
ping -n 3 127.1 >nul
adb shell input tap 540 1810
rem 点击开始按钮
ping -n 7 127.1 >nul
adb shell input tap 835 1715
rem 点击停止
ping -n 3 127.1 >nul
adb shell input tap 1000 1800
rem tap send button
ping -n 3 127.1 >nul

::=======================================================再次输入当前日期和时间发送
rem 再次输入当前日期和时间发送
adb shell input text "%time%"
ping -n 1 127.1 >nul
adb shell input tap 1000 1800
ping -n 1 127.1 >nul

::=======================================================选择2个v-card并发送  
adb shell input tap 80 1800
rem tap attach button
ping -n 1 127.1 >nul

rem 向下移动
adb shell input keyevent 20
rem 向下移动
adb shell input keyevent 20
rem 向下移动
adb shell input keyevent 20
rem 向下移动
adb shell input keyevent 20
rem 向下移动
adb shell input keyevent 20
rem 向下移动
adb shell input keyevent 20
rem 向下移动
adb shell input keyevent 20
rem 向下移动
adb shell input keyevent 20
rem 向下移动
adb shell input keyevent 20

rem 回车选择
adb shell input keyevent 66

rem select the first one
ping -n 3 127.1 >nul
adb shell input tap 1005 335

rem select the second one
ping -n 3 127.1 >nul
adb shell input tap 1005 535

rem tap ok button
ping -n 3 127.1 >nul
adb shell input tap 805 1850

rem tap send button
ping -n 3 127.1 >nul
adb shell input tap 1000 1800

ping -n 3 127.1 >nul

::=======================================================再次输入当前日期和时间发送
rem 再次输入当前日期和时间发送
adb shell input text "%time%"
ping -n 1 127.1 >nul
adb shell input tap 1000 1800
ping -n 1 127.1 >nul

::=======================================================选择file中的图片发送
rem 选择file中的图片发送
adb shell input tap 80 1800
rem tap attach button
ping -n 1 127.1 >nul
adb shell input keyevent 20
rem 向下移动
adb shell input keyevent 20
rem 向下移动
adb shell input keyevent 20
rem 向下移动
adb shell input keyevent 20
rem 向下移动
adb shell input keyevent 20
rem 向下移动
adb shell input keyevent 20
rem 向下移动
adb shell input keyevent 20
rem 向下移动
adb shell input keyevent 20
rem 向下移动
adb shell input keyevent 66
rem 回车选择
ping -n 3 127.1 >nul
adb shell input tap 176 520
rem select image
ping -n 3 127.1 >nul
adb shell input tap 180 420
rem select the first one
ping -n 3 127.1 >nul
adb shell input tap 1000 1800
rem tap send button
ping -n 3 127.1 >nul

::=======================================================再次输入当前日期和时间发送
rem 再次输入当前日期和时间发送
adb shell input text "%time%"
ping -n 1 127.1 >nul
adb shell input tap 1000 1800
ping -n 1 127.1 >nul

::=======================================================选择file中的音频发送
rem 选择file中的音频发送
adb shell input tap 80 1800
rem tap attach button
ping -n 3 127.1 >nul
adb shell input tap 288 1720
rem select file
ping -n 3 127.1 >nul
adb shell input tap 540 520
rem select audio
ping -n 3 127.1 >nul
adb shell input tap 520 330
rem select the first one
ping -n 3 127.1 >nul
adb shell input tap 1000 1800
rem tap send button
ping -n 3 127.1 >nul

::=======================================================再次输入当前日期和时间发送
rem 再次输入当前日期和时间发送
adb shell input text "%time%"
ping -n 1 127.1 >nul
adb shell input tap 1000 1800
ping -n 1 127.1 >nul

::=======================================================选择file中的视频发送
rem 选择file中的视频发送
adb shell input tap 80 1800
rem tap attach button
ping -n 1 127.1 >nul
adb shell input tap 288 1720
rem select file
ping -n 3 127.1 >nul
adb shell input tap 900 520
rem select video
ping -n 3 127.1 >nul
adb shell input tap 180 420
rem select the first one
ping -n 3 127.1 >nul
adb shell input tap 1000 1800
rem tap send button
ping -n 3 127.1 >nul

::=======================================================再次输入当前日期和时间发送
rem 再次输入当前日期和时间发送
adb shell input text "%time%"
ping -n 1 127.1 >nul
adb shell input tap 1000 1800
ping -n 1 127.1 >nul

::=======================================================选择file中的vcard发送
rem 选择file中的vcard发送
adb shell input tap 80 1800
rem tap attach button
ping -n 1 127.1 >nul
adb shell input tap 288 1720
rem select file
ping -n 3 127.1 >nul
adb shell input tap 900 850
rem select documents
ping -n 3 127.1 >nul
adb shell input tap 520 330
rem select the first one
ping -n 3 127.1 >nul
adb shell input tap 1000 1800
rem tap send button
ping -n 3 127.1 >nul

::=======================================================退出当前会话详情
adb shell input tap 80 155