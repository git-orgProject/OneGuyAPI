
from rest_framework import serializers, viewsets

from api import UserSerializer
from goods.models import CouponModel



class CouponSerializer(serializers.HyperlinkedModelSerializer):
    user=UserSerializer(many=False)
    class Meta:
        model = CouponModel
        fields = ("couponCode", "user",
                    "couponName", "couponMoney", "couponType", "LimitPrice", "giveoutTime", "validTime")


class CouponAPIView(viewsets.ModelViewSet):
    queryset = CouponModel.objects.all()
    serializer_class = CouponSerializer
