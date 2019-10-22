# Python十分钟入门指南/技术图谱

![Build](https://img.shields.io/badge/Build-passing-brightgreen.svg)
![Languages](https://img.shields.io/badge/Languages-Python3.7-green.svg)
![License](https://img.shields.io/badge/License-MIT-orange.svg)
![Contributions](https://img.shields.io/badge/Contributions-welcome-ff69b4.svg)

我的学习记录，将学习Python，Test过程中遇到的好项目，好技能，好分享记录下来，方便自己查找使用，也希望对你有帮助~

the roadmap of my study and learn from others

## 0. 学习路线
### Python 学习路径图/思维导图（待更新）
### Python 开发应用/职业规划选择
### Python 测试/Web/人工智能/大数据/金融量化

#### Python书籍使用
看这个就够了：
[如果有人让你推荐 Python 技术书，请让他看这个列表](https://github.com/jobbole/awesome-python-books)

-《图解算法,python实现，回头增加下》
## 1. 环境安装
- **【Python环境安装与搭建】**
    - 官网下载：[官网下载最新包](https://www.python.org/)
- **【PyCharm安装】**
    - 官网下载：[官网下载最新包](https://www.jetbrains.com/pycharm/)
    - Google下 PyCharm激活码自行解决

## 2. 基础语法思维导图

## 3. 算法

## Django
### 学习指南
#### Django基础
- **[【Django基础\(1\): Model模型的介绍与设计】](https://mp.weixin.qq.com/s/nmwikIXGwVFN6e0E5FlPEQ)**

- [《Python知识手册》](http://liyangbit.com/python-knowledge-handbook/)

## Flask

### [Flask官方快速入门文档](http://docs.jinkan.org/docs/flask/quickstart.html#quickstart)

### Flask-Script

[Flask的Web开发服务器支持很多启动设置选项，但只能在脚本中作为参数传给app.run()函数。
这种方式很不方便，传递设置选项的理想方式是使用命令行参数。
Flask-Scrip就是这么一个Flask扩展，为Flask程序添加一个命令行解析器。](http://www.pianshen.com/article/4624292459/)

**添加自定义shell命令**
- 例如：对数据库进行操作
- 解决跨域问题 from flask_cors import CORS
```python

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

========================================================
python天天练习，每天都要写代码，即使是手动抄别人的代码!


## conf/config配置文件的使用

**详情见conf中的readme.md**


## 本地&线上同步推进
### 业务场景
本地与线上的 Swagger API 文档的接口的地址是不同的，但都依赖同一个配置文件 **`\conf\setting.py`**。<br>
而个人项目有着本地和线上同步，开发和测试同步的需求，会不断修改 **`\conf\setting.py`** 文件，无法用 **`.gitignore`** 做到忽略配置文件，本地和线上配置隔离的效果。 

### 解决
**`本地`** 和 **`线上`** 自动根据所处的环境(由 .gitignore 控制)不同，选择不同的配置文件。<br>
那么， **`本地`** 可以比 **`线上`** 多了 **`conf/dev.py`** 文件; 基于该文件的存在与否，可以用 **`if else`** 控制 **`conf/`** 中配置输出。

### Demo
1. `echo "/conf/dev.py" >> .gitignore` # 追加 Git 忽略提交配置到 .gitignore
2. 新建 **`/conf/dev.py`** 文件


## Requirements
- 生成指南：
- 第一步：安装包 pip install pipreqs
- 第二步：在对应路径cmd，输入命令生成 requirements.txt文件：pipreqs ./ --encoding=utf8 --force 避免中文路径报错
- 第三步：下载该代码后直接pip install -r requirements.txt
- 或者创建虚拟环境安装


## Ptyhon创建虚拟环境

### 方法一：自带命令
1. 进入文件夹目录
2. python -m venv -h 可查看帮助信息
3. 下面的
```
Linux运行命令行
$ 创建默认环境：python3 -m venv my_venv 
$ 创建指定环境：python3.6 -m venv  my_venv,  python2 -m venv  my_venv(添加到系统环境变量中)
$ 激活环境：. my_venv/bin/activate  (. 或者 source )
$ 退出环境：deactivate 

Windows系统运行cmd，使用 "py" Python 启动器命令配合 "-m" 开关选项:
$ 创建环境：py -3 -m venv my_venv (或者python -m venv my_venv)
$ 创建指定环境：py -3.6 -m venv my_venv,  py -3.7 -m venv my_venv (添加到系统环境变量中)
$ 激活环境：my_venv\Scripts\activate.bat
$ 退出环境：deactivate

执行后，会在目录前方出现<my_venv>表明已进入虚拟环境

安装项目:
$ pip install -r requirements.txt
```

### 方法二：Windows在PyCharm下创建虚拟环境
1. 安装并激活PyCharm
这个请自行安装
官方地址：https://www.jetbrains.com/pycharm/

2. 在PyCharm下创建虚拟环境
第一步：点击New Project
第二步：选择下图的New environment
第三步：点击create即可
pycharm会为新创建的项目自动建立一个虚拟环境


### 方法三：conda创建虚拟环境

[anaconda中的常用操作](https://blog.csdn.net/CampusAmour/article/details/83215524)


Linux下启动其终端命令行 
$ source ~/anaconda3/bin/activate root
$ anaconda-navigator

- 创建虚拟环境，conda create -n env_name python=3.6

- 同时安装必要的包，conda create -n env_name numpy matplotlib python=3.6

- 激活虚拟环境
  - Linux：source activate your_env_name(虚拟环境名称)
  - Windows：activate your_env_name(虚拟环境名称)

- 退出虚拟环境： 
  - Linux：source deactivate your_env_name(虚拟环境名称)
  - Windows：deactivate your_env_name(虚拟环境名称)

- 删除虚拟环境，conda remove -n your_env_name(虚拟环境名称) --all
- 删除包使用命令，conda remove --name $your_env_name  $package_name（包名)


conda常用命令
- 查看已安装的包，conda list
- 安装包，conda install package_name(包名)
- 查看当前存在的虚拟环境，conda env list 或 conda info -e
- 检查更新当前conda，conda update conda


## linux部署指南
**1. linux sh & nohup后台运行脚本**
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

**2. 使用gunicorn 部署flask服务**
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

**3. 使用screen命令部署**
  - 第一步：screen -S yourname，新建一个叫yourname的session
  - 第二步：python run.py，运行代码，关闭shell连接后还会一直在linux上跑
  - 针对用户量小的情况，快速部署（本次使用这个）
  - 关于screen，详情见：https://www.cnblogs.com/mchina/archive/2013/01/30/2880680.html 
```
    杀死所有命令的：ps aux|grep 你的进程名|grep -v grep | awk '{print $2}'|xargs kill -9
    
    https://www.hutuseng.com/article/how-to-kill-all-detached-screen-session-in-linux
```
**4. 使用flask + nginx + uwsgi**
  - 针对用户访问量大的情况，具体参考下面的文章
    - https://blog.csdn.net/spark_csdn/article/details/80790929
    - https://www.cnblogs.com/Ray-liang/p/4173923.html
    - https://blog.csdn.net/daniel_ustc/article/details/9070357

**5. 使用flask + nginx + gunicorn**
  - 生产环境很多大公司采用这个方式的，后面有时间再研究


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
### 只知道端口号
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
### 如果知道项目部署在tomcat里
如果你的项目在linux 中是部署到tomcat容器里，可以输入下边的命令找到，如下:
```
ps anx|grep tomcat
```