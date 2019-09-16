from django.urls import path

from cart import views

app_name = 'cart'

urlpatterns = [
    path('cartshow/', views.cartshow, name="cartshow"),
]
