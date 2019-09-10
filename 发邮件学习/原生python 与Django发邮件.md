## 原生python 发邮件

```python 
#发送纯文本邮件

#邮件发送库
import  smtplib
#邮件的标题
from email.header import Header
#邮件的正文
from email.mime.text import MIMEText


"""
user:发送方的用户名
pwd：授权码
sender：发送方，
recevier：接收方,为一个列表
content：正文
title：标题
"""
def sendEmail(user,pwd,sender,recevier,content,title):
 mailHost = "smtp.163.com"  #163的服务器地址【163的域名】

 #一：准备工作
 #1.创建一个对象，表示邮件对象
 message = MIMEText(content,"plain","utf-8")
 #2.设置邮件的发送方
 message["From"] = sender
 #3.设置邮件的接收方
 message["To"] = ",".join(recevier)
 #4.设置邮件的标题
 message["Subject"] = title

 #二、发送邮件
 #1.启动SSL发送邮件，端口号一般为465
 smtpObj = smtplib.SMTP_SSL(mailHost,465)
 #2.登录邮箱进行验证
 smtpObj.login(user,pwd)
 #3.开始发送
 #参数：发送方 接收方，  发送的内容
 smtpObj.sendmail(sender,recevier,message.as_string())

 print("邮件发送成功")

if __name__ == "__main__":
 user = "18501970795@163.com"
 pwd = "yang0122"

 sender = user
 recevier = ["1490980468@qq.com","549412132@qq.com","1571405800@qq.com","185798766@qq.com","1757965647@qq.com"]

 content = "~~~~~~~~~你真帅"
 title = "你收到邮件了吗？"

 sendEmail(user,pwd,sender,recevier,content,title)
```

```python
#发送带附件的邮件

import  smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

user = "18501970795@163.com"
pwd = "yang0122"
sender = user
recevier = ",".join(["18501970795@163.com","549412132@qq.com","1571405800@qq.com","185798766@qq.com","1757965647@qq.com"])

#multipart表示多个部分
msg = MIMEMultipart()
msg["From"] = sender
msg["To"] = recevier
msg["Subject"] = "带有附件的邮件~~~~~"

#正文部分
text = MIMEText("我是纯文本部分，正文部分")
msg.attach(text)

#附件部分
imageContent = open("dog.jpg","rb").read()
application = MIMEApplication(imageContent)
application.add_header("Content-Dispositon","attachment",filename="dog.jpg")
msg.attach(application)

#发送邮件
smtpObj = smtplib.SMTP()
smtpObj.connect("smtp.163.com")
smtpObj.login(user,pwd)
smtpObj.sendmail(sender,recevier,msg.as_string())

#退出服务
smtpObj.quit()

print("带有附件的邮件发送成功")
```

## Django发邮件

settin.py中配置

```python
# 设置邮件域名
EMAIL_HOST = 'smtp.163.com'
# 设置端口号，为数字
EMAIL_PORT = 25
# 设置发件人邮箱
EMAIL_HOST_USER = '15129903773@163.com'
# 设置发件人 授权码
EMAIL_HOST_PASSWORD = 'zfl321'
# 设置是否启用安全链接
EMAIL_USER_TLS = False
# 设置发件人
EMAIL_FROM = 'xxxxxxxxxxx@sina.cn'          
```



```python
from django.shortcuts import render
from django.http import HttpResponse
# 引入发送邮件的模块
from django.core.mail import send_mail, send_mass_mail, EmailMultiAlternatives

# 发送普通邮件
def send_email(request):
    if request.method == 'POST':
        # 值1： title    值2： message
        # 值3： sender   值4： receivers
        res = send_mail('关于中秋节放假通知',
                        '中秋节放三天假',
                        '15129903773@163.com',
                        ['15129903773@163.com', '1094563328@qq.com'])
        if res:
            return HttpResponse('邮件发送成功')
        else:
            return HttpResponse('邮件发送失败')
    else:
        return render(request, 'index.html')


# 发送html
def send_html(request):
    html_message = '<a href="http://www.baidu.com">百度</a>'
    res = EmailMultiAlternatives('邮件title',
                                 '邮件内容，请点击下面的链接:' + html_message,
                                 '15129903773@163.com',
                                 ['875634410@163.com', '1094563328@qq.com'])
    res.content_subtype = 'html'
    result = res.send()
    return HttpResponse(result)


#多人多条发送
def send_mass_email(request):
    message1 = ('title',
                'message',
                '15129903773@163.com',
                ['1094563328@qq.com', '875634410@qq.com'])

    message2 = ('title',
                'message',
                '15129903773@163.com',
                ['875634410@qq.com', '1094563328@qq.com'])
    res = send_mass_mail((message1, message2))
    if res:
        return HttpResponse('多封邮件发送成功')
    else:
        return HttpResponse('多封邮件发送失败')
```



