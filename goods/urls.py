
from django.urls import path
from .views import CommodityView


# coding: utf-8
from django.urls import path


from .api_category import category_api_detail, CategoryAPIView
from .views_1 import FirstCategoryView

app_name = 'goods'


urlpatterns = [
            path('api/<str:pk>', category_api_detail, name='category'),
            path('api/',CategoryAPIView.as_view(), name='category_1'),
            path('f_category',FirstCategoryView.as_view(),name="first_category"),
            path('commodity/<str:fk>',CommodityView.as_view(),name='commodity'),
            path('commodity/<str:pk>',CommodityView.as_view(),name='commodity_details')
]






