from rest_framework.response import Response
from rest_framework.views import APIView
from api.commodity import CommodityModelSerializer
from .models import CommodityModel

class CommodityViewALL(APIView):  #所有商品信息
    def get(self,request):
        datas = CommodityModel.objects.all()
        serializer = CommodityModelSerializer(datas, many=True) #序列化类
        return Response({'data': serializer.data})

class CommodityViewPK(APIView):   #通过商品id来获取商品信息
    def get(self,request):
        pid=request.GET.get('id')
        datas = CommodityModel.objects.filter(id=pid).all()
        serializer = CommodityModelSerializer(datas, many=True) #序列化类
        return Response({'data': serializer.data})

class CommodityViewFK(APIView):  #通过商品类型获取商品信息
    def get(self,request):
        fid = request.GET.get('id') #获取用户请求的参数
        datas = CommodityModel.objects.filter(categoryId_id=fid).all() #当用户请求的参数和外键的id值相等时返回所有数据
        serializer = CommodityModelSerializer(datas, many=True) #序列化类
        return Response({'data': serializer.data})
