
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
<<<<<<< HEAD
            path('commodity/',CommodityViewALL.as_view(),name='commodity_all'),

            path('commodity/<str:id>',CommodityViewPK.as_view(),name='commodity_pk'),
=======
>>>>>>> e7e427a2e5e25056c3a5de453e0f4693ff694644
            path('s_category/<str:fk>',SecondCategoryView.as_view(),name="second_category"),
            path('coupon/<str:userid>',CouponView.as_view(),name='CouponView'),
            path('category_list',product_category_list),

<<<<<<< HEAD

            path('commoditypk',CommodityViewPK.as_view(),name='commodity_pk'),
            path('commodityfk',CommodityViewFK.as_view(),name='commodity_fk'),

            path('coupon/<str:userid>',CouponView.as_view(),name='CouponView')



=======
            path('commodity/', CommodityViewALL.as_view(), name='commodity_all'),
            path('commoditypk',CommodityViewPK.as_view(),name='commodity_pk'),
            path('commodityfk',CommodityViewFK.as_view(),name='commodity_fk'),


>>>>>>> e7e427a2e5e25056c3a5de453e0f4693ff694644

]






