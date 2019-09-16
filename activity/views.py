from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from activity.models import NavlistModel, ActiveModel
from order.models import CityModel, AreaModel, AddressModel
from api.active import CityModelSerializer, navModelSerializer, AreaModelSerializer, ActiveModelSerializer, \
    AreaCommodModelSerializer, AddressModelSerializer


class CityView(APIView):
    def get(self,request):
        char = list(map(chr, range(ord('A'), ord('Z') + 1)))
        data1={}
        for ch in char:
            data1[ch]=CityModelSerializer(CityModel.objects.filter(firstChar=ch),many=True).data

        data1['hotcity']=CityModelSerializer(CityModel.objects.filter(hotcity=1),many=True).data

        return Response({
            'data':data1,
            'code':200
                         })

class NavlistView(APIView):
    def get(self,request):
        datas = NavlistModel.objects.all()
        serializer=navModelSerializer(datas,many=True)
        return Response({
            'data':serializer.data,
            'code':200
        })

class AreaModelView(APIView):

    def get(self,request):
        cid=request.GET.get('id')
        datas = AreaModel.objects.filter(city_id=cid).all()
        serializer=AreaModelSerializer(datas,many=True)
        return Response({
            'data':serializer.data,
            'code':200})

class AddressModelView(APIView):
    def get(self,request):
        cid=request.GET.get('id')
        datas = AddressModel.objects.get(pk=cid)
        serializer=AddressModelSerializer(datas)
        return JsonResponse({
            'data':serializer.data,
            'code':200})
    def post(self,request):
        serializer = AddressModelSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                'data':serializer.instance,
                'code':200
            })
        else:
            return JsonResponse({'data':serializer.errors,
                             'code':400
                            })


class AreaCommodModelView(APIView):

    def get(self,request):
        cid=request.GET.get('id')
        datas = AreaModel.objects.get(pk=cid).area.all()
        serializer=AreaCommodModelSerializer(datas,many=True)
        return Response({
            'data':serializer.data})

class ActiveModelView(APIView):
    def get(self,request):
        datas = ActiveModel.objects.all()
        serializer=ActiveModelSerializer(datas,many=True)
        return Response({
            'data':serializer.data,
            'code':200
        })




