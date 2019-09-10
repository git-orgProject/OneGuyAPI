from django.db import models

# Create your models here.
from common import YGBaseModel




class CategoryModel(YGBaseModel):
    code=models.UUIDField(max_length=20,
                          verbose_name='编码')
    name=models.CharField(max_length=20,
                          verbose_name='名称')
    grade=models.IntegerField(default=1,
                              verbose_name='等级')
    parent=models.ForeignKey('self',
                             on_delete=models.CASCADE,
                             verbose_name='父类',
                             null=True,
                             blank=True)

    picture_url = models.CharField(max_length=200,
                                   verbose_name='图片路径',
                                   blank=True,
                                   null=True)


    def __str__(self):
        return self.id

    class Meta:
        db_table = 't_category'
        verbose_name = verbose_name_plural = '分类表'


class CommodityModel(YGBaseModel):  # 要继承
    __commodityTuple__ = ((0, "无货"), (1, "有货"))
    categoryId = models.ForeignKey(CategoryModel, on_delete="SET_NULL", blank=True, null=True, verbose_name="分类id")
    commodityName = models.CharField(max_length=200, verbose_name="商品名称")
    state = models.IntegerField(choices=__commodityTuple__, verbose_name="商品状态")
    sellPrice = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="销售价格")
    maxCommodityCount = models.IntegerField(null=True, blank=True, verbose_name="库存")
    sales = models.IntegerField(null=True, blank=True, verbose_name="销量")
    spec = models.CharField(max_length=50, verbose_name="商品规格")
    field = models.CharField(max_length=100, verbose_name="产地")
    iframepage = models.CharField(max_length=400, null=True, blank=True, verbose_name="图文详情")
    smallPicture = models.CharField(max_length=400, verbose_name="商品小图")
    showPicture = models.CharField(max_length=400, verbose_name="商品展示图片")
    subTitle = models.CharField(max_length=200, null=True, blank=True, verbose_name="商品二级标题")
    canAddCart = models.BooleanField(verbose_name="能否加入购物车")
    canNoReasonToReturnText = models.CharField(max_length=100, default="不支持7天无理由退货",null=True, blank=True,)
    deliveryTips = models.CharField(max_length=100, default=" 16:00 前完成订单，预计明日送达",null=True, blank=True,)

    def __str__(self):
        return self.commodityName

    class Meta:
        db_table = "t_commodity"
        verbose_name_plural = verbose_name = "商品信息表"
