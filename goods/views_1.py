from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import CategoryModel
from api.category import CategorySerializer



@api_view(['GET', 'PUT', 'DELETE'])
def user_api_detail(request, pk):
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
