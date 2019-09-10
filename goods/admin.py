from django.contrib import admin
from .models import CategoryModel, CommodityModel


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'picture_url', 'grade', 'parent_id')
    fields = ('name', 'code', 'picture_url', 'parent', 'grade')
    search_fields = ('code', 'name')


admin.site.register(CategoryModel, CategoryAdmin)


class CommodityAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ('categoryId', 'commodityName', 'state', 'sellPrice',
                    'maxCommodityCount', 'sales', 'spec', 'field', 'iframepage',
                    'smallPicture', 'showPicture', 'subTitle', 'canAddCart')
    fields = ('categoryId', 'commodityName', 'state', 'sellPrice',
              'maxCommodityCount', 'sales', 'spec', 'field', 'iframepage',
              'smallPicture', 'showPicture', 'subTitle', 'canAddCart', 'canNoReasonToReturnText', 'deliveryTips')
    search_fields = ('categoryId', 'commodityName')


admin.site.register(CommodityModel, CommodityAdmin)
=======
    list_display = ('id','categoryId','commodityName','state','sellPrice',
                    'maxCommodityCount','sales','spec','field','iframePage',
                    'smallPicture','showPicture','subTitle','canAddCart')
    fields = ('categoryId','commodityName','state','sellPrice',
                    'maxCommodityCount','sales','spec','field','iframePage',
                    'smallPicture','showPicture','subTitle','canAddCart','canNoReasonToReturnText','deliveryTips')
    search_fields = ('categoryId','commodityName')
admin.site.register(CommodityModel, CommodityAdmin)
>>>>>>> a13abf785cb37e62d27c56b1627dd587b60a980e
