from django.db import models
from django.db.models import Q

from common import YGBaseModel

# Create your models here.
from goods.models import CommodityModel


class CityModel(YGBaseModel):
    cityName = models.CharField(max_length=20,
                                verbose_name='城市名')
    firstChar = models.CharField(max_length=2,
                                 verbose_name='首字母')
    hotcity = models.IntegerField(choices=((0,'否'),(1,'是')),
                                  verbose_name='热门城市',
                                  null=True,blank=True,default=0)
    def __str__(self):
        return self.cityName
    class Meta:
        db_table = 't_city'
        verbose_name_plural = verbose_name = '城市'

class AreaModel(YGBaseModel):
    AreaName = models.CharField(max_length=20,verbose_name='地区名')
    city = models.ForeignKey(CityModel,related_name='area',
                             on_delete=models.CASCADE)

    def __str__(self):
        return self.AreaName
    class Meta:
        db_table = 't_area'
        verbose_name_plural = verbose_name = '地区'

class Area_commodityModel(YGBaseModel):
    area = models.ForeignKey(AreaModel,verbose_name='地区',related_name='area',on_delete=models.SET_NULL,
                             null=True,blank=True)
    commodity = models.ForeignKey(CommodityModel,verbose_name='商品',related_name='commodity',on_delete=models.SET_NULL,
                                  null=True,blank=True)
    class Meta:
        db_table='t_area_commodity'
        verbose_name_plural=verbose_name = '地区商品'


class OrederManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(~Q(status=5))


class OrderModel(YGBaseModel):
    title = models.CharField(max_length=100,
                             verbose_name='订单名称'
                                          '')
    create_time = models.DateTimeField(verbose_name='下单时间',
                                       auto_now_add=True)

    total = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                verbose_name='订单金额')

    pay_type = models.IntegerField(choices=((0,'余额'),
                                            (1,'银行卡支付'),
                                            (2,'微信支付'),
                                            (3,'支付宝支付')),
                                   verbose_name='支付方式',
                                   default=0)

    status = models.IntegerField(choices=((0,'待支付'),
                                          (1,'已支付'),
                                          (2,'待收货'),
                                          (3,'已收货'),
                                          (4,'完成'),
                                          (5,'取消'),),
                                 verbose_name='订单状态',
                                 default=0)

    receiver = models.CharField(max_length=20,
                                verbose_name='收货人')

    receiver_phone = models.CharField(max_length=11,
                                      verbose_name='收货人手机号')

    receiver_address = models.TextField(max_length=50,
                                        verbose_name='收货地址')

    objects = OrederManager()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 't_order'
        verbose_name_plural = verbose_name = '订单表'



