from django.contrib import admin
from .models import CategoryEntity,Commodity


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code',  'grade','parent_id')
    fields = ('name', 'code',  'parent', 'grade')
    search_fields = ('code', 'name')

admin.site.register(CategoryEntity, CategoryAdmin)

class CommodityAdmin(admin.ModelAdmin):
    list_display = ('categoryId','commodityName','state','sellPrice',
                    'maxCommodityCount','sales','spec','field','iframepage',
                    'smallPicture','showPicture','subTitle','canAddCart','canNoReasonToReturnText','deliveryTips')
    fields = ('categoryId','commodityName','state','sellPrice',
                    'maxCommodityCount','sales','spec','field','iframepage',
                    'smallPicture','showPicture','subTitle','canAddCart')
    search_fields = ('commodityName')
admin.site.register(Commodity, CommodityAdmin)