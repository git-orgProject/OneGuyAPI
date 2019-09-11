from rest_framework import serializers
from goods.models import CommodityModel
from .category import CategorySerializer

# 序列化类
class CommodityModelSerializer(serializers.HyperlinkedModelSerializer):
    categoryId = CategorySerializer(many=False) #一端数据many为False
    class Meta:
        model = CommodityModel
        fields = ('id','categoryId','commodityName', 'state','sellPrice',
                  'maxCommodityCount','spec','smallPicture','showPicture',
                  'subTitle','canAddCart','canNoReasonToReturnText','deliveryTips')

