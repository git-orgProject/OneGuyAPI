from django.http import JsonResponse
from rest_framework import status
from django.views import View
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CategoryModel,CouponModel
from api.category import CategorySerializer





class CategoryAPIView(APIView):
    def get(self, request):
        datas = CouponModel.objects.all()
        serializer = CategorySerializer(datas, many=True)

        return Response(serializer.data,status=status.HTTP_204_NO_CONTENT)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.instance)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def category_api_detail(request, pk):
    print(type(request))
    print(type(request.GET))
    print(type(request.POST),1)
    method = request.method
    instance = CategoryModel.objects.get(pk=pk)
    if method == 'GET':
        serializer = CategorySerializer(instance)
        return Response(serializer.data)

    elif method == 'PUT':
        print(request.data)
        serializer = CategorySerializer(instance, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(instance,
                            status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    if method == 'DELETE':
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
