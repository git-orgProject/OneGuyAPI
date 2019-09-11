#!/usr/bin/python3
# coding: utf-8
from rest_framework import routers

from api.order import OrderAPIView
from api.user import UserSerializer, UserAPIView
from .cart import CartAPIView, CommodityCartAPIView
from goods.views import CommodityView
from .category import CategoryAPIView


# 声明api路由
api_router = routers.DefaultRouter()

# 向api路由中注册ViewSet
api_router.register('cart', CartAPIView)
api_router.register('CommodityCart', CommodityCartAPIView)
api_router.register('Category',CategoryAPIView)
api_router.register('user',UserAPIView)
api_router.register('order',OrderAPIView)

