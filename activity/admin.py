from django.contrib import admin

# Register your models here.

from .models import ActiveModel,NavlistModel,TemplateModel

class ActiveAdmin(admin.ModelAdmin):
    list_display = ('activeName','pictureUrl','linkUrl')


class NavListAdmin(admin.ModelAdmin):
    list_display = ('navName','navPictureUrl','navLinkUrL')

class TemplateAdmin(admin.ModelAdmin):
    list_display = ('templateName','templateHtml')

admin.site.register(ActiveModel,ActiveAdmin)
admin.site.register(NavlistModel,NavListAdmin)
admin.site.register(TemplateModel,TemplateAdmin)
