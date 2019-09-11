<<<<<<< HEAD
from django.urls import path
from .views import CommodityView
=======

# coding: utf-8
from django.urls import path


from .api_category import category_api_detail, CategoryAPIView
from .views_1 import FirstCategoryView
>>>>>>> 7a48eca4b4eecd9fbd0579c7d5a04ca4c96bce2c
app_name = 'goods'


urlpatterns = [
<<<<<<< HEAD
            path('commodity/',CommodityView.as_view(),name='commodity'),
            path('commodity/<pk>',CommodityView.as_view(),name='commodity')
]
=======
    path('api/<str:pk>', category_api_detail, name='category'),
    path('api/',CategoryAPIView.as_view(), name='category_1'),
    path('f_category',FirstCategoryView.as_view(),name="first_category"),

]

>>>>>>> 7a48eca4b4eecd9fbd0579c7d5a04ca4c96bce2c
