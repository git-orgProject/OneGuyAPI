from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from user.views import UserView

app_name = 'user'


urlpatterns = [
    path('login/', csrf_exempt(UserView.as_view())),
]