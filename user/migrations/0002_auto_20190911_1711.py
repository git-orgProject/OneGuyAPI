# Generated by Django 2.0.1 on 2019-09-11 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='sex',
            field=models.CharField(choices=[('male', '男'), ('femal', '女')], default='male', max_length=5, verbose_name='性别'),
        ),
    ]
