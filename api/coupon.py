
from rest_framework import serializers, viewsets
from goods.models import CouponModel



class CouponSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CouponModel
        fields = ("couponCode", "userId",
                    "couponName", "couponMoney", "couponType", "LimitPrice", "giveoutTime", "validTime")


class CouponAPIView(viewsets.ModelViewSet):
    queryset = CouponModel.objects.all()
    serializer_class = CouponSerializer
