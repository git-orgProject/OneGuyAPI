from django.urls import path,include
from user import views

app_name = 'user'


urlpatterns = [
    path('index/', views.index),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
    # path('imgcode/', views.new_img_code),
    path('captcha/',include('captcha.urls'))

]