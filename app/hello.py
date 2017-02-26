#!/usr/bin/env python3.5
# -*- coding:utf-8 -*-
__author__ = 'hanyong'

from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config.update(
    #EMAIL SETTINGS
    MAIL_SERVER='smtp.163.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    # 下面写的是你的账号
    MAIL_USERNAME = 'hanlrflask@163.com',
    # 下面写的是授权码 不是你的密码哦 被坑了一天的时间 哎
    MAIL_PASSWORD = 'dx0873667979'
    )

mail = Mail(app)

@app.route("/")
def index():
    # 发送的信息不能乱写 要不然会被过滤的
    msg = Message(subject="这里不能写英文的你好",
                  # 这个账号和你上面的那个MAIL_USERNAME 一样
                  sender='hanlrflask@163.com',
                  # 这个收件人
                  recipients=['hanyong0413@126.com'])
    msg.html = "<b>testing 这都不行？</b> html"

    mail.send(msg)

    return '<h1>Sent</h1>'

if __name__ == '__main__':
    app.run(debug=True)