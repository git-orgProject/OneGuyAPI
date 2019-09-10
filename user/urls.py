from django.urls import path
from user import views

app_name = 'user'


urlpatterns = [
    path('index/', views.index),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),

]