慕课接口自动化

python版本：3.6.5

课程：https://www.dazhuanlan.com/2019/10/05/5d98078b0522b/
https://coding.imooc.com/class/374.html

CSDN 别人的博客
https://blog.csdn.net/iam_emily/article/details/82670540



代码主要来源：
Desktop\2muke_api\base

1、接口方法实现和封装runmethod.py

2、组织测试和生成报告test_method.py

注意点：

- HTMLTestRunner.py文件使用的python3版本，详情见：https://github.com/Valuebai/awesome-python-io/issues/9

- python3以后mock模块已经整合到了unittest测试框架中，不用再单独安装，直接使用from unittest import mock




3 测试数据处理
./data/get_data.py

4 主函数main
./main/main.py

5 添加日志
具体说明在./common/logConf.py 中

## 【部署报错】在pycharm执行正常，在命令行窗口报错No module named 'base'
import os, sys
# 解决在命令行窗口报错No module named 'base'，需要放在最前面
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


```
慕课网《Python接口测试框架实战与自动化进阶》2017
『课程目录』:
Python接口自动化测试框架实战
本课程带你从接口基础知识回顾开始，主流的Fiddler、Requests、Unittest、Mock等接口测试工具/框架，全程以慕课网作为案例实战应用，从简单接口入手到自己如何去设计、开发整个接口自动化测试框架，带你设计Python接口自动化测试框架，让你在测试领域走的更远！

第1章 接口测试基础回顾
对接口基础知识进行回顾，课前预习

1-1 接口自动化测试从基础到框架-导学 试看
1-2 接口基础知识回顾
1-3 接口测试基础面试解答
第2章 fiddler在工作中的运用
讲解在工作中如何使用fiddler，提高工作效率，增加对接口的了解，对接口自动化打下基础

2-1 如何抓接口
2-2 大量重复数据模拟以及过滤规则使用
2-3 模拟接口响应数据 试看
2-4 fiddler进行接口测试
第3章 如何开发getpost接口
通过了解接口的实现原理以及实现方式，为编码打下基础，也为工作中和开发更加方便的沟通，同时也是为了对接口进行自动化测试打下基础

3-1 开发接口环境搭建
3-2 django之接口工作原理
3-3 django之post接口开发
3-4 django之get请求
3-5 django之接口数据处理
第4章 requests库的相关使用
通过介绍接口测试必不可少的requests库的基础知识以及他简单的工作方式，让用户知道如何去实现接口自动化测试，增强基础知识掌握

4-1 requests安装
4-2 requests简单使用-post
4-3 重构发送post请求
4-4 重构get请求+格式化响应数据
4-5 使用类封装接口测试脚本
第5章 unittest使用
通过介绍unittest的使用，方便在实际中对case的管理，并达到接口自动化的目的

5-1 unittest简单使用
5-2 unittest和request重构封装
5-3 unittest中assert的使用
5-4 unittest中case的管理及运用
5-5 unittest和HTMLTestRunner结合生成报告
5-6 unittest之常见面试解答及知识回顾
第6章 mock服务入门到实战
mock服务是接口测试必不可少的，也是为了让测试和开发同时进行工作，不因开发的进度而影响接口脚本的开发，奠定代码基础

6-1 如何在接口开发阶段编写接口测脚本
6-2 mock服务介绍以及实现原理
6-3 在case中通过底层函数实现mock 试看
6-4 重构封装mock服务
第7章 从接口自动化框架设计到开发
通过从用例的设计到框架的设计以及初级代码的实现到代码的重构，让一个初级用户完成整个学习过程，从而掌握python知识，也懂得了如何去开发属于自己的接口自动化测试框架

7-1 如何设计一个接口自动化测试框架
7-2 学习python操作excel获得内容
7-3 重构操作excel函数
7-4 学习操作json文件
7-5 重构json工具类
7-6 封装获取常量方法
7-7 封装获取接口数据
7-8 post、get基类的封装
7-9 主流程封装及错误解决调试
7-10 返回数据格式处理以及调错
7-11 获取接口返回状态
7-12 通过预期结果判断case是否执行成功
7-13 将测试结果写入到excel中
7-14 数据依赖问题从设计思路开始
7-15 数据依赖问题方法封装之通过case_id获取case数据
7-16 数据依赖问题之根据规则提取响应数据
7-17 数据依赖问题之依赖结构构建
7-18 数据依赖问题之流程实施
7-19 case运行结果统计
7-20 构建发送邮件服务
7-21 结果统计+报告通知
第8章 持续集成
从环境到运行，了解持续集成如何使用

8-1 持续集成环境搭建
8-2 持续集成之项目配置
第9章 获取cookie及请求处理
获取cookie思路分析，模拟登录获取cookie请求订单接口，重构封装携带cookie请求处理流程

9-1 获取cookie思路分析
9-2 模拟登录获取cookie请求订单接口
9-3 如何拿到cookie去写入文件
9-4 携带cookie处理请求数据多重字典问题
9-5 重构封装携带cookie请求处理流程
第10章 数据库相关操作
连接数据库查询数据，获取数据库数据重构及转换数据，返回数据和数据库数据进行对比，格式化数据对结果进行回写

10-1 连接数据库查询数据
10-2 获取数据库数据重构及转换数据
10-3 返回数据和数据库数据进行对比_
10-4 格式化数据对结果进行回写
第11章 接口测试异常处理
接口测试中遇见异常接口我们该如何处理？我们应该从哪些地方分析?带你从问题本源去分析解决问题。

11-1 分析异常接口处理
11-2 异常接口处理
11-3 如何处理https接口
11-4 put、delete接口处理
11-5 webservice接口测试方法介绍及简单使用
11-6 webservice接口测试获取所有测试方法封装
11-7 分析解决webservice无法通过参数直接调用方法问题
11-8 webservice接口测试封装
本课程已完结


链接：https://pan.baidu.com/s/1jYBYoY8FAm6XEu8ebwwnbw
提取码：pwkd

```