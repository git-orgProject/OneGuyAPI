import json

from django.db.models import Q
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
    def get(self, request, fk):
        category_all = CategoryModel.objects.filter(parent_id=fk).all()
        ser = CategorySerializer(category_all, many=True)

        # print(ser.data,type(ser.data))
        return JsonResponse({'data': ser.data})



class Category_list(View):
    def get(self, request, ):
        data_1 = CategoryModel.objects.filter(grade=1).all()
        # s = CategorySerializer(data1, many=True)
        data_2 = CategoryModel.objects.filter(grade=2).all()

        l1 = []
        l2 = []
        for i in data_1:
            l1.append(
                {"id": i.id, "name": i.name, "picture_url": i.picture_url, "code": i.code, 'parent_id': i.parent_id,
                 "child": []})
        for j in data_2:
            l2.append(
                {"id": j.id, "name": j.name, "picture_url": j.picture_url, "code": j.code, 'parent_id': j.parent_id})
        for ll1 in l1:
            for ll2 in l2:
                if ll1["id"] == ll2["parent_id"]:
                    ll1["child"].append(ll2)
        return JsonResponse({"data": l1})

class CouponView(View):
    def get(self, request, userid):
        # coupon_all =CategoryModel.objects.filter(userId_id=userId).all()
        coupon_all=CouponModel.objects.filter(userId=userid).all()
        s = CouponSerializer(coupon_all, many=True)
        return JsonResponse({"data": s.data})


@csrf_exempt
def product_category_list(request):
    data1 = CategoryModel.objects.filter(grade=1).all()
    # s = CategorySerializer(data1, many=True)
    data2 = CategoryModel.objects.filter(grade=2).all()

    l1 = []
    l2 = []
    for i in data1:
        l1.append({"id": i.id, "name": i.name,"picture_url":i.picture_url,"code":i.code, 'parent_id': i.parent_id, "child": []})
    for j in data2:
        l2.append({"id": j.id, "name": j.name,"picture_url":j.picture_url,"code":j.code, 'parent_id': j.parent_id})
    for ll1 in l1:
        for ll2 in l2:
            if ll1["id"] == ll2["parent_id"]:
                ll1["child"].append(ll2)
    # print(l1)

    return render(request, 'category/category_list.html', {"data": l1})

