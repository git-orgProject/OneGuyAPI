#!/usr/bin/python3
# coding: utf-8

from rest_framework import serializers, viewsets
from cart.models import CommodityCart, CartModel
from api.commodity import CommodityModelSerializer


class CartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CartModel
        fields = ('user_id', 'user_state')


class CartAPIView(viewsets.ModelViewSet):
    queryset = CartModel.objects.all()
    serializer_class = CartSerializer


class CommodityCartSerializer(serializers.HyperlinkedModelSerializer):
    cart = CartSerializer()
    goods = CommodityModelSerializer()
    class Meta:
        model = CartModel
        fields = ('cart', 'commondity', 'count', 'is_choice')


class CommodityCartAPIView(viewsets.ModelViewSet):
    queryset = CommodityCart.objects.all()
    serializer_class = CommodityCartSerializer

