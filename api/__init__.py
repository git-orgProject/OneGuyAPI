#!/usr/bin/python3
# coding: utf-8
from rest_framework import routers

from .cart import CartAPIView, CommodityCartAPIView
from .goods import CategoryAPIView

# 声明api路由
api_router = routers.DefaultRouter()

# 向api路由中注册ViewSet
api_router.register('cart', CartAPIView)
api_router.register('CommodityCart', CommodityCartAPIView)
api_router.register('Category',CategoryAPIView)
