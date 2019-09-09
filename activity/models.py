from django.db import models
from common import YGBaseModel

# Create your models here.

class ActiveModel(YGBaseModel):
    activeName = models.CharField(max_length=50,verbose_name='活动名称')
    pictureUrl = models.CharField(max_length=50,verbose_name='图片地址')
    linkUrl = models.CharField(max_length=50,verbose_name='链接地址')
    class Meta:
        db_table='t_active'
        verbose_name_plural = verbose_name ='活动'

class NavlistModel(YGBaseModel):
    navName = models.CharField(max_length=50,verbose_name='导航名称')
    navPictureUrl = models.CharField(max_length=50,verbose_name='图片地址')
    navLinkUrl = models.CharField(max_length=50,verbose_name='链接地址')
    class Meta:
        db_table= 't_navlist'
        verbose_name_plural=verbose_name = '推荐导航'

class TemplateModel(YGBaseModel):
    templateName = models.CharField(max_length=50,verbose_name='模板名称')
    templateHtml = models.CharField(max_length=20,verbose_name='模板网页')
    class Meta:
        db_table = 't_temp'
        verbose_name_plural = verbose_name = '模板类型'

