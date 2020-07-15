#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2020/6/16 16:10
# @Software: PyCharm
# @Author  : https://github.com/Valuebai/
"""
    <mail>.$ {发送邮件}
    ~~~~~~~~~~~~~~~

    分为[mail_config.py]配置文件和[send_mail.py]调用发送文件, 可发送附件1，html附件2，图片附件3，多个附件List

    1. SMTP是发送邮件的协议，Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件；
    2. Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件；
    3. Smtplib是关于 SMTP(简单邮件传输协议)的操作模块，在发送邮件的过程中，起到服务器之间互相通信的作用；
    4. Email是用来设置服务器之间通信的信息，包括信息头、信息主体等等；
    5. 用脚本发邮件时，需要先打开自己邮箱的 SMTP 功能，各家邮箱的设置方法不同，可自行百度；

    Usage Example
    -------------
    :: 1. 在mail_config 设置相关信息
    :: 2. 代码中用的是print，可全局替换为日志的 logger
    :: 3. 调用时导入模块
    # 发送1-3个附件
    BaseMail().sendEmail(subject='新标题', text='正文内容', attach_file_path='./test地球日志.txt',
                         mail_receiver_list=["aa@foxmail.com", "bb@qq.com"])

    # 发送多个附件
    BaseMail().sendEmail(subject='[Test]发送附件', content='', attack_files_list=['../outputs/result_apk_meiju.json',
                                                                              '../outputs/result_apk_meiju.html',
                                                                              '../outputs/apk_pie_chart_meiju.png'],
                         mail_receiver_list=["xx@qq.com"])
"""

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header

from always_use.run_mail.mail_config import *


