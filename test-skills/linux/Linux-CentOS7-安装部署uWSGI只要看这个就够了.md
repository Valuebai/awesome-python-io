1.（firstsite文件是从这里来的https://blog.51cto.com/12419955/2063269）

2.查找解决方法，在菜鸟教程中，找到uwsgi安装后的调试，用下面的命令来启动是OK的
```
uwsgi --http :8080 --chdir /root/firstsite -w firstsite.wsgi --processes 4 --threads 2 --stats 127.0.0.1:9191
```

但是用，uwsgi firstsite.ini，启动脚本后，发现8080端口一直没有起来，
```
菜鸟教程上的配置如下：
[uwsgi]
socket = 127.0.0.1:3031
chdir = /home/foobar/myproject/
wsgi-file = myproject/wsgi.py
processes = 4
threads = 2
stats = 127.0.0.1:9191
```
经过一番查找，在CSDN上的文章查看（https://blog.csdn.net/chenKFKevin/article/details/78297666），要把socket改为http！！！
```
...
保存后，运行（这步请将上面红色字体的socket改为http，socket是配置与nginx通信的（tcp协议），等下一步跟

nginx结合的时候再改回为socket，这里我们浏览器测试要改为http协议）：

uwsgi --inihello_uwsgi.ini 

在浏览器同样输入http://ip:8008/，看到it works的页面，说明配置成功。
```