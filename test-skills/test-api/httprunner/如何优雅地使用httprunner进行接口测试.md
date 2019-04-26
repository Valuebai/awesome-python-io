
* * *
一天，你的领导X要你对某接口做测试，你一听，接口测试，高大上。用什么做好呢？postman？jmeter？loadrunner？balabala。。。优秀的你，想到了一大堆工具，当然也包括用python写。为了凸显B格，你选择了python。新建一个a.py文件，然后一顿猛如虎的撸代码：
```python
import requests url = “******” params = "******" re = reqeste.get(url, params)
```

你家领导，一看，还行，提醒你少了断言，于是你加进去了

```python
assertEqual (content.msg, "***"）
```


你家领导可能是比较关心你，于是又丢了几个接口给你，你开始依葫芦画瓢，流水账代码搞起。完事后，你仔细想想总觉得不对，于是你将每个请求都封装起来，大概长这样：
```python
def qingqiu_a():

url = "***"

...

def fangwen_b():

url = "***"

...

def shenmegui_c():

url = "***"

...

```

显然，你的领导是爱你的，某天他又丢给你几十个接口，然后希望你输出报告。你：“exm？”，改改改。于是你引入了unittest单元测试框架、HTMLTestRunner等等。

正打算将各个测试用例分类重新规整，你领导又来了。如果世界上有真爱这种东西存在的话，那你领导对你的爱便是了。

“我又从开发那里帮你要了100个接口过来测，开不开心？”

“你的脚本给我看下，这个是啥意思？可以在我那边运行吗？”

“你的脚本怎么这么多啊，好乱啊”

“这个接口我要做性能测试，还有这个、这个。。。”

“这几个接口是串联起来的，你处理下”

…

你几近崩溃，为什么，为什么不能简单点。

（脑补《演员》）

幸好，你并没有放弃，你在某个机缘巧合下发现了一个叫httprunner的测试框架，这个框架使用的是yaml格式的文本来描述脚本，只需一行命令即可进行接口测试。在连夜研究完这个框架后，你发出慨然长叹：“原来接口测试可以这么优雅的写啊！”

于是你将几百个接口丢进一个yaml文本里，执行了下面这条命令：

hrun api.yaml

刷刷刷，搞定，X吃惊的看着你，似乎在看一头变帅的猪

“这次咋这么快？平时光调试都得一两天。”

“测试报告不错！”

“数据也都校验了。”

“咦，这脚本简单，我都看得懂，可以可以，很强势！”

…

so，你是怎么使用httprunner的呢？

* * *


### 0，安装
安装好python3，直接pip install httprunner即可

hrun -V 查看版本，能看到版本信息，就代表安装成功

hrun -h 查看帮助信息

### 1，用例格式
通常一个脚本文件里面有如下模块：

config

test

test

即：全局配置、用例、用例

config模块里面定义的是整个文本测试集的变量，即全局变量

test模块里面定义的是具体接口请求，下面看个具体例子

### 2，举个例子
以某快递查询接口为例，新建一个yaml文件，命名为test_post_api.yaml
```python
- config:
    name: test kuaidi100 api
    request:
        base_url: http://www.kuaidi100.com
            
- test:
    name: test kuaidi100 one
    request:
        url: /query
        method: GET
        params:
            type: huitongkuaidi
            postid: 350757858666
#这个我在windows10下执行发现有问题，用charles抓包后，har2case转化为yaml，再执行就可以了

```

```python
#在httprunner 2.1.1版本下执行正常
-   config:
        name: testcase description
        variables: {}
-   test:
        name: /query
        request:
            headers:
                User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
                    (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36
            method: GET
            params:
                postid: '350757858666'
                type: huitongkuaidi
            url: http://www.kuaidi100.com/query
        validate:
        -   eq:
            - status_code
            - 200
        -   eq:
            - headers.Content-Type
            - text/html;charset=UTF-8

```
yaml格式类似与json，可以看成是优雅的json。yaml中，跟python一样，也是空格缩进表示同一层级，不过没有python那么严格，只要缩进空格数一样就是同一级，“-”python读取出来是list，“#”用来注释，更多语法可以去官网学习。

