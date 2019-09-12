from rest_framework import serializers

from activity.models import NavlistModel, ActiveModel
from api.commodity import CommodityModelSerializer
from order.models import CityModel, AreaModel, Area_commodityModel


class AreaModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AreaModel
        fields=('id','AreaName','city_id')

class CityModelSerializer(serializers.HyperlinkedModelSerializer):
    area = AreaModelSerializer(many=True)
    class Meta:
        model = CityModel
        fields=('id','cityName','firstChar','area','hotcity')

class navModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NavlistModel
        fields=('id','navName','navPictureUrl','navLinkUrl')

class ActiveModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ActiveModel
        fields=('id','activeName','pictureUrl','linkUrl')

class AreaCommodModelSerializer(serializers.HyperlinkedModelSerializer):
    area = AreaModelSerializer()
    commodity= CommodityModelSerializer()
    class Meta:
        model = Area_commodityModel
        fields=('id','area','commodity')


