
from django.urls import path
from .views import CommodityViewALL,CommodityModelViewFK,CommodityViewPK




# coding: utf-8
from django.urls import path


from .api_category import category_api_detail, CategoryAPIView
from .views_1 import FirstCategoryView, SecondCategoryView, CouponView

app_name = 'goods'


urlpatterns = [
            path('api/<str:pk>', category_api_detail, name='category'),
            path('api/',CategoryAPIView.as_view(), name='category_1'),
            path('f_category',FirstCategoryView.as_view(),name="first_category"),
<<<<<<< HEAD
            path('commodity/',CommodityViewALL.as_view(),name='commodity_all'),
            path('commodity/<str:id>',CommodityViewPK.as_view(),name='commodity_pk'),
            path('commodityfk/<str:categoryId>',CommodityModelViewFK.as_view(),name='commodity_fk'),


=======
            path('s_category/<str:fk>',SecondCategoryView.as_view(),name="second_category"),
            path('commodity/<str:fk>',CommodityView.as_view(),name='commodity'),
            path('commodity/<str:pk>',CommodityView.as_view(),name='commodity_details'),
            path('coupon/<str:userid>',CouponView.as_view(),name='CouponView')
>>>>>>> 860cfa3f7a82fb44822d7dc248938d0d5747f77c
]






