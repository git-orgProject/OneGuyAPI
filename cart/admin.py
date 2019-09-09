from django.contrib import admin

# Register your models here.
from cart.models import CartModel, CommodityCart


class CartModelAdmin(admin.ModelAdmin):
    list_display = ('user_id',)


class CommodityCartAdmin(admin.ModelAdmin):
    list_display = ('cart', 'commondity', 'count')


# 将模型增加到站点中
admin.site.register(CartModel, CartModelAdmin)
admin.site.register(CommodityCart, CommodityCartAdmin)
