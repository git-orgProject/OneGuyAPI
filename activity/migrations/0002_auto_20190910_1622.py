# Generated by Django 2.0.1 on 2019-09-10 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activemodel',
            name='id',
            field=models.CharField(auto_created=True, default='e44efa4afadb4682893b5b411abf6d5c', max_length=50, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='navlistmodel',
            name='id',
            field=models.CharField(auto_created=True, default='e44efa4afadb4682893b5b411abf6d5c', max_length=50, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='templatemodel',
            name='id',
            field=models.CharField(auto_created=True, default='e44efa4afadb4682893b5b411abf6d5c', max_length=50, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]