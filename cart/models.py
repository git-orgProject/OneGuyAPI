from django.db import models

from common import YGBaseModel
from user.models import UserModel
from goods.models import CommodityModel


# Create your models here.


class CartModel(YGBaseModel):
    user_id = models.OneToOneField(UserModel,
                                   verbose_name='用户ID',
                                   on_delete=models.CASCADE)
    user_state = models.IntegerField(verbose_name="用户状态",
                                  choices=((0, '离线'), (1, '在线')))


    class Meta:
        db_table = 't_cart'
        verbose_name_plural = verbose_name = '购物车'


class CommodityCart(YGBaseModel):
    cart = models.ForeignKey(CartModel,
                             on_delete=models.CASCADE,
                             verbose_name='购物车ID')

    commondity = models.ForeignKey(CommodityModel,
                                   on_delete=models.CASCADE,
                                   verbose_name='商品ID')
    count = models.IntegerField(verbose_name='商品数量',
                                default=1)

    class Meta:
        db_table = 't_goods_cart'
        verbose_name_plural = verbose_name = '购物车详情表'
