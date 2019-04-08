
##### 反爬虫策略

1. 返回错误的状态码：302、 403、 404、 500等，302是重定向,比如微博的登录页面,他就跳转了几个页面,这个时候使用scrapy框架,   可以用跟随那个
2. cookie、 user-agent等 headers头信息一般服务器都会都cookie,user-agent进行判断
3. 登录认证、故意制造复杂的流程
    * a)比如登录验证,故意恶心你
4. 用户户行为分析
    * a)他通过登录时的输入时间,这个时候我用for循环输入,睡个0.1秒,模拟人正常输入速度.
5. 请求频率限制a)这个很少很会的,
6. ajax动态加载、iframe异步加载
7. 短信、图形、拖动、拼图等各种验证码就用自己手动填,因为用机器学习,其实首先,正确不高,还有就是需要大量数据喂养,说不定喂养了后,生成代码又变了就废了
8. 页面数据混淆、造假a)这里在我们写入sql数据库的时候,坏的程序员可能会sql注入,直接删掉你的数据库
9. 隐身链接
隐身链接,在页面不起眼的地方放链接,设置display=none,外面是a标签,发送到特定的网址,然后直接封ip,如果你想取出属性判断,所有display=none属性删除,设置style:color=和底面颜色一样,这样你也看不到了,写Img标签,像素点1x1,也看不见,style定义posision,绝对定位,放到页面外,隐身链接的精髓在于随机定义一些看不见的链接.




如何应对反爬虫
1.伪造headers信息
2.ip代理
3.限制请求频率
4.使用模拟器模仿浏览器行为
elenium控制PhantomJS登录微博

5.适当人工干预

常见爬虫框架
scrapy,pyspider,selenium PhantonJS


1.常用的HTTP库和工具具有哪些？
a)postman 谷歌浏览器检查
2.常用的python解析html的库有哪些？
a)beautifulsoup4
b)lxml 
c)re
3.常见的爬虫框架和工具具有哪些？
scrapy,pyspider,selenium PhantonJS
a)
4.写出遇到过的反爬虫措施以及应对应对案。
a)
5.看过哪些爬虫相关的书？
6.如何提高爬取效率？
增加请求并发数: CONCURRENT_REQUESTS = 100 
增加线程池数量：REACTOR_THREADPOOL_MAXSIZE = 20
降低log级别：LOG_LEVEL = ‘INFO'
禁用cookies： COOKIES_ENABLED = False 
禁止重试：RETRY_ENABLED = False 
禁止重定向：REDIRECT_ENABLED = False
减少超时等待：DOWNLOAD_TIMEOUT = 15


7.robots.txt是什么？
爬虫协议,网站通过robots协议告诉搜索引擎哪些页面抓取,哪些页面不能抓取
8.python2和 python3的区别
python2 raw_input         python3 input 
python2 定义编码格式,      python3 默认utf-8编码
python3性能比python2慢
Python2 print               python3 print()
9.python中的enumerate有何作用？
a)内置函数,枚举,列举的意思,对于可迭代对象,将其组成一个索引序列,同时获得索引和值.我举个例子
b)	list1 = ["这", "是", "一个", "测试"] for index, item in 	enumerate(list1): print index, item
0 这 1 是 2 一个 3 测试

10.说明python的 import机制
a) Python中所有加载到内存的模块都放在sys.modules。当import一个模块时首先会在这个列表中查找是否已经加载了此模块，加载了则只是将模块的名字加入到正在调用import的模块的Local名字空间中。如果没有加载则从sys.path目录中按照模块名称查找模块文件，模块文件可以是py、pyc、pyd，找到后将模块载入内存，并加入到sys.modules中，并将名称导入到当前的Local名字空间。

11.列出常见的关系型数据库和非关系型数据库。

12.HTTP和 HTTPS有何区别？
超文本传输协议,安全超文本传输协议
http    htpps
端口	80			443
有CA证书
明文		安全,ssl加密

13.GET和 POST方法法有何区别？
get没有body,post有body
14.scrapy如何实现中断后继续爬取？
scrapy-redis 自动实现, scrapy jobdir

15.简述scrapy的架构和爬取流程。
架构,items,middlewares,pipilines,settings,spider.
中间件:介入到scrapy的spider处理机制的钩子框架,中间件用来处理发送给spider的response及spider产生的item和request

16.爬虫状态持久化
 	-s JOBDIR=/tmp/qianmu