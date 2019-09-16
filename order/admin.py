from django.contrib import admin

# Register your models here.
from order.models import CityModel, AreaModel, OrderModel, Area_commodityModel


class CityAdmin(admin.ModelAdmin):
    list_display = ('cityName','firstChar')

class AreaAdmin(admin.ModelAdmin):
    list_display = ('AreaName','city')

class AreaCommoAdmin(admin.ModelAdmin):
    list_display = ('area_id','commodity_id','cityname','commodityname')
    list_filter = ('area_id',)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('title',  'total', 'pay_type','status', 'receiver','receiver_phone', 'receiver_address' )

class AddressAdmin(admin.ModelAdmin):
    list_display = ('privName',  'cityName', 'streetName','specify')



admin.site.register(CityModel,CityAdmin)
admin.site.register(AreaModel,AreaAdmin)
admin.site.register(OrderModel,OrderAdmin)
admin.site.register(Area_commodityModel,AreaCommoAdmin)
