import json

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework import status
from django.views import View
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from api.coupon import CouponSerializer
from .models import CategoryModel, CouponModel
from api.category import CategorySerializer


class FirstCategoryView(View):
    def get(self, request):
        category_all = CategoryModel.objects.all().filter(grade=1)
        ser = CategorySerializer(category_all, many=True)
        return JsonResponse({'data': ser.data})

class SecondCategoryView(View):
    def get(self, request,fk):

        category_all = CategoryModel.objects.filter(parent_id=fk).all()
        ser = CategorySerializer(category_all, many=True)

        # print(ser.data,type(ser.data))
        return JsonResponse({'data': ser.data})


class CouponView(View):
    def get(self,request,userid):
        coupon_all=request.GET.get(userid,None)
        # coupon_all=CouponModel.objects.filter(userId=userid).all()
        s=CouponSerializer(coupon_all,many=True)
        return JsonResponse({"data":s.data})

@csrf_exempt
def product_category_list(request):
    data1=CategoryModel.objects.filter(grade=1).all()
    s = CategorySerializer(data1, many=True)


    return render(request, 'category/category_list.html', {"data":s.data})





