from rest_framework import serializers
from order.models import CityModel

class CityModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CityModel
        fields=('id','cityName','firstChar')
