# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

def send_data_mail(mail_host,mail_user,mail_pass,mail_message,receivers,subject):

    # 第三方 SMTP 服务
    sender = mail_user
    message = MIMEText(mail_message, 'html', 'utf-8')
    message['From'] = mail_user
    message['To'] = ";".join(receivers)
    print(message['To'])
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
        smtpObj.login(mail_user,mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print "邮件发送成功"
    except smtplib.SMTPException,e:
        print "Error: 无法发送邮件"
        print e
if __name__ == '__main__':
    mail_host="smtp.126.com"  #设置服务器
    mail_user="wyj880220@126.com"    #用户名
    mail_pass="Lifeifei@#880612"   #口令
    receivers = ['yjwang@qdio.ac.cn','340041928@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    subject = '数据下载完成邮件通知'
    mail_message="<p>尊敬的用户您好：</p><p>您在服务器的数据下载完成,请及时登录服务器整理归类</p>"
    send_data_mail(mail_host,mail_user,mail_pass,mail_message,receivers,subject)