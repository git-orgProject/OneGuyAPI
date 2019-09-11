from django.http import JsonResponse
from rest_framework.views import APIView
from .models import UserModel


def login(self,request):
    user_name = request.data.get('username',None)
    password = request.data.get('password',None)

    if not all((user_name,password)):
        return JsonResponse({
            'code':100,
            'mag':'用户名或口令不能为空'
        })


