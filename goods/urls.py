
from django.urls import path
from .views import CommodityViewALL,CommodityModelViewFK,CommodityViewPK




# coding: utf-8
from django.urls import path


from .api_category import category_api_detail, CategoryAPIView
from .views_1 import FirstCategoryView

app_name = 'goods'


urlpatterns = [
            path('api/<str:pk>', category_api_detail, name='category'),
            path('api/',CategoryAPIView.as_view(), name='category_1'),
            path('f_category',FirstCategoryView.as_view(),name="first_category"),
            path('commodity/',CommodityViewALL.as_view(),name='commodity_all'),
            path('commodity/<str:id>',CommodityViewPK.as_view(),name='commodity_pk'),
            path('commodityfk/<str:categoryId>',CommodityModelViewFK.as_view(),name='commodity_fk'),


]






