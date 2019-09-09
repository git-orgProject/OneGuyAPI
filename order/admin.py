from django.contrib import admin

# Register your models here.
from order.models import CityModel, AreaModel


class CityAdmin(admin.ModelAdmin):
    list_display = ('cityName','firstChar')

class AreaAdmin(admin.ModelAdmin):
    list_display = ('AreaName','city')



admin.site.register(CityModel,CityAdmin)
admin.site.register(AreaModel,AreaAdmin)
