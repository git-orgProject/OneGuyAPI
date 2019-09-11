from rest_framework.response import Response
from rest_framework.views import APIView
from api.commodity import CommodityModelSerializer
from .models import CommodityModel

class CommodityView_p(APIView):
    def get(self,request):
        datas = CommodityModel.objects.all()[:20]
        serializer = CommodityModelSerializer(datas, many=True) #序列化类
        return Response({
            'page': 1,
            'pageSize':20,
            'data': serializer.data
        })

class CommodityView_f(APIView):
    def get(self,request):
        datas = CommodityModel.objects.all()[:20]
        serializer = CommodityModelSerializer(datas, many=True) #序列化类
        return Response({
            'page': 1,
            'pageSize':20,
            'data': serializer.data
        })
