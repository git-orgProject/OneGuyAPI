from django.urls import path

from activity.views import CityView, NavlistView, AreaModelView, ActiveModelView, AreaCommodModelView, first_page

app_name = 'activity'

urlpatterns = [
    path('city/', CityView.as_view(), name='city'),
    path('nav/', NavlistView.as_view(), name='nav'),
    path('area/', AreaModelView.as_view(), name='area'),
    path('act/', ActiveModelView.as_view(), name='act'),
    path('area/commod/', AreaCommodModelView.as_view(), name='area_commod'),
    path('page/',first_page, name='page'),
]