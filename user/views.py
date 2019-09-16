from django.shortcuts import render,redirect
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
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')

            try:
                user = models.UserModel.objects.get(name=username)
            except:
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



