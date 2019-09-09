from django.contrib.auth.hashers import make_password
from django.db import models

class UserModel(models.Model):
    user_id = models.IntegerField(max_length=20,
                                  verbose_name='用户ID')

    phone = models.IntegerField(max_length=11,
                                verbose_name='手机号码',
                                blank=True,
                                null=True,)

    user_name = models.CharField(max_length=20,
                                 verbose_name='昵称')

    sex = models.CharField(max_length=5,
                           choices=(('male','男'),('female','女')),
                           default='male',verbose_name='性别')


    password = models.CharField(max_length=20,
                                verbose_name='密码',
                                blank=True,
                                null=True)

    def save(self,force_insert=False,force_update=False,using=None,update_field=None):
        if len(self.password)<10:
            #明文转密文
            self.password = make_password(self.password)

        super().save()

    def __str__(self):
        return self.user_name

    class Meta:
        db_table = 't_user'
        verbose_name_plural = verbose_name = '客户管理'



