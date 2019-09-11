from rest_framework import serializers

from activity.models import NavlistModel
from order.models import CityModel, AreaModel


class AreaModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AreaModel
        fields=('id','AreaName','city_id')

class CityModelSerializer(serializers.HyperlinkedModelSerializer):
    area = AreaModelSerializer(many=True)
    class Meta:
        model = CityModel
        fields=('id','cityName','firstChar','area')

class navModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NavlistModel
        fields=('id','navName','navPictureUrl','navLinkUrl')

