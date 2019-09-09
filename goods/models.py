from django.db import models

# Create your models here.
from common import YGBaseModel

class CategoryEntity(YGBaseModel):
    code=models.CharField(max_length=20,
                          verbose_name='编码')
    name=models.CharField(max_length=20,
                          verbose_name='名称')
    grade=models.IntegerField(default=1,
                              verbose_name='等级')
    parent=models.ForeignKey('self',
                             on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 't_category'
        verbose_name = verbose_name_plural = '分类表'
