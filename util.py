# 日期时间相关
import time
from datetime import datetime
from chinese_calendar import is_workday
# 邮件服务相关
import smtplib
from email.mime.text import MIMEText
# 财经接口
import tushare as ts


def is_trade_time():
    now = int(time.strftime('%H%M'))
    return 930 <= now <= 1130 or 1300 <= now <= 1500


def is_closed_time():
    now = int(time.strftime('%H%M'))
    return now > 1500


def is_trade_day(date):
    mydate = datetime.strptime(date, '%Y-%m-%d').date()
    if is_workday(mydate):
        if mydate.isoweekday() < 6:
            return True
        return False


def get_stock_price(code):
    data = ts.get_realtime_quotes(code)
    price = float(data['price'])
    return price


def send_mail(content):
    # 设置服务器所需信息
    # 163邮箱服务器地址
    mail_host = 'smtp.163.com'
    # 163用户名
    mail_user = 'imliu2005@163.com'
    # 密码(部分邮箱为授权码)
    mail_pass = 'UPKUKKFHDUMKVKYB'
    # 邮件发送方邮箱地址
    sender = 'imliu2005@163.com'
    # 邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
    receivers = ['ningliu@keyamedical.com']

    # 邮件内容设置
    message = MIMEText(content, 'plain', 'utf-8')
    # 邮件主题
    message['Subject'] = 'stock-notify'
    # 发送方信息
    message['From'] = sender
    # 接受方信息
    message['To'] = receivers[0]

    # 登录并发送邮件
    try:
        smtpObj = smtplib.SMTP()
        # 连接到服务器
        smtpObj.connect(mail_host, 25)
        # 登录到服务器
        smtpObj.login(mail_user, mail_pass)
        # 发送
        smtpObj.sendmail(sender, receivers, message.as_string())
        # 退出
        smtpObj.quit()
        print('send email success')
    except smtplib.SMTPException as e:
        print('send email error', e)
