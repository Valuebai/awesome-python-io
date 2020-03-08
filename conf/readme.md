# python配置文件使用规范

总结我在python实战中的经验

## Yaml文件

yaml格式的文件看起来很清爽，建议使用

- **.yaml文件的命名统一，以yaml_xxx.yaml作为规范**

- 获取yaml文件内容，参考get_yaml.py



配置文件请严格遵循yaml语法格式，yaml学习地址 https://ansible-tran.readthedocs.io/en/latest/docs/YAMLSyntax.html


## ini文件

- 在python中不建议使用ini，建议使用yaml。因为用pycharm.utf-8打开会乱码，得用GBK打开才正常

- logging.ini已被废弃，使用logConf.py进行日志系统的打印

- 也可以用.conf代替，但是觉得yaml更好


## log日志系统

抛弃使用，将logging.ini文件用python代码写出来，自定义logging日志系统，可直接复制使用

不使用flask自带的日志系统，用这个实测可用

```md
flask项目大致结构，使用windows-cmd，tree命令生成
├─APP
│  ├─AA
│  │  ├─static
│  │  ├─templates
│  │  └─AA.py
├─conf
│  └─logConf.py
│  
├─data
├─logs
├─static
├─templates
├─tests
└─run.py
```

**创建在conf路径下logConf.py，在flask中的入口文件run.py中，或者AA.py文件中，直接导入使用**
```python
from conf.log_config import logger

# 在具体需要的地方
logger.info('开始连接数据库...')
# logger.error(e)
```

## Database配置

- 使用yaml_databases.yaml配置DB信息
- 使用dbConf.py进行读取


## 路径配置

- 做项目时：最好将使用的pathConf.py配置统一配置系统的路径，小文件调试时无所谓
- 经验：在上面的flask项目框架中，使用../a.py, ../../b.py， 在pycharm中直接执行OK，但是在命令行中执行run.py会造成路径错乱
- 经验：python函数中不用写具体的路径，最好将路径定义为函数名的参数


## setting配置区分线上/开发环境

### 业务场景
本地与线上的 Swagger API 文档的接口的地址是不同的，但都依赖同一个配置文件 **`\conf\setting.py`**。<br>
而个人项目有着本地和线上同步，开发和测试同步的需求，会不断修改 **`\conf\setting.py`** 文件，无法用 **`.gitignore`** 做到忽略配置文件，本地和线上配置隔离的效果。 

### 解决
**`本地`** 和 **`线上`** 自动根据所处的环境(由 .gitignore 控制)不同，选择不同的配置文件。<br>
那么， **`本地`** 可以比 **`线上`** 多了 **`conf/dev.py`** 文件; 基于该文件的存在与否，可以用 **`if else`** 控制 **`conf/`** 中配置输出。

### Demo
1. `echo "/conf/dev.py" >> .gitignore` # 追加 Git 忽略提交配置到 .gitignore
2. 新建 **`/conf/dev.py`** 文件


## 其他配置参考

- pushbearConf.py 
  - 使用get_yaml获取./yaml_ticket_config.yaml的信息，在文件中的具体使用conf["pushbear_conf"]["is_pushbear"]

- yaml_ticket_config.yaml
  - 12306项目的配置，值得参考