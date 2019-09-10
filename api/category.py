#!/usr/bin/python3
#coding:utf-8
from rest_framework import serializers, viewsets

from goods.models import CategoryModel



class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ( 'code', 'name', 'grade','picture_url')


class CategoryAPIView(viewsets.ModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer