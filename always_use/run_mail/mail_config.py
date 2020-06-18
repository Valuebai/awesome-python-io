#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# [登录信息]
# 邮箱账号/用户名
mail_user = "520huibo@sina.com"
# 邮箱密码
# 如果：qq、sina等邮箱开启POP3/IMAP/SMTP，这里直接填生成的[授权码]，而不是密码
mail_pass = "fc1d768363876fd5"
# 邮箱的smtp服务器地址
mail_host = "smtp.sina.com"

# [邮件信息]
# 发件人
mail_sender = "520huibo@sina.com"
# 收件人
mail_receiver = ["luhuibo306@foxmail.com", "745919068@qq.com"]
# 邮件主题
mail_subject = "这是一封来自火星的研究报告~"
# 邮件内容
mail_content_text = "传说中的2020年，对面的地球发生了很多事情..."
# 邮件附件的路径
path_mail_attachment = "./"

# [其他收件人信息]
mail_others = []
TesterEmails = ["xxx@qq.com", "123456@qq.com"]
BackEmails = ["xxx@qq.com", "123456@qq.com"]
AndroidDeveloperEmails = ["xxx@qq.com", "123456@qq.com"]
IOSDeveloperEmails = ["xxx@qq.com", "123456@qq.com"]
H5DevelopEmail = ["xxx@qq.com", "123456@qq.com"]

# 根据需要添加相应的收件人 + XXX + XXX
mail_receiver = mail_receiver + mail_others
