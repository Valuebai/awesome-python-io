### 安装前：简单了解下2种安装方式，yum和源码手动安装的区别

[nginx服务器详细安装过程（使用yum 和 源码包两种安装方式，并说明其区别）](https://segmentfault.com/a/1190000007116797)

## 一、yum安装方式
```
官网的nginx install方式：一定要看2个，不然会被坑的
1）http://nginx.org/en/linux_packages.html#RHEL-CentOS  （没有说要替换$releasever参数为7）
2）https://www.nginx.com/resources/wiki/start/topics/tutorials/install/  （没有说要yum install yum-utils）
P.S. 一般安装某个软件，跟进官方教程是OK的
```

### 正确的yum步骤（根据官网文档整理）：

### 第一步 – 添加Nginx存储库

##### 1）安装前的准备，请打开终端并使用以下命令：
```
sudo yum install yum-utils    #只要执行这个即可

sudo yum install epel-release #如果提示 No package nginx available，用这个命令
```

##### 2）设置云仓库，创建文件vim /etc/yum.repos.d/nginx.repo，并填入配置并保存 
```
[nginx]
name=nginx repo
baseurl=http://nginx.org/packages/centos/7/$basearch/
gpgcheck=0
enabled=1
gpgkey=https://nginx.org/keys/nginx_signing.key
```
### 第二步 – 安装Nginx
##### 现在Nginx存储库已经安装在您的服务器上，使用以下yum命令安装Nginx ：
```
sudo yum install nginx

在对提示回答yes后，Nginx将在服务器上完成安装。
```

### 第三步 – 启动Nginx
##### Nginx不会自行启动。要运行Nginx，请输入：
```
sudo systemctl start nginx

P.S. 启动报端口被占用，到/etc/nginx/conf.d/default.conf 修改下默认端口
```
##### 如果您正在运行防火墙，请运行以下命令以允许HTTP和HTTPS通信：
```
sudo firewall-cmd --permanent --zone=public --add-service=http 
sudo firewall-cmd --permanent --zone=public --add-service=https
sudo firewall-cmd --reload

--zone #作用域
--add-port=80/tcp #添加端口，格式为：端口/通讯协议
--permanent #永久生效，没有此参数重启后失效
```
##### 【运行成功】输入地址，会看到默认的CentOS 7 Nginx网页，这是为了提供信息和测试目的。它应该看起来像这样：
![9b3f75f01ed34dc88688a5b2a7c4b828.png](https://www.centos.bz/wp-content/uploads/2018/01/1-7.png)
##### 如果看到这个页面，那么你的Web服务器现在已经正确安装了。
### 第四步-设置系统启动时启用Nginx
##### 请输入以下命令：
```
设置开机启动
$ sudo systemctl enable nginx
 
启动服务
$ sudo systemctl start nginx
 
停止服务
$ sudo systemctl restart nginx
 
重新加载，因为一般重新配置之后，不希望重启服务，这时可以使用重新加载。
$ sudo systemctl reload nginx
 
 
Nginx 是一个很方便的反向代理，配置反向代理可以参考 Module ngx_http_proxy_module 。本文不做累述。
 
需要指出的是 CentOS 7 的 SELinux，使用反向代理需要打开网络访问权限。
 
$ sudo setsebool httpd_can_network_connect 1 
打开网络权限之后，反向代理可以使用了。
```
### 第五步-Nginx默认目录
##### 查找Nginx安装目录的命令
```
whereis nginx
```
##### 以下是Nginx的默认路径：即可看到类似于如下的内容：
```
nginx: /usr/sbin/nginx /usr/lib64/nginx /etc/nginx /usr/share/nginx

(1) Nginx配置路径：/etc/nginx/

(2) PID目录：/var/run/nginx.pid

(3) 错误日志：/var/log/nginx/error.log

(4) 访问日志：/var/log/nginx/access.log

(5) 默认站点目录：/usr/share/nginx/html

事实上，只需知道Nginx配置路径，
其他路径均可在/etc/nginx/nginx.conf 以及/etc/nginx/conf.d/default.conf 中查询到。
P.S. Nginx启动报端口被占用也是在这里改的
```
### 第六步-常用命令
```
(1) 启动：nginx
(2) 测试Nginx配置是否正确：nginx -t
(3) 查看nginx 进程：ps -ef | grep nginx
(4) 杀死进程：kill -9 nginx进程号
(5) 查看tcp是否正常监听：ntstat -nlp
```


* * *
## 二、源代码手动安装 

[CentOS7安装Nginx及配置](https://www.jianshu.com/p/9a6c96ecc8b8)

[CentOS7 下 Nginx 安装部署和配置](https://www.linuxidc.com/Linux/2018-07/153183.htm)

