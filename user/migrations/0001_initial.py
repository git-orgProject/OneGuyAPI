# Generated by Django 2.0.1 on 2019-09-09 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(max_length=20, verbose_name='用户ID')),
                ('phone', models.IntegerField(blank=True, max_length=11, null=True, verbose_name='手机号码')),
                ('user_name', models.CharField(max_length=20, verbose_name='昵称')),
                ('sex', models.CharField(choices=[('male', '男'), ('female', '女')], default='male', max_length=5, verbose_name='性别')),
                ('password', models.CharField(blank=True, max_length=20, null=True, verbose_name='密码')),
            ],
            options={
                'verbose_name': '客户管理',
                'verbose_name_plural': '客户管理',
                'db_table': 't_user',
            },
        ),
    ]
