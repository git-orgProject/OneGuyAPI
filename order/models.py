from django.db import models
from common import YGBaseModel

# Create your models here.

class CityModel(YGBaseModel):
    cityName = models.CharField(max_length=20,verbose_name='城市名')
    firstChar = models.CharField(max_length=2,verbose_name='首字母')
    def __str__(self):
        return self.cityName
    class Meta:
        db_table = 't_city'
        verbose_name_plural = verbose_name = '城市'

class AreaModel(YGBaseModel):
    AreaName = models.CharField(max_length=20,verbose_name='地区名')
    city = models.ForeignKey(CityModel,related_name='area',
                             on_delete=models.CASCADE)

    def __str__(self):
        return self.AreaName
    class Meta:
        db_table = 't_area'
        verbose_name_plural = verbose_name = '地区'







