from django.urls import path
from .views import CommodityView
app_name = 'goods'


urlpatterns = [
            path('commodity/',CommodityView.as_view(),name='commodity'),
            path('commodity/<pk>',CommodityView.as_view(),name='commodity')
]