class SearchView(View):
    def get(self,request):
        wd = request.GET.get('wd')
        info = CategoryModel.objects.all().filter(Q(name__contains=wd) | Q(code__contains=wd))

        s = CategorySerializer(info, many=True)
        if info:
            data = {

                "code": 200,
                "msg": "ok",
                "data": {
                    "datas": s.data,},
                    }

            return JsonResponse({"data": data})
        else:
            data = {'code': 404, 'msg': 'not found'}

            return JsonResponse({"data": data})

    # [{'id': '1e17a99d-ca4b-49be-908b-93c8faa20baf', 'name': '国产水果', 'parent_id': '00000000-0000-0000-0000-000000000000',
    #   'child': [{'id': '04b4701e-2f3a-49b6-98ea-b5f2bf897fc1', 'name': '李',
    #              'parent_id': '1e17a99d-ca4b-49be-908b-93c8faa20baf'},
    #             {'id': '0cd906fe-3ba4-487e-a4a6-0ade7c8c0c83', 'name': '莓',
    #              'parent_id': '1e17a99d-ca4b-49be-908b-93c8faa20baf'},
    #             {'id': '0ef106a4-7e12-46f1-9fee-581e07707120', 'name': '原箱水果',
    #              'parent_id': '1e17a99d-ca4b-49be-908b-93c8faa20baf'},
    #             {'id': '0fc21277-9f47-4479-bbee-b5c137ff3fff', 'name': '瓜',
    #              'parent_id': '1e17a99d-ca4b-49be-908b-93c8faa20baf'},
    #             {'id': '1481ba08-1ac6-4381-97de-0b986b6a85df', 'name': '芭乐',
    #              'parent_id': '1e17a99d-ca4b-49be-908b-93c8faa20baf'},
    #             {'id': '1d966c17-1345-4aaa-a551-12a9f48a8fe3', 'name': '梨',
    #              'parent_id': '1e17a99d-ca4b-49be-908b-93c8faa20baf'},
    #             {'id': '36f6e6d4-d8b7-494d-9830-1f3b9b8d27b9', 'name': '柑桔橙柚',
    #              'parent_id': '1e17a99d-ca4b-49be-908b-93c8faa20baf'},
    #             {'id': '41e196eb-f6a5-450e-a096-dcda8ae7209b', 'name': '凤梨',
    #              'parent_id': '1e17a99d-ca4b-49be-908b-93c8faa20baf'},
    #             {'id': '4ca7775f-912d-4a09-ba45-cdad1bf39221', 'name': '百香果',
    #              'parent_id': '1e17a99d-ca4b-49be-908b-93c8faa20baf'},
    #             {'id': '5dc6d26f-6766-4ffc-b32c-2d25116c4334', 'name': '枣',
    #              'parent_id': '1e17a99d-ca4b-49be-908b-93c8faa20baf'},
    #             {'id': '831cdad9-ac18-4632-a6b0-232708cdc617', 'name': '芒果',
    #              'parent_id': '1e17a99d-ca4b-49be-908b-93c8faa20baf'},
    #             {'id': 'a0ba1b75-9ea4-49a4-ad89-1a0ede082832', 'name': '时令水果',
    #              'parent_id': '1e17a99d-ca4b-49be-908b-93c8faa20baf'},
    #             {'id': 'a5828dfa-e319-4935-aa79-32129673be17', 'name': '莲雾',
    #              'parent_id': '1e17a99d-ca4b-49be-908b-93c8faa20baf'},
    #             {'id': 'afffecb2-ddba-4dbc-9da1-698fdfbcd0f8', 'name': '苹果',
    #              'parent_id': '1e17a99d-ca4b-49be-908b-93c8faa20baf'},
    #             {'id': 'b3cc10e5-11f7-4f56-a20a-1ce56054d743', 'name': '桃',
    #              'parent_id': '1e17a99d-ca4b-49be-908b-93c8faa20baf'},
    #             {'id': 'f1aa3a26-fce7-4752-baba-deb883d0e063', 'name': '葡萄',
    #              'parent_id': '1e17a99d-ca4b-49be-908b-93c8faa20baf'},
    #             {'id': 'f3bc8cc5-4774-41f2-98ad-a0139f8f7bbb', 'name': '猕猴桃',
    #              'parent_id': '1e17a99d-ca4b-49be-908b-93c8faa20baf'},
    #             {'id': 'fc2dc923-34e0-4ef8-8d2b-f04d093b614b', 'name': '热带水果',
    #              'parent_id': '1e17a99d-ca4b-49be-908b-93c8faa20baf'}]},
    #  {'id': '34c19d99-19a6-4e86-9144-18a8670cc577', 'name': '海鲜水产', 'parent_id': '00000000-0000-0000-0000-000000000000',
    #   'child': [{'id': '0b3b71c3-4969-4929-abc8-4479b72102ed', 'name': '鳕鱼',
    #              'parent_id': '34c19d99-19a6-4e86-9144-18a8670cc577'},
    #             {'id': '4b39faa9-96ab-453f-90c3-93aa7cee24c8', 'name': '鱼',
    #              'parent_id': '34c19d99-19a6-4e86-9144-18a8670cc577'},
    #             {'id': '69a9962b-0a8c-4a58-b6e8-f9a15d73da80', 'name': '大闸蟹券',
    #              'parent_id': '34c19d99-19a6-4e86-9144-18a8670cc577'},
    #             {'id': '72228b91-2f01-4ee7-9da7-4dea02c13e3c', 'name': '加工水产',
    #              'parent_id': '34c19d99-19a6-4e86-9144-18a8670cc577'},
    #             {'id': '75b795d9-b684-4676-bde4-224f44545b31', 'name': '虾',
    #              'parent_id': '34c19d99-19a6-4e86-9144-18a8670cc577'},
    #             {'id': '8496be00-ccce-4e04-870b-dbf143357ab5', 'name': '蟹',
    #              'parent_id': '34c19d99-19a6-4e86-9144-18a8670cc577'},
    #             {'id': 'ccd38218-f940-4198-b568-bcec5e9b2eeb', 'name': '虾仁',
    #              'parent_id': '34c19d99-19a6-4e86-9144-18a8670cc577'},
    #             {'id': 'd9e3b53c-344d-4a83-b298-e61008e1b1bc', 'name': '三文鱼',
    #              'parent_id': '34c19d99-19a6-4e86-9144-18a8670cc577'},
    #             {'id': 'dc40812a-911b-47b7-ad4d-85b7e2615457', 'name': '海参',
    #              'parent_id': '34c19d99-19a6-4e86-9144-18a8670cc577'},
    #             {'id': 'ded0caba-6c76-44bc-ae5e-15971cbac694', 'name': '活鲜',
    #              'parent_id': '34c19d99-19a6-4e86-9144-18a8670cc577'},
    #             {'id': 'fa496d72-50c6-4477-bdd3-6d8d71bc8e36', 'name': '贝',
    #              'parent_id': '34c19d99-19a6-4e86-9144-18a8670cc577'}]},
    #  {'id': '7044ff88-2139-4874-ac5b-b8e2275d64b5', 'name': '食品饮料', 'parent_id': '00000000-0000-0000-0000-000000000000',
    #   'child': [{'id': '4f968a14-415f-4400-be80-e05585f1dfb5', 'name': '啤酒',
    #              'parent_id': '7044ff88-2139-4874-ac5b-b8e2275d64b5'},
    #             {'id': '722a78cd-0313-44fa-82a7-79bb85ae726a', 'name': '水',
    #              'parent_id': '7044ff88-2139-4874-ac5b-b8e2275d64b5'},
    #             {'id': '880514a5-a7f2-4c0f-bdcc-01c0ef818326', 'name': '葡萄酒/酒具',
    #              'parent_id': '7044ff88-2139-4874-ac5b-b8e2275d64b5'},
    #             {'id': 'eee11a0d-5368-467b-a1de-3d110bff137d', 'name': '休闲食品',
    #              'parent_id': '7044ff88-2139-4874-ac5b-b8e2275d64b5'},
    #             {'id': 'f9004467-d514-47a3-a50c-90e1aee87ab6', 'name': '冲调饮品',
    #              'parent_id': '7044ff88-2139-4874-ac5b-b8e2275d64b5'}]},
    #  {'id': 'a250e942-b409-4483-8e37-57268ea15762', 'name': '乳品糕点', 'parent_id': '00000000-0000-0000-0000-000000000000',
    #   'child': [{'id': '8252482f-f825-462d-828a-7b0a16e7f5a3', 'name': '面包',
    #              'parent_id': 'a250e942-b409-4483-8e37-57268ea15762'}]},
    #  {'id': 'ad7f227d-73c0-44a2-9edd-924006deb134', 'name': '进口水果', 'parent_id': '00000000-0000-0000-0000-000000000000',
    #   'child': [{'id': '06e154b9-3f2e-4dc7-8f4b-a55490fcc9ce', 'name': '柑桔橙柚',
    #              'parent_id': 'ad7f227d-73c0-44a2-9edd-924006deb134'},
    #             {'id': '1c95feae-bbe3-461f-bf4f-ef3ca80d2a93', 'name': '火龙果',
    #              'parent_id': 'ad7f227d-73c0-44a2-9edd-924006deb134'},
    #             {'id': '26d97149-fb8b-41f8-9d51-96447aefe8b1', 'name': '芒果',
    #              'parent_id': 'ad7f227d-73c0-44a2-9edd-924006deb134'},
    #             {'id': '2b040360-4b32-4615-a756-5bfda7c47b3b', 'name': '热带水果',
    #              'parent_id': 'ad7f227d-73c0-44a2-9edd-924006deb134'},
    #             {'id': '48c7855d-dbac-4b86-9b33-e097e715a15d', 'name': '梨',
    #              'parent_id': 'ad7f227d-73c0-44a2-9edd-924006deb134'},
    #             {'id': '5558b856-f46f-4cf2-bee7-4ee6a18eb72a', 'name': '莓',
    #              'parent_id': 'ad7f227d-73c0-44a2-9edd-924006deb134'},
    #             {'id': '56fad30c-1fc9-4415-9d5d-c91644f59771', 'name': '椰子',
    #              'parent_id': 'ad7f227d-73c0-44a2-9edd-924006deb134'},
    #             {'id': '5dceb73e-5507-4910-85ae-71f071be1f93', 'name': '提子',
    #              'parent_id': 'ad7f227d-73c0-44a2-9edd-924006deb134'},
    #             {'id': '5ea0d07d-0d9d-4b85-9776-8fdfb66df6db', 'name': '山竹',
    #              'parent_id': 'ad7f227d-73c0-44a2-9edd-924006deb134'},
    #             {'id': '6a2a75d7-74a5-4d6d-b2dd-8960610949a6', 'name': '李',
    #              'parent_id': 'ad7f227d-73c0-44a2-9edd-924006deb134'},
    #             {'id': '8a28d3a3-b6e9-4ff9-b8e7-a924d6219bf0', 'name': '苹果',
    #              'parent_id': 'ad7f227d-73c0-44a2-9edd-924006deb134'},
    #             {'id': '8ea31d17-5731-4a86-a98d-8d6e8804cd41', 'name': '榴莲',
    #              'parent_id': 'ad7f227d-73c0-44a2-9edd-924006deb134'},
    #             {'id': 'b379be17-8eb3-4f0e-bc7a-272a933f10af', 'name': '车厘子',
    #              'parent_id': 'ad7f227d-73c0-44a2-9edd-924006deb134'},
    #             {'id': 'b5fff91c-caef-4a8e-a1b4-bc2f44475110', 'name': '奇异果',
    #              'parent_id': 'ad7f227d-73c0-44a2-9edd-924006deb134'},
    #             {'id': 'd2594a09-48d7-4fda-9e47-ac273c2ecf65', 'name': '牛油果',
    #              'parent_id': 'ad7f227d-73c0-44a2-9edd-924006deb134'},
    #             {'id': 'd8240fb9-de89-4eb6-8f9f-74be289eb0ec', 'name': '原箱水果',
    #              'parent_id': 'ad7f227d-73c0-44a2-9edd-924006deb134'},
    #             {'id': 'ee308ae7-2916-410d-ae65-360a0024dcfb', 'name': '凤梨',
    #              'parent_id': 'ad7f227d-73c0-44a2-9edd-924006deb134'},
    #             {'id': 'fbbe6f60-ceb2-4a07-9cdf-86844277cf9e', 'name': '时令水果',
    #              'parent_id': 'ad7f227d-73c0-44a2-9edd-924006deb134'}]},
    #  {'id': 'bbbf4838-2574-4e71-9f96-328e664e6e1e', 'name': '粮油杂货', 'parent_id': '00000000-0000-0000-0000-000000000000',
    #   'child': [{'id': '11f8065c-1001-4962-a6df-d05370e3b64c', 'name': '面/面制品',
    #              'parent_id': 'bbbf4838-2574-4e71-9f96-328e664e6e1e'},
    #             {'id': '1339af62-7b56-4067-861e-f89b9e265f03', 'name': '干货',
    #              'parent_id': 'bbbf4838-2574-4e71-9f96-328e664e6e1e'},
    #             {'id': '15d4d187-3647-4fb7-a0c2-4c3d4fe1d0fc', 'name': '油',
    #              'parent_id': 'bbbf4838-2574-4e71-9f96-328e664e6e1e'},
    #             {'id': '33a7a858-ef0c-48fd-b8ec-fc2a55337461', 'name': '果干/零食',
    #              'parent_id': 'bbbf4838-2574-4e71-9f96-328e664e6e1e'},
    #             {'id': '6ac1ffc4-97a6-4cfb-b450-1862a05f040f', 'name': '米',
    #              'parent_id': 'bbbf4838-2574-4e71-9f96-328e664e6e1e'},
    #             {'id': 'a3e461f2-5c83-41ef-80e9-0a12eb503157', 'name': '调味料',
    #              'parent_id': 'bbbf4838-2574-4e71-9f96-328e664e6e1e'},
    #             {'id': 'e8460963-aa4a-4911-8220-9394117cecd6', 'name': '杂粮',
    #              'parent_id': 'bbbf4838-2574-4e71-9f96-328e664e6e1e'}]},
    #  {'id': 'be7fa57d-ce6c-4040-82f9-4aef7af0a1cb', 'name': '禽类蛋品', 'parent_id': '00000000-0000-0000-0000-000000000000',
    #   'child': [{'id': '76e8b280-c4a6-4e81-8a25-891c8635358f', 'name': '鸡',
    #              'parent_id': 'be7fa57d-ce6c-4040-82f9-4aef7af0a1cb'},
    #             {'id': '9eb1744e-050a-4c91-8097-8b50425cbfb9', 'name': '鹅/鸽/特色禽类',
    #              'parent_id': 'be7fa57d-ce6c-4040-82f9-4aef7af0a1cb'},
    #             {'id': 'c239bd4b-81dc-41dd-9291-05283648fa8f', 'name': '蛋',
    #              'parent_id': 'be7fa57d-ce6c-4040-82f9-4aef7af0a1cb'},
    #             {'id': 'dced328e-b058-4f76-9583-b87637a03124', 'name': '鸭',
    #              'parent_id': 'be7fa57d-ce6c-4040-82f9-4aef7af0a1cb'}]},
    #  {'id': 'ccd5a8ef-66ca-48d2-962c-613d23500cf9', 'name': '常温食品', 'parent_id': '00000000-0000-0000-0000-000000000000',
    #   'child': [{'id': 'aa62ac7c-9798-4d72-9993-71055ec2b2b0', 'name': '米面杂粮',
    #              'parent_id': 'ccd5a8ef-66ca-48d2-962c-613d23500cf9'}]},
    #  {'id': 'd5562ffa-2e72-4cea-9807-e481d06472f6', 'name': '方便速食', 'parent_id': '00000000-0000-0000-0000-000000000000',
    #   'child': [{'id': '0038429e-74e5-4d76-9c06-22855b9d3636', 'name': '冷冻点心',
    #              'parent_id': 'd5562ffa-2e72-4cea-9807-e481d06472f6'},
    #             {'id': '297f9732-a901-4d42-a7cd-a2cf61bdc99b', 'name': '中式主食',
    #              'parent_id': 'd5562ffa-2e72-4cea-9807-e481d06472f6'},
    #             {'id': 'ad54ecd7-2af6-4c39-b88a-6767d6a4aeb4', 'name': '半成品菜',
    #              'parent_id': 'd5562ffa-2e72-4cea-9807-e481d06472f6'},
    #             {'id': 'e6898b2c-850d-4b75-9f2c-e19c5af0de33', 'name': '火锅料',
    #              'parent_id': 'd5562ffa-2e72-4cea-9807-e481d06472f6'}]},
    #  {'id': 'e1680a10-9cd6-4ba1-98f9-50e02eb990cb', 'name': '精选肉类', 'parent_id': '00000000-0000-0000-0000-000000000000',
    #   'child': [{'id': '6a31430a-31ce-49b4-8cd1-91602abfe6a9', 'name': '牛排',
    #              'parent_id': 'e1680a10-9cd6-4ba1-98f9-50e02eb990cb'},
    #             {'id': 'c97c8152-1ef8-44cf-beb9-16c349bf5479', 'name': '肉制品',
    #              'parent_id': 'e1680a10-9cd6-4ba1-98f9-50e02eb990cb'},
    #             {'id': 'db6518e8-c360-46f7-b9ae-dbe4ae45e84c', 'name': '羊肉',
    #              'parent_id': 'e1680a10-9cd6-4ba1-98f9-50e02eb990cb'}]}]
