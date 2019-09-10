from django.shortcuts import render
from django.http import HttpResponse
# 引入发送邮件的模块
from django.core.mail import send_mail, send_mass_mail, EmailMultiAlternatives


def sendEmail(request):
    return render(request, 'index.html')


def send_email(request):
    if request.method == 'POST':
        # 值1： title    值2： message
        # 值3： sender   值4： receiver
        res = send_mail('关于中秋节放假通知',
                        '中秋节放三天假',
                        '15129903773@163.com',
                        ['15129903773@163.com'])
        if res:
            return HttpResponse('邮件发送成功')
        else:
            return HttpResponse('邮件发送失败')
    else:
        return render(request, 'index.html')


def send_html(request):
    html_message = '<a href="http://www.baidu.com">百度</a>'
    res = EmailMultiAlternatives('关于对点击事件的安排',
                                 '请点击下面的链接:' + html_message,
                                 '15129903773@163.com',
                                 ['875634410@163.com', '1094563328@qq.com'])
    res.content_subtype = 'html'
    result = res.send()
    return HttpResponse(result)


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
