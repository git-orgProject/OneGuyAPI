from django.contrib import admin

from .models import UserModel
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id','phone' ,'user_name', 'sex' ,'password')
    list_per_page = 2


admin.site.register(UserModel,UserAdmin)