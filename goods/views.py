from rest_framework.response import Response
from rest_framework.views import APIView
from api.commodity import CommodityModelSerializer
from .models import CommodityModel

class CommodityViewALL(APIView):  #所有商品信息
    def get(self,request):
        datas = CommodityModel.objects.all()
        serializer = CommodityModelSerializer(datas, many=True) #序列化类
        return Response(serializer.data)


class CommodityViewPK(APIView):   #通过商品id来获取商品信息
    def get(self,request,id):
        datas = CommodityModel.objects.filter(pk=id).all()
        serializer = CommodityModelSerializer(datas, many=True) #序列化类
        return Response(serializer.data)

class CommodityModelViewFK(APIView):  #通过商品类型获取商品信息
    def get(self,request,categoryId):
        datas = CommodityModel.objects.filter(categoryId_id=categoryId)
        serializer = CommodityModelSerializer(datas, many=True) #序列化类
        return Response(serializer.data)
