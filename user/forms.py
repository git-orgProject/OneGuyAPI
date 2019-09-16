from django import forms
from captcha.fields import CaptchaField

class UserForm(forms.Form):
    user_name = forms.CharField(max_length=128,
                                widget=forms.TextInput(attrs={'class':'form-control','placeholder':"请输入您的用户名",'autofocus':''}))
    password = forms.CharField(max_length=256,
                               widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':"请输入您的密码"}))
    # captcha = CaptchaField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':"请输入验证码"}))


class RegisterForm(forms.Form):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    username = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':"请输入您的用户名"}))
    password1 = forms.CharField( max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':"请输入您的密码"}))
    password2 = forms.CharField(max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':"请再次输入您的密码"}))
    sex = forms.ChoiceField(label='性别', choices=gender)


