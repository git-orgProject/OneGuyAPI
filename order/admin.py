from django.contrib import admin

# Register your models here.
from order.models import CityModel, AreaModel,OrderModel


class CityAdmin(admin.ModelAdmin):
    list_display = ('cityName','firstChar')

class AreaAdmin(admin.ModelAdmin):
    list_display = ('AreaName','city')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('title',  'total', 'pay_type','status', 'receiver','receiver_phone', 'receiver_address' )



admin.site.register(CityModel,CityAdmin)
admin.site.register(AreaModel,AreaAdmin)
admin.site.register(OrderModel,OrderAdmin)
