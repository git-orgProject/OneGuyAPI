from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from order.models import CityModel
from api.active import CityModelSerializer


class CityView(APIView):
    def get(self,request):
        datas = CityModel.objects.all()
        serializer = CityModelSerializer(datas,many=True)
        return Response(serializer.data)


