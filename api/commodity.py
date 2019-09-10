from rest_framework import serializers, viewsets
from goods.models import CommodityModel
from .category import CategorySerializer

# 序列化类
class CommodityModelSerializer(serializers.HyperlinkedModelSerializer):
    categoryId = CategorySerializer
    class Meta:
        model = CommodityModel
        fields = ('id','categoryId','commodityName', 'state','sellPrice',
                  'maxCommodityCount','spec','smallPicture','showPicture',
                  'subTitle','canAddCart','canNoReasonToReturnText','deliveryTips')


# API视图类
class CommodityAPIView(viewsets.ModelViewSet):
    queryset = CommodityModel.objects.all() #查询结果集
    serializer_class = CommodityModelSerializer #序列化类