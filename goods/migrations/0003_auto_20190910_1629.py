# Generated by Django 2.0.1 on 2019-09-10 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_auto_20190910_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorymodel',
            name='id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='commoditymodel',
            name='id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
