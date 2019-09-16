from django.contrib import admin
from .models import CategoryModel, CommodityModel, CouponModel


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'picture_url', 'grade', 'parent_id')
    fields = ('name', 'code', 'picture_url', 'parent', 'grade')
    search_fields = ('code', 'name')
    list_per_page = 10


admin.site.register(CategoryModel, CategoryAdmin)


class CouponModelAdmin(admin.ModelAdmin):
    list_display = ("couponCode", "user_id",
                    "couponName", "couponMoney", "couponType", "LimitPrice", "giveoutTime", "validTime")
    fields = ("couponCode","user_id","couponName","couponMoney","couponType","LimitPrice","giveoutTime","validTime")
    list_per_page = 10
    search_fields = ("couponCode",)


admin.site.register(CouponModel, CouponModelAdmin)


class CommodityAdmin(admin.ModelAdmin):
    list_display = ('id', 'categoryId', 'commodityName', 'state', 'sellPrice',
                    'maxCommodityCount', 'sales', 'spec', 'field', 'iframePage',
                    'smallPicture', 'showPicture', 'subTitle', 'canAddCart')
    fields = ('categoryId', 'commodityName', 'state', 'sellPrice',
              'maxCommodityCount', 'sales', 'spec', 'field', 'iframePage',
              'smallPicture', 'showPicture', 'subTitle', 'canAddCart', 'canNoReasonToReturnText', 'deliveryTips')
    search_fields = ('commodityName',)
    list_per_page = 20


admin.site.register(CommodityModel, CommodityAdmin)
