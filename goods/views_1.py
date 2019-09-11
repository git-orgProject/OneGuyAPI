import json

from django.http import JsonResponse
from rest_framework import status
from django.views import View
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CategoryModel
from api.category import CategorySerializer


class FirstCategoryView(View):
    def get(self, request):
        first_category = CategoryModel.objects.all().filter(grade=1)
        # print(first_category)
        second_category = CategoryModel.objects.all().filter(grade=2)



        l=[]
        s=[]
        data = {}
        Child = {}
        for i in first_category:
            print(i.id)
            data = {
                "id": i.id,
                "code": i.code,
                "name": i.name,
                "grade": i.grade,
                "picture_url": i.picture_url,
                "parent_id": i.parent_id,

            }

            l.append(data)
         # print(l)
        for j in second_category:



            Child = {
                        "id": j.id,
                        "code": j.code,
                        "name": j.name,
                        "grade": j.grade,
                        "picture_url": j.picture_url,
                        "parent_id": j.parent_id,
                    },
            s.append(Child)
        # print(s)
        for ii in l:
            # print(ii)
            for jj in s:
                if ii ==  jj:
                    pass






        # print(data)
        # s = CategorySerializer(data, many=True)

        return JsonResponse({'data': data})


# class FirstCategoryView(View):
#     def get(self, request):
#         category_all = CategoryModel.objects.all().filter(grade=1)
#         ser = CategorySerializer(category_all, many=True)
#
#         # print(ser.data,type(ser.data))
#
#         return JsonResponse({'data': ser.data})

