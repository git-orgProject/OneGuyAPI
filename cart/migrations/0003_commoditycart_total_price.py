# Generated by Django 2.0.1 on 2019-09-11 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_commoditycart_is_choice'),
    ]

    operations = [
        migrations.AddField(
            model_name='commoditycart',
            name='total_price',
            field=models.FloatField(default=0.0, verbose_name='总价格'),
        ),
    ]
