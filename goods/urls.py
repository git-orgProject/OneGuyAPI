
from django.urls import path
from .views import CommodityViewALL,CommodityViewPK,CommodityViewFK




# coding: utf-8
from django.urls import path


from .api_category import category_api_detail, CategoryAPIView
from .views_1 import FirstCategoryView, SecondCategoryView, CouponView

app_name = 'goods'


urlpatterns = [
            path('api/<str:pk>', category_api_detail, name='category'),
            path('api/',CategoryAPIView.as_view(), name='category_1'),
            path('f_category',FirstCategoryView.as_view(),name="first_category"),

            path('commodity/',CommodityViewALL.as_view(),name='commodity_all'),
            path('commoditypk',CommodityViewPK.as_view(),name='commodity_pk'),
            path('commodityfk',CommodityViewFK.as_view(),name='commodity_fk'),

            path('s_category/<str:fk>',SecondCategoryView.as_view(),name="second_category"),
            path('coupon/<str:userid>',CouponView.as_view(),name='CouponView')


]