config模块

name 本用例集名称

request 请求全局变量，包括base_url（公共host）、headers等

base_url 全局公共host，也可以不定义，用例中写全url即可

以上全局配置，除了name，其他都是非必要的，根据需要添加。

test模块

name 本条测试用例的名字

request 请求体

url 请求的路径，由于全局变量已经定义好host，这里就直接填写后面的路由即可

method 请求方式

params 请求参数

示例是某快递查询接口，脚本初步写好，接下来开始测试吧，怎么测试脚本？

打开cmd，进入到该文件目录，执行命令hrun test_post_api.yaml回车即可。

![710267d955d6d46d757af9d9f4e4af63.png](https://img-blog.csdnimg.cn/20190105174049197.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3h1NTQ3ODIzNTAx,size_16,color_FFFFFF,t_70)


成功，cool，可以看到一条用例测试通过，而且还在脚本所在目录生成了report文件夹，生成的测试报告就放在里面，报告名字为测试时间戳。报告长这样，还是蛮清爽的。

![9e5e198a0964f396c64c4f63ca4607cc.png](https://img-blog.csdnimg.cn/20190105174104986.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3h1NTQ3ODIzNTAx,size_16,color_FFFFFF,t_70)


点击log，可以查看详细日志

![6466034ab0b0b113f7d5ca56845b5170.png](https://img-blog.csdnimg.cn/20190105174124986.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3h1NTQ3ODIzNTAx,size_16,color_FFFFFF,t_70)


### 3，断言
虽然运行成功，但我们无法判断请求的结果与我们的预期是否一致。这个时候就需要断言。httprunner中断言很简单，通过在用例里面增加validate参数实现，如下：

![5a81b9e0d06accfd2f4d50351a6ef44b.png](https://img-blog.csdnimg.cn/20190105174148296.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3h1NTQ3ODIzNTAx,size_16,color_FFFFFF,t_70)

那么怎么知道如何定义被断言的数据呢？即上图中的content.message等。

浏览器执行该接口，其返回值是字典（如下，这些字典数据存在content变量里面），可以直接通过content后面接“.key”获取value值，再判断与我们给出的值是否相等，以此判断用例是否通过。如：content.message断言值设置为“ok”，如果其对应的value等于“ok”，就表示通过。

```python

{"message":"ok","nu":"350757858666","ischeck":"1","condition":"F00","com":"huitongkuaidi","status":"200"......
```


加好想要的断言后，再次执行用例，打开报告查看日志，可以看到，日志里面清楚的记录了所以的断言结果。

![14a3f15991167404c598b010e31d78de.png](https://img-blog.csdnimg.cn/20190105174227361.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3h1NTQ3ODIzNTAx,size_16,color_FFFFFF,t_70)

### 4，参数传递
在做接口测试时，经常需要将上一个接口返回的结果，传入到下一个接口中当着参数，httprunner中使用extration参数来进行参数的传递。由于演示接口只有一个，切接口返回值里面有运单号，就直接拷贝了上面的用例作为接受参数的用例。故可以将第一个用例返回值中的运单号提取出来，传入第二个用例当做参数，只需在前面加$就可以引用该参数，look

```python
- config:
    name: test kuaidi100 api
    # parameters:
        # - user_id: [1001, 1002, 1003, 1004]
    request:
        base_url: http://www.kuaidi100.com
            
- test:
    name: test kuaidi100 one
    request:
        url: /query
        method: GET
        params:
            type: huitongkuaidi
            postid: 350757858666
    validate:
        - eq: [status_code, 200]
        - eq: [content.message, "ok"]
        - eq: [content.com, "huitongkuaidi"]
        - eq: [content.nu, "350757858666"]        
    extract:
        - postid: content.nu
        
- test:
    name: test kuaidi100 two
    request:
        url: /query
        method: GET
        params:
            type: huitongkuaidi
            postid: $postid
    validate:
        - eq: [status_code, 200]
        - eq: [content.message, "ok"]
        - eq: [content.com, "huitongkuaidi"]
        - eq: [content.nu, "350757858666"]     

```

执行测试，通过，cool：

![37c81ee9292668645330de003f82095f.png](https://img-blog.csdnimg.cn/20190105174319663.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3h1NTQ3ODIzNTAx,size_16,color_FFFFFF,t_70)
### 5，脚本运行方式
上面也提到了，单个脚本可以使用：hrun ***.yaml

当要同时运行多个脚本文件的时候，后面接多个文件：hrun a.yaml b.yaml c.yaml

当然，也可以直接指定文件夹，运行文件下所以脚本：hrun ***\test\

### 6，参数化
诚然，无论在日常接口测试，还是性能测试，都对数据有要求，特别是性能测试，需要大量数据，这个时候就需要对传递的参数进行参数化了。

httprunner中支持的参数化方法有：csv文本、自定义函数

#### 6.1、使用csv文本进行参数化
在脚本同级目录下新建csv文件，打开存入需要的数据，保存

![aa2183b9f07cb97068e63d317598a960.png](https://img-blog.csdnimg.cn/2019010517435185.png)

引用： 增加一个parameters参数，通过调用P(∗∗∗.csv)方法来读取csv文本中的数据，也是使用 {P(***.csv)}方法来读取csv文本中的数据，也是使用P(∗∗∗.csv)方法来读取csv文本中的数据，也是使用+变量名引用参数。

值得注意的是，通常来说，一个CSV文件中会放多列数值，那么这个时候，各列参数通过“-”连接来读取参数，如：要传postid1、name两列参数，这样写就可以postid1-name: ${P(postid.csv)}

![be0d218e5c458693839a1ab2ce703e9c.png](https://img-blog.csdnimg.cn/20190105174403731.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3h1NTQ3ODIzNTAx,size_16,color_FFFFFF,t_70)


来来来，测试下，“Ran 4 tests in 2.076s”，good。因为csv中有4个参数，用例也运行了4遍，查看log，4个参数都是csv里面的，而且是顺序的。

![1c457652384e0813bae267899eb4b433.png](https://img-blog.csdnimg.cn/20190105174416547.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3h1NTQ3ODIzNTAx,size_16,color_FFFFFF,t_70)


#### 6.2、使用自定义函数进行参数化

还是在脚本下，新建debugtalk.py文件，注意，这个文件名字就不能随便取啦，固定的。

![188d8c140e6aeb4a8a144d31e4ee39c7.png](https://img-blog.csdnimg.cn/20190105174435165.png)

![e84c2513d9b3da8251130c50867098bb.png](https://img-blog.csdnimg.cn/20190105174438867.png)

![76db21dd482f8a9ba4a06486c766fcf7.png](https://img-blog.csdnimg.cn/20190105174443343.png)


与csv引用类似，脚本中使用${get_postids(5)}来引用函数，5表示想要获取的参数个数，执行结果如下：

![3b9e7b494f87af0a4136e49d637b6df0.png](https://img-blog.csdnimg.cn/20190105174458948.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3h1NTQ3ODIzNTAx,size_16,color_FFFFFF,t_70)

至此，httprunner接口测试框架的主要功能、或者说接口测试需要用到的大部分功能、场景，大概说了一遍。这样做接口测试是不是感觉非常的简单、优雅呢？

注意，由于这个框架集成了locusts性能测试工具，故还可以非常方便的进行性能测试，与接口测试类似，执行如下命令：locusts -f test_post_api.yaml，浏览器打开http://localhost:8089即可进行性能测试。

最后，这是一份非常简单的入门教程，也还算比较全。其中有些细节，官网也没有给出，写的时候还是整了蛮久的。其他更多功能、细节，还是请参考官方中文教程网站：http://cn.httprunner.org/ 源码挪步：https://github.com/httprunner/httprunner


欢迎扫描关注我的公众号，欢迎投稿，一起探讨技术、人生，谢谢。
* * *
作者：xuyiwen007 
来源：CSDN 
原文：https://blog.csdn.net/xu547823501/article/details/85862702 
版权声明：本文为博主原创文章，转载请附上博文链接！









