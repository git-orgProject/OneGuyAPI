
from django.urls import path
from .views import CommodityViewALL,CommodityViewPK,CommodityViewFK




# coding: utf-8
from django.urls import path


from .api_category import category_api_detail, CategoryAPIView
from .views_1 import FirstCategoryView, SecondCategoryView, CouponView, product_category_list

app_name = 'goods'


urlpatterns = [
            path('api/<str:pk>', category_api_detail, name='category'),
            path('api/',CategoryAPIView.as_view(), name='category_1'),
            path('f_category',FirstCategoryView.as_view(),name="first_category"),
            path('commodity/',CommodityViewALL.as_view(),name='commodity_all'),
<<<<<<< HEAD
            path('commodity/<str:id>',CommodityViewPK.as_view(),name='commodity_pk'),
            path('commodityfk/<str:categoryId>',CommodityModelViewFK.as_view(),name='commodity_fk'),
            path('s_category/<str:fk>',SecondCategoryView.as_view(),name="second_category"),
            path('coupon/<str:userid>',CouponView.as_view(),name='CouponView'),
            path('category_list',product_category_list),

=======
            path('commoditypk',CommodityViewPK.as_view(),name='commodity_pk'),
            path('commodityfk',CommodityViewFK.as_view(),name='commodity_fk'),
>>>>>>> 0b6934bdf3f5b5ab84c3982d09adbe4a82c59b2b



]






