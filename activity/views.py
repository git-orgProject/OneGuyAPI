from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from activity.models import NavlistModel
from order.models import CityModel, AreaModel
from api.active import CityModelSerializer, navModelSerializer, AreaModelSerializer


class CityView(APIView):
    def get(self,request):
        datas = CityModel.objects.all()
        serializer = CityModelSerializer(datas,many=True)
        return Response(serializer.data)

class NavlistView(APIView):
    def get(self,request):
        datas = NavlistModel.objects.all()
        serializer=navModelSerializer(datas,many=True)
        return Response(serializer.data)

class AreaModelView(APIView):
    def get(self,request):
        citys = CityModel.objects.filter(cityName='西安').first()
        datas = AreaModel.objects.filter(city_id=citys.id).all()
        serializer=AreaModelSerializer(datas,many=True)
        return Response(serializer.data)


