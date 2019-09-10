# Generated by Django 2.0.1 on 2019-09-09 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartModel',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.UserModel', verbose_name='用户ID')),
            ],
            options={
                'verbose_name': '购物车',
                'db_table': 't_cart',
            },
        ),
        migrations.CreateModel(
            name='CommodityCart',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=1, verbose_name='商品数量')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.CartModel', verbose_name='购物车ID')),
                ('commondity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.CommodityModel', verbose_name='商品ID')),
            ],
            options={
                'verbose_name': '购物车详情表',
                'verbose_name_plural': '购物车详情表',
                'db_table': 't_goods_cart',
            },
        ),
    ]