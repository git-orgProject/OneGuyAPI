# Generated by Django 2.0.1 on 2019-09-10 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0003_auto_20190910_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activemodel',
            name='linkUrl',
            field=models.CharField(max_length=100, verbose_name='链接地址'),
        ),
        migrations.AlterField(
            model_name='activemodel',
            name='pictureUrl',
            field=models.CharField(max_length=100, verbose_name='图片地址'),
        ),
        migrations.AlterField(
            model_name='navlistmodel',
            name='navLinkUrl',
            field=models.CharField(max_length=100, verbose_name='链接地址'),
        ),
        migrations.AlterField(
            model_name='navlistmodel',
            name='navPictureUrl',
            field=models.CharField(max_length=100, verbose_name='图片地址'),
        ),
    ]
