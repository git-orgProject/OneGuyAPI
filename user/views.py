from django.http import JsonResponse, HttpResponse
from rest_framework.utils import json

from rest_framework.views import APIView

from api import UserSerializer
from .models import UserModel

class UserView(APIView):
    def login(self,request):
        user_name = request.data.get('username')
        password = request.data.get('password')

        if not all((user_name,password)):
            return JsonResponse({
                'code':100,
                'mag':'用户名或口令不能为空'
            })
        else:
            qs = UserModel.objects.filter(user_name=user_name)
            if qs.exists():
                login_user = qs.first()
                if login_user.password == password:
                    info = UserSerializer(login_user,many=False).data
                    return JsonResponse({
                        'code':200,
                        'data':{
                            'user_id':login_user.id,
                            'phone':login_user.phone
                        }
                    })
                return JsonResponse({
                    'code':102,
                    'msg':'用户名或口令不正确，请重试'
                })
            else:
                return JsonResponse({
                    'code':101,
                    'msg':'用户不存在'
                })

    def regist(self,request):
        resp1 = HttpResponse(content='您好'.encode('utf-8'),
                             status=200,
                             content_type='text/html;charset=utf-8')

        with open('images/fz.jpg', 'rb') as f:
            bytes = f.read()

        # 响应图片数据
        resp2 = HttpResponse(content=bytes)
        # ?? 响应头如何设置
        resp2['Content-Type'] = 'image/jpg'

        # 响应json数据
        data = {'name': 'fz', 'age': 20}

        resp3 = HttpResponse(content=json.dumps(data),
                             content_type='application/json')

        resp4 = JsonResponse(data)

        return resp2

    def get(self,request):
        id = request.GET.get('id',None)
        if not id:
            return JsonResponse({
                'code':100,
                'msg':'必须提供id参数'
            })
        try:
            login_user = UserModel.objects.get(pk=id)
            return JsonResponse({
                'code':200,
                'data':UserSerializer(login_user).data
            })
        except:
            return JsonResponse({
                'code':101,
                'msg':'用户不存在'
            })

    def post(self,request):

        action = request.GET.get('action')
        if action == 'login':
            return self.login(request)
        elif action == 'regist':
            return self.regist(request)
        else:
            return JsonResponse({
                'msg':'请求无效 请确定是否action参数'
            })
    def put(self, request):
        # 修改用户信息（头像、口令、激活）
        pass

    def delete(self, request):
        # 注销用户
        pass