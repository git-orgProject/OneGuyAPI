from order.models import OrderModel
from rest_framework import serializers,viewsets

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderModel
        fields = ('title','create_time','status')

class OrderAPIView(viewsets.ModelViewSet):
    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializer
