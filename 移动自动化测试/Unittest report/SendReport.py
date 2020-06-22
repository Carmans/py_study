#!/usr/bin/python
# -*- coding: utf8 -*-
import smtplib
from email.mime.text import MIMEText

mail_host = "smtp.163.com"  # 设置服务器
mail_user = "shenzhoutester@163.com"  # 用户名
mail_pass = "tester123"  # 口令
mail_postfix = "163.com"  # 发件箱的后缀

# to_list：收件人；sub：主题；content：邮件内容
def send_mail(to_list, sub, reportpath):
    file = open(reportpath, "rb")
    content = ""
    for line in file.readlines():
        content = content + line.replace("class='hiddenRow'", "")

    # 这里的hello可以任意设置，收到信后，将按照设置显示
    me = "TestCenter" + "<" + mail_user + ">"
    # 创建一个实例，这里设置为html格式邮件
    msg = MIMEText(content, _subtype='html', _charset='utf-8')
    # 设置主题
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        s = smtplib.SMTP()
        # 连接smtp服务器
        s.connect(mail_host)
        # 登陆服务器
        s.login(mail_user, mail_pass)
        # 发送邮件
        s.sendmail(me, to_list, msg.as_string())
        s.close()
        return True
    except Exception, e:
        return False