class BaseMail(object):

    def __init__(self):
        # 设置 smtplib 所需参数
        self.__smtpserver = mail_host
        self.__username = mail_user
        self.__password = mail_pass
        self.__sender = mail_sender
        self.__receiver = mail_receiver
        self.__subject = mail_subject
        self.__content = mail_content_text
        self.__attach_path = path_mail_attachment

    # 设置邮件标题
    def setSubject(self, subject):
        # 如果传入为空，读取默认的
        if not subject:
            subject = self.__subject
        subject = Header(subject, 'utf-8').encode()
        return subject

    # 设置邮件正文
    def setContent(self, content):
        # 如果传入为空，读取默认的
        if not content:
            content = self.__content
        text = MIMEText(content, 'plain', 'utf-8')
        return text

    # 设置文件作为邮件附件
    @staticmethod
    def setFile(source_file_path):
        """

        Args:
            source_file_path: 文件路径，str

        Returns: MIMEText 构造对象

        """
        # 如果路径为空，返回空
        if not source_file_path:
            return None
        try:
            with open(source_file_path, 'rb') as f:
                file_data = f.read()
        except Exception as e:
            print("读取邮件-附件失败!" + '\n' + '异常信息:{}'.format(e))
            return None
        # strText：邮件正文，可以是普通str字符串，也可以是html字符串
        # subType：正文类型，有text / plain和text / html两种
        # encode：一般是utf - 8，用于保证多语言的兼容性。
        text = MIMEText(file_data, 'base64', 'utf-8')
        text["Content-Type"] = 'application/octet-stream'
        text.add_header('Content-Disposition', 'attachment', filename=os.path.basename(source_file_path))

        return text

    # 设置邮件html文件作为附件
    @staticmethod
    def setHtmlFile(html_path):
        """

        Args:
            html_path: html的路径

        Returns: MIMEText 构造对象
        """
        # 如果路径为空，返回空
        if not html_path:
            return None
        try:
            with open(html_path, 'rb') as f:
                image_data = f.read()
        except Exception as e:
            print("setImageFile()读取图片失败!" + '\n' + '异常信息:{}'.format(e))
            return None
        text_html = MIMEText(image_data, 'html', 'utf-8')
        text_html.add_header('Content-Disposition', 'attachment', filename=os.path.basename(html_path))

        return text_html

    # 设置图片作为邮件附件
    @staticmethod
    def setImageFile(source_image_path):
        """

        Args:
            source_image_path: 读取的图片路径

        Returns: MIMEImage构造对象
        """
        # 如果路径为空，返回空
        if not source_image_path:
            return None
        try:
            with open(source_image_path, 'rb') as f:
                image_data = f.read()
        except Exception as e:
            print("setImageFile()读取图片失败!" + '\n' + '异常信息:{}'.format(e))
            return None
        image = MIMEImage(image_data)
        image.add_header("Content-ID", "<image1>")
        image.add_header("Content-Disposition", "attachment", filename=os.path.basename(source_image_path))

        return image

    # 发送邮件
    def sendEmail(self, subject, content, attach_file_path=None, attach_picture_path=None, attach_html_path=None,
                  attack_files_list=None, mail_receiver_list=None):
        """

        smtplib 模块主要负责发送邮件：是一个发送邮件的动作，连接邮箱服务器，登录邮箱，发送邮件（有发件人，收信人，邮件内容）。
        email   模块主要负责构造邮件：指的是邮箱页面显示的一些构造，如发件人，收件人，主题，正文，附件等。

        Args:
            subject: 必填，邮件的标题，str
            content:    必填，邮件的正文，str
            attach_file_path:       选填，邮件的附件.所在的地址，添加单个附件，str
            attach_picture_path:    选填，邮件的图片.所在的地址，添加单个附件，str
            attach_html_path:       选填，邮件的html.所在的地址，添加单个附件，str
            attack_files_list:      选填，邮件的附件.所在的地址，添加多个附件，list,如["aa.txt","bb.txt"]
            mail_receiver_list:     选填，list，重新设置新的收件人，否则使用配置的, 如["xx@qq.com","bb@qq.com"]

        MIMEMultipart有三种类型：multipart/alternative, multipart/related和multipart/mixed。
            - 邮件类型为"multipart/alternative"的邮件包括纯文本正文（text/plain）和超文本正文（text/html）。
            - 邮件类型为"multipart/related"的邮件正文中包括图片，声音等内嵌资源。
            - 邮件类型为"multipart/mixed"的邮件包含附件。向上兼容，如果一个邮件有纯文本正文，超文本正文，内嵌资源，附件，则选择mixed类型。
        """
        msg = MIMEMultipart('mixed')
        # 设置邮件的标题、发件人、收件人
        msg['Subject'] = self.setSubject(subject)
        msg['From'] = self.__sender + " <" + self.__sender + ">"
        # 判断是否使用新的收件人
        if mail_receiver_list is None:
            set_mail_receiver = self.__receiver
        else:
            set_mail_receiver = mail_receiver_list
        msg['To'] = ','.join(set_mail_receiver)

        # 添加邮件的正文
        msg.attach(self.setContent(content))
        # 添加邮件文件附件（单个）
        if attach_file_path:
            msg.attach(self.setFile(attach_file_path))
        # 添加图片作为附件（单个）
        if attach_picture_path:
            msg.attach(self.setImageFile(attach_picture_path))
        # 添加邮件的html（单个）
        if attach_html_path:
            msg.attach(self.setHtmlFile(attach_html_path))
        # 添加邮件文件附件（多个）
        if attack_files_list:
            for file in attack_files_list:
                msg.attach(self.setFile(file))

        # 发送邮件
        sm = smtplib.SMTP()
        # sm = smtplib.SMTP_SSL()  # 注意：如果遇到发送失败的情况（提示远程主机拒接连接），这里要使用SMTP_SSL方法
        try:
            sm.connect(self.__smtpserver)
            sm.login(self.__username, self.__password)
            sm.sendmail(self.__sender, set_mail_receiver, msg.as_string())
            print("邮件发送成功!")
        except Exception as e:
            print("邮件发送失败!" + '\n' + '异常信息:{}'.format(e))
        finally:
            sm.quit()


if __name__ == "__main__":
    # BaseMail().sendEmail(subject='[Test]发送附件', content='', attach_file_path='../outputs/result_apk_meiju.json',
    #                      attach_html_path='../outputs/result_apk_meiju.html',
    #                      attach_picture_path='../outputs/apk_pie_chart_meiju.png',
    #                      mail_receiver_list=["xx@qq.com"])
    BaseMail().sendEmail(subject='[Test]发送附件', content='', attack_files_list=['../outputs/result_apk_meiju.json',
                                                                              '../outputs/result_apk_meiju.html',
                                                                              '../outputs/apk_pie_chart_meiju.png'],
                         mail_receiver_list=["xx@qq.com"])
