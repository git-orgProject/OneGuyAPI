from django.urls import path

from activity.views import CityView, NavlistView, AreaModelView, ActiveModelView

app_name = 'activity'

urlpatterns = [
    path('city/', CityView.as_view(), name='city'),
    path('nav/', NavlistView.as_view(), name='nav'),
    path('area/<name>', AreaModelView.as_view(), name='area'),
    path('act/', ActiveModelView.as_view(), name='act'),
]