from django.contrib import admin

# Register your models here.

from .models import ActiveModel,NavlistModel,TemplateModel

class ActiveAdmin(admin.ModelAdmin):
    list_display = ('activeName','pictureUrl','linkUrl')


class NavListAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ('navName','navPictureUrl','navLinkUrL')
=======
    list_display = ('navName','navPictureUrl','navLinkUrl')
>>>>>>> f54c20c9d9d6bbba6819de51d14826eaf9f52e3d

class TemplateAdmin(admin.ModelAdmin):
    list_display = ('templateName','templateHtml')

admin.site.register(ActiveModel,ActiveAdmin)
admin.site.register(NavlistModel,NavListAdmin)
admin.site.register(TemplateModel,TemplateAdmin)
