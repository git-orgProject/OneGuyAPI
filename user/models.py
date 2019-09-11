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
                           choices=(('male','男'),('femal','女')),
                           default='male',verbose_name='性别')


    password = models.CharField(max_length=20,
                                verbose_name='密码',
                                blank=True,
                                null=True)



    def __str__(self):
        return self.user_name

    class Meta:
        db_table = 't_user'
        verbose_name_plural = verbose_name = '客户管理'


