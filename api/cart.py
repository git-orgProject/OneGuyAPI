#!/usr/bin/python3
# coding: utf-8

from rest_framework import serializers, viewsets
from cart.models import CommodityCart, CartModel
from api.commodity import CommodityModelSerializer
from api.user import UserSerializer



class CartSerializer(serializers.HyperlinkedModelSerializer):
    user_id = UserSerializer()

    class Meta:
        model = CartModel
        fields = ('user', 'user_state')


class CartAPIView(viewsets.ModelViewSet):
    queryset = CartModel.objects.all()
    serializer_class = CartSerializer


class CommodityCartSerializer(serializers.HyperlinkedModelSerializer):
    cart = CartSerializer()
    commondity = CommodityModelSerializer()

    class Meta:
        model = CommodityCart
        fields = ('cart', 'commondity', 'count', 'total_price', 'is_choice')


class CommodityCartAPIView(viewsets.ModelViewSet):
    queryset = CommodityCart.objects.all()
    serializer_class = CommodityCartSerializer
