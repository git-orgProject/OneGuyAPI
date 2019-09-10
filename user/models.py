from django.contrib.auth.hashers import make_password
from django.db import models
from django import forms

class UserModel(models.Model):
    user_id = models.CharField(max_length=20,
                                  verbose_name='用户ID',
                                  unique=True)

    phone = models.CharField(max_length=11,
                                verbose_name='手机号码',
                                blank=True,
                                null=True,
                                unique=True)

    user_name = models.CharField(max_length=20,
                                 verbose_name='昵称')

    sex = models.CharField(max_length=5,
                           choices=(('male','男'),('female','女')),
                           default='male',verbose_name='性别')


    password = models.CharField(max_length=20,
                                verbose_name='密码',
                                blank=True,
                                null=True)

    # def save(self,force_insert=False,force_update=False,using=None,update_field=None):
    #     if len(self.password)<10:
    #         #明文转密文
    #         self.password = make_password(self.password)
    #
    #     super().save()

    def __str__(self):
        return self.user_name

    class Meta:
        db_table = 't_user'
        verbose_name_plural = verbose_name = '客户管理'




class UserForm(forms.Form):
        username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
        password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

