# -*- coding: UTF-8 -*-
#发送邮件（测试成功）
import smtplib
from email.mime.text import MIMEText

msg = MIMEText('','plain','utf-8')
from_addr = ""
password = ""
to_addr  = ""
smtp_server = ""

server = smtplib.SMTP_SSL(smtp_server,465)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()


