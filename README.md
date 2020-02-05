# Python十分钟入门指南/技术图谱

![Build](https://img.shields.io/badge/Build-passing-brightgreen.svg)
![Languages](https://img.shields.io/badge/Languages-Python3.7-green.svg)
![License](https://img.shields.io/badge/License-MIT-orange.svg)
![Contributions](https://img.shields.io/badge/Contributions-welcome-ff69b4.svg)

我的学习记录，将学习Python过程中遇到的好项目，好技能，好分享记录下来，方便自己查找使用，也希望对你有帮助~

the roadmap of my study and learn from others



## 环境安装
- **【Python环境安装与搭建】**
    - 官网下载：[官网下载最新包](https://www.python.org/)
- **【PyCharm安装】**
    - 官网下载：[官网下载最新包](https://www.jetbrains.com/pycharm/)
    - Google下 PyCharm激活码自行解决

- ./python-ide/：记录python环境的其他说明
**readme.md记录Ptyhon创建虚拟环境的方法**


## python思维导图


## 算法 & 数据结构
- Leetcode刷题指南101，follow漂亮小姐姐：
[https://valuebai.github.io/2020/01/01/Leetcode%E5%88%B7%E9%A2%98%E6%8C%87%E5%8D%97101-follow%E6%BC%82%E4%BA%AE%E5%B0%8F%E5%A7%90%E5%A7%90/](https://valuebai.github.io/2020/01/01/Leetcode%E5%88%B7%E9%A2%98%E6%8C%87%E5%8D%97101-follow%E6%BC%82%E4%BA%AE%E5%B0%8F%E5%A7%90%E5%A7%90/)

- ./run_leetcode/：记录学习算法相关代码


## 在练习和学习中掌握
- ./run_test_code/: python天天练, 多写代码，即使是手动抄别人的代码!


## 在项目中成长
- ./project-run/imooc_auto_api/ : API自动化测试框架



## common & conf常用配置
- ./common/ : 常用的，好用的，通用的操作
- conf/config配置文件的使用：**详情见conf中的readme.md**


## Requirements
- 生成指南：
- 第一步：安装包 pip install pipreqs
- 第二步：在对应路径cmd，输入命令生成 requirements.txt文件：pipreqs ./ --encoding=utf8 --force 避免中文路径报错
- 第三步：下载该代码后直接pip install -r requirements.txt
- 或者创建虚拟环境安装


## Pycahrm 打开时加载很慢，indexing不停，scan半天的解决方法
- 笨办法：把大文件夹直接exculeded，这样不影响，被excluded的文件还是可以在程序中用。
- In pycharm, go to the "File" on the left top, then select "invalidate caches/restart...", and press "invalidate and restart".
- 知乎：https://www.zhihu.com/question/47427720/answer/106059581




---
## Python 两大web框架之Django
- 大而全，功能极其强大，是Python web框架的先驱，用户多，第三方库极其丰富，多用于中大型网站
- 比喻：Django类似于精装修的房子，自带豪华家具、非常齐全功能强大的家电，什么都有了，拎包入住即可，十分方便。

> **[Django官方3.0中文指南](https://docs.djangoproject.com/zh-hans/3.0/intro/tutorial01/)**

**++新手学习的话建议先学flask++**

## Python 两大web框架之Flask
- 轻量级，更多用来快速搭建简单网页，API等，多用于小型网站
- 比喻：Flask类似于毛坯房，自己想把房子装修成什么样自己找材料，买家具自己装。材料和家具种类非常丰富，并且都是现成免费的，直接拿过去用即可。

> **[Flask官方快速入门文档](http://docs.jinkan.org/docs/flask/quickstart.html#quickstart)**

### Flask-Script

[Flask的Web开发服务器支持很多启动设置选项，但只能在脚本中作为参数传给app.run()函数。
这种方式很不方便，传递设置选项的理想方式是使用命令行参数。
Flask-Scrip就是这么一个Flask扩展，为Flask程序添加一个命令行解析器。](http://www.pianshen.com/article/4624292459/)

**添加自定义shell命令**
- 例如：对数据库进行操作
- 解决跨域问题 from flask_cors import CORS
```

    # app = create_app() 在run.py中调用

    # 在__init__.py中添加def create_app(), register_blueprint(app), register_plugin(app)
def create_app():
	app = Flask(__name__, static_folder="./static", template_folder="./static/views")

	app.config.from_object('app.config.secure')
	app.config.from_object('app.config.setting')

	register_blueprint(app)
	register_plugin(app)

	return app

def register_plugin(app):
	# 解决跨域问题
	from flask_cors import CORS
	cors = CORS()
	cors.init_app(app, resources={"/*": {"origins": "*"}})

	# 连接数据库
	from app.models.base import db
	db.init_app(app)
	with app.app_context():  # 手动将app推入栈
		db.create_all()  # 首次模型映射(ORM ==> SQL),若无则建表; 初始化使用

	# Debug模式下可以查阅 API文档
	if app.config['DEBUG']:
		from flasgger import Swagger
		from app.api.v1 import create_api_tags_v1
		from app.api.v2 import create_api_tags_v2
		template = {
			# 默认与 conf/setting.py 的 SWAGGER 合并
			'tags': create_api_tags_v1() + create_api_tags_v2()  # 数组
		}
		swagger = Swagger(template=template)  # 可以将secure.py中的SWAGGER全部写入template
		swagger.init_app(app)
```



### Flask Blueprint，分隔视图
**当你的Flask项目膨胀到一定规模的时候， 全部都写到主入口之中。 一定需要按照模块进行拆分。 Blueprint(蓝图)就是这个时候需要使用的东西。**

- [Blueprint 之中使用日志](https://www.flyml.net/2018/12/12/flask-logging-usage-demo/)
- 完成blueprint框架后，在APP中的blueprint中
```python
from flask import current_app
# 在需要的地方
current_app.logger.info("simple page info...")
```







---
## 持续集成
- Jenkins CI: https://www.cnblogs.com/cnkemi/p/9051910.html

- Gitlab CI: https://blog.crazyphper.com/2019/10/26/python%E6%8E%A5%E5%8F%A3%E8%A6%86%E7%9B%96%E7%8E%87%E9%9B%86%E6%88%90gitlab-ci%E8%A1%8C%E5%8A%A8%E6%8C%87%E5%8D%97/


@[TOC](文章目录) #在CSDN自动生成目录
---
## linux部署指南
### 1. linux sh & nohup后台运行python脚本
  - 1）创建脚本vim run.sh
  - 2）填写内容并保存：nohup python3 -u  run.py > nohup.log 2>&1 &
  - 3）运行：sh run.sh 或者 . run.sh
  - 参考：[Linux sh、source和.命令执行.sh文件的区别](https://www.zengdongwu.com/article3.html) +
            [linux后台执行命令：&和nohup](https://blog.csdn.net/liuyanfeier/article/details/62422742)
```md
      - nohup : 就是不挂起的意思( no hang up)，可以在你退出帐户之后继续运行相应的进程
        - 使用&命令后，作业被提交到后台运行，当前控制台没有被占用，但是一但把当前控制台关掉(退出帐户时)，作业就会停止运行。nohup命令可以在你退出帐户之后继续运行相应的进程。
      - python3 -u  run.py : 执行py文件
      - -u的意思就是 uninterrupt不中断的意思，如果你的代码里边有sleep等线程沉睡相关的操作，如果你不-u的话 在后台 它就停住了
      - > nohup.log : 重定向保存日志到当前路径下的nohup.log
      - 2>&1 : 将标准出错也输出到nohup.log文件中
      - & : 最后一个&， 是让该命令在后台执行。
```

### 2. 使用gunicorn 部署flask服务 （个人项目推荐使用这个）
  - 1）创建脚本vim gunicorn.sh
  - 2）填写内容并保存：
    - conda activate just_do_it （在linux上创建好自己的环境，可选）
    - nohup gunicorn -w 4 -b 0.0.0.0:8001 run:app & （不带日志）
    - nohup gunicorn -w 4 -b 0.0.0.0:8001 run:app > gunicorn.log 2>&1 & （带日志）
    
  - 3）运行：sh gunicorn.sh 或者 . gunicorn.sh
  
```md
需要提前pip install gunicorn
简单地，gunicorn可以通过gunicorn -w 4 -b 0.0.0.0:8001 run:app启动一个Flask应用。其中,

-w 4是指预定义的工作进程数为4，
-b 127.0.0.1:4000指绑定地址和端口
run是flask的启动python文件，app则是flask应用程序实例

其中run.py中文件的可能形式是：
# run.py
from flask import Flask
app = Flask(__name__)

参考文章：
gunicorn部署Flask服务 https://www.jianshu.com/p/fecf15ad0c9a
https://www.cnblogs.com/gaidy/p/9784919.html
```

### 3. 使用screen命令部署
  - 第一步：screen -S yourname，新建一个叫yourname的session
  - 第二步：python run.py，运行代码，关闭shell连接后还会一直在linux上跑
  - 针对用户量小的情况，快速部署（本次使用这个）
  - 关于screen，详情见：https://www.cnblogs.com/mchina/archive/2013/01/30/2880680.html 
```
    杀死所有命令的：ps aux|grep 你的进程名|grep -v grep | awk '{print $2}'|xargs kill -9
    
    https://www.hutuseng.com/article/how-to-kill-all-detached-screen-session-in-linux
```

### 4. 使用flask + nginx + uwsgi (不建议，因Flask 与 uWsgi 结合有许多难以处理的 bug)
  - 针对用户访问量大的情况，具体参考下面的文章
    - https://blog.csdn.net/spark_csdn/article/details/80790929
    - https://www.cnblogs.com/Ray-liang/p/4173923.html
    - https://blog.csdn.net/daniel_ustc/article/details/9070357

### 5. 使用flask + nginx + gunicorn （大项目推荐使用这个）
  - 生产环境很多大公司采用这个方式的，故推荐这个
  - 因Flask 与 uWsgi 结合有许多难以处理的 bug，故推荐这个
  - [Flask + Gunicorn + Nginx 部署](https://www.cnblogs.com/Ray-liang/p/4837850.html)



## linux上杀死gunicorn的进程
**方法一**
1. netstat -nltp | grep 8188
能看到类似下面的：
tcp        0      0 0.0.0.0:8188            0.0.0.0:*               LISTEN      23422/gunicorn: mas

2. kill -9 23422（换成你的）


**方法二**
1. 获取Gunicorn进程树 
```
pstree -ap|grep gunicorn

得到的结果如下

Python
| | |-grep,14519 --color=auto gunicorn
| -gunicorn,28097 /usr/local/bin/gunicorn query_site.wsgi:application -c ... 
| |-gunicorn,14226 /usr/local/bin/gunicorn query_site.wsgi:application -c ... 
| | |-{gunicorn},14229 
| | |-{gunicorn},14230 
...

```

2. 重启Gunicorn任务

kill -HUP 14226

3. 退出Gunicorn任务

kill -9 28097


## linux根据端口号查找项目路径方法
### 1. 只知道端口号
1. 首先根据端口号查找进程
```
netstat -nltp
或者
netstat -nltp | grep python
或者
netstat -apn |grep 10010
```
2. 然后根据进程号去查找项目路径
```
ps -ef |grep 8567
```
3. 如果你第二步没有找到项目路径的话，尝试用
```
lsof -p 8567
```
### 2. 如果知道项目部署在tomcat里
如果你的项目在linux 中是部署到tomcat容器里，可以输入下边的命令找到，如下:
```
ps anx|grep tomcat
```

## 【技巧】如何通过pycharm实现远程(linux)代码的调试和开发
> https://www.jianshu.com/p/79df9ac88e96

> Pycharm远程连接服务器（windows下远程修改服务器代码），https://blog.csdn.net/zhaihaifei/article/details/53691873

## 【技巧】git查看某个文件的修改历史

> git查看某个文件的修改历史，https://www.cnblogs.com/flyme/archive/2011/11/28/2265899.html

> git log 查看某文件的修改历史，https://www.cnblogs.com/Sir-Lin/p/6064844.html

> Sourcetree右上角


```
该完善区域
## 0. 学习路线
### Python 学习路径图/思维导图（待更新）
### Python 开发应用/职业规划选择
### Python 测试/Web/人工智能/大数据/金融量化

#### Python书籍使用
看这个就够了：
[如果有人让你推荐 Python 技术书，请让他看这个列表](https://github.com/jobbole/awesome-python-books)

-《图解算法,python实现，回头增加下》

- [《Python知识手册》](http://liyangbit.com/python-knowledge-handbook/)
```