import random

from PIL import Image, ImageDraw, ImageFont
from django.http import HttpResponse
from django.shortcuts import render,redirect

from common.code import new_code_str
from . import models
from . import forms
import hashlib

def hash_code(s,salt='user'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  #update方法只接收bytes类型
    return h.hexdigest()

def index(request):
    if not request.session.get('is_login',None):
        return redirect('/user/login/')
    return render(request,'login/index.html')

def login(request):
    if request.session.get('is_login',None):    #不允许重复登录
        return redirect('/user/index')
    if request.method == 'POST':
        login_form = forms.UserForm(request.POST)
        message = "请检查填写的内容!"
        if login_form.is_valid():

            username = login_form.cleaned_data.get('user_name')
            password = login_form.cleaned_data.get('password')
            try:
                user = models.UserModel.objects.filter(user_name=username).first()
            except Exception as e:
                print(e)
                message = '用户不存在!'
                return render(request, 'login/login.html', locals())
            if user.password == password:
                request.session['is_login'] = True   #写入用户状态和数据
                request.session['user_id'] = user.id
                request.session['user_name'] = user.user_name
                return redirect('/user/index/')
            else:
                message = '密码不正确!'
                return render(request, 'login/login.html', locals())
        else:
            return render(request, 'login/login.html',locals())

    login_form = forms.UserForm()
    return render(request, 'login/login.html',locals())

def register(request):
    if request.session.get('is_login', None):
        return redirect('/user/index/')

    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            sex = register_form.cleaned_data.get('sex')

            if password1 != password2:
                message = '两次输入的密码不同！'
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = models.UserModel.objects.filter(name=username)
                if same_name_user:
                    message = '用户名已经存在'
                    return render(request, 'login/register.html', locals())


                new_user = models.UserModel()
                new_user.user_name = username
                new_user.password = hash_code(password1)
                new_user.sex = sex
                new_user.save()

                return redirect('/user/login/')
        else:
            return render(request, 'login/register.html', locals())
    register_form = forms.RegisterForm()
    return render(request, 'login/register.html', locals())

def logout(request):
    if not request.session.get('is_login',None):
        #如果本来就未登录，也就没有登出一说
        return redirect("/user/login")
    request.session.flush()

    return redirect("/user/login/")

def new_img_code(request):

    # 创建画布
    img = Image.new('RGB', (120, 40), (100, 100, 0))

    # 从画布中获取画笔
    draw = ImageDraw.Draw(img, 'RGB')

    # 创建字体对象和字体颜色
    font_color = (0, 20, 100)
    font = ImageFont.truetype(font='static/fonts/buding.ttf',
                              size=30)

    valid_code = new_code_str(6)
    request.session['code'] = valid_code
    print(valid_code)
    # 开始画内容
    draw.text((5, 5), valid_code, font=font, fill=font_color)

    for _ in range(500):
        x = random.randint(0, 120)
        y = random.randint(0, 40)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        draw.point((x, y), (r, g, b))

    # 将画布写入内存字节数组中
    from io import BytesIO
    buffer = BytesIO()
    img.save(buffer, 'png')  # 写入

    return HttpResponse(content=buffer.getvalue(),
                        content_type='image/png')


