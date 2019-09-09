from django.contrib import admin
from .models import CategoryEntity


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code',  'grade','parent_id')
    fields = ('name', 'code',  'parent', 'grade')
    search_fields = ('code', 'name')

admin.site.register(CategoryEntity, CategoryAdmin)