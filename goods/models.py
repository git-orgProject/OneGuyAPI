from django.db import models

from common import YGBaseModel
from user.models import UserModel


class CategoryModel(YGBaseModel):
    code = models.CharField(max_length=20,
                            verbose_name='编码')
    name = models.CharField(max_length=20,
                            verbose_name='名称')

    grade = models.IntegerField(default=1,
                                verbose_name='等级')

    parent = models.ForeignKey('self',
                               on_delete=models.CASCADE,
                               verbose_name='父类',
                               null=True,
                               blank=True)

    picture_url = models.CharField(max_length=200,
                                   verbose_name='图片路径',
                                   blank=True,
                                   null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 't_category'
        verbose_name = verbose_name_plural = '分类表'


class CommodityModel(YGBaseModel):  # 要继承YGBaseModel
    __commodityTuple__ = ((0, "无货"), (1, "有货"))
    categoryId = models.ForeignKey(CategoryModel,
                                   on_delete=models.SET_NULL, blank=True, null=True, verbose_name="分类id")
    commodityName = models.CharField(max_length=200, verbose_name="商品名称")
    state = models.IntegerField(choices=__commodityTuple__, verbose_name="商品状态", default=1)
    sellPrice = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="销售价格")
    maxCommodityCount = models.IntegerField(null=True, blank=True, verbose_name="库存")
    sales = models.IntegerField(null=True, blank=True, verbose_name="销量")
    spec = models.CharField(max_length=50, verbose_name="商品规格")
    field = models.CharField(max_length=100, verbose_name="产地",null=True, blank=True,)
    iframePage = models.CharField(max_length=400, null=True, blank=True, verbose_name="图文详情")
    smallPicture = models.CharField(max_length=400, verbose_name="商品小图")
    showPicture = models.CharField(max_length=400, verbose_name="商品展示图片")
    subTitle = models.CharField(max_length=200, null=True, blank=True, verbose_name="商品二级标题")
    canAddCart = models.BooleanField(default=True,verbose_name="能否加入购物车")
    canNoReasonToReturnText = models.CharField(max_length=100, default="不支持7天无理由退货",null=True, blank=True,)
    deliveryTips = models.CharField(max_length=100, default=" 16:00 前完成订单，预计明日送达",null=True, blank=True,)

    def __str__(self):
        return self.commodityName

    class Meta:
        db_table = "t_commodity"
        verbose_name_plural = verbose_name = "商品信息表"

class CouponModel(models.Model):
    couponCode=models.CharField(primary_key=True,
                                max_length=20,
                                verbose_name='优惠券号')
    user=models.ForeignKey(UserModel,
                             verbose_name='用户id',
                             on_delete=models.SET_NULL,
                             blank=True,
                             null=True,
                             )

    couponName=models.CharField(max_length=50,
                                verbose_name='优惠券名称')
    couponMoney=models.DecimalField(max_digits=10,
                                    decimal_places=2,
                                    verbose_name='优惠金额或折扣')
    couponType=models.IntegerField(verbose_name='优惠券类型')
    LimitPrice=models.DecimalField(max_digits=10,
                                    decimal_places=2,
                                    verbose_name='优惠的价格上限/门槛')
    giveoutTime=models.DateTimeField(verbose_name="发放时间")
    validTime=models.DateTimeField(verbose_name='有效时间')

    def __str__(self):
        return self.couponName

    class Meta:
        db_table = "t_coupon"
        verbose_name_plural = verbose_name = "优惠券类型"