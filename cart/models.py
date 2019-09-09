from django.db import models
from user.models import UserModel
from goods.models import Commodity
# Create your models here.
class CartModel(models.Model):
    user_id = models.OneToOneField(UserModel,
                                   verbose_name='用户ID',
                                   on_delete=models.CASCADE)

    class Meta:
        db_table = 't_cart'
        verbose_name = '购物车'


class CommondityCart(models.Model):
    cart = models.ForeignKey(CartModel,
                             on_delete=models.CASCADE,
                             verbose_name='购物车')

    commondity = models.ForeignKey(CommondityModel,
                                   on_delete=models.CASCADE,
                                   verbose_name='商品ID')
    count = models.IntegerField(verbose_name='商品数量',
                                default=1)

    class Meta:
        db_table = 't_goods_cart'
        verbose_name_plural = verbose_name = '购物车详情表'