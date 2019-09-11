from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from activity.models import NavlistModel, ActiveModel
from order.models import CityModel, AreaModel
from api.active import CityModelSerializer, navModelSerializer, AreaModelSerializer, ActiveModelSerializer


class CityView(APIView):
    def get(self,request):
        char = list(map(chr, range(ord('A'), ord('Z') + 1)))
        data1={}
        for ch in char:
            data1[ch]=CityModelSerializer(CityModel.objects.filter(firstChar=ch),many=True).data

        data1['hotcity']=CityModelSerializer(CityModel.objects.filter(hotcity=1),many=True).data

        return Response({'data':data1})

class NavlistView(APIView):
    def get(self,request):
        datas = NavlistModel.objects.all()
        serializer=navModelSerializer(datas,many=True)
        return Response(serializer.data)

class AreaModelView(APIView):

    def get(self,request):
        cid=request.GET.get('id')
        datas = AreaModel.objects.filter(city_id=cid).all()
        serializer=AreaModelSerializer(datas,many=True)
        return Response({
            'data':serializer.data})

class ActiveModelView(APIView):
    def get(self,request):
        datas = ActiveModel.objects.all()
        serializer=ActiveModelSerializer(datas,many=True)
        return Response(serializer.data